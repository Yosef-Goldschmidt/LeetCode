"""
LeetCode minimal scaffold generator (signature-only).

Usage:
  python new.py 217
  python new.py

Creates:
  python/xxxx_problem_name/
      problem_name.py
      test_problem_name.py
"""

import re
import sys
from pathlib import Path
from typing import Optional, Tuple

import requests
from requests.exceptions import RequestException


LEETCODE_ALL_URL = "https://leetcode.com/api/problems/all/"
LEETCODE_GQL_URL = "https://leetcode.com/graphql"
HEADERS = {"User-Agent": "Mozilla/5.0"}


# ---------- Helpers ----------

def sanitize_name(name: str) -> str:
    name = name.lower().replace("-", "_").replace(" ", "_")
    name = re.sub(r"[^a-z0-9_]", "", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")


def fetch_slug_title(problem_number: str) -> Tuple[Optional[str], Optional[str]]:
    try:
        print(f"Fetching basic data for #{problem_number}...")
        r = requests.get(LEETCODE_ALL_URL, headers=HEADERS, timeout=10)
        r.raise_for_status()
        data = r.json()

        for q in data.get("stat_status_pairs", []):
            stat = q.get("stat", {})
            if str(stat.get("frontend_question_id")) == problem_number:
                return (
                    stat.get("question__title_slug"),
                    stat.get("question__title"),
                )

        return None, None

    except (RequestException, ValueError) as e:
        print(f"[Warning] API error: {e}")
        return None, None


def fetch_python_stub(slug: str) -> Optional[str]:
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        codeSnippets {
          langSlug
          code
        }
      }
    }
    """

    payload = {"query": query, "variables": {"titleSlug": slug}}

    try:
        print("Fetching Python starter code...")
        r = requests.post(LEETCODE_GQL_URL, json=payload, headers=HEADERS, timeout=10)
        r.raise_for_status()
        data = r.json()

        snippets = ((data.get("data") or {}).get("question") or {}).get("codeSnippets")

        if not isinstance(snippets, list):
            return None

        for sn in snippets:
            if sn.get("langSlug") in ("python3", "python"):
                code = sn.get("code")
                if code and code.strip():
                    return code.strip()

        return None

    except (RequestException, ValueError) as e:
        print(f"[Warning] GraphQL error: {e}")
        return None


# ---------- Stub Fixes ----------

def fix_typing_generics(stub: str) -> str:
    """Replace typing generics to avoid imports."""
    stub = re.sub(r"\bList\[", "list[", stub)
    stub = re.sub(r"\bOptional\[", "Optional[", stub)
    return stub


def ensure_stub_is_runnable(stub: str) -> str:
    """
    Ensure every function has a body (insert 'pass' if missing).
    """
    lines = stub.splitlines()
    output = []
    i = 0

    while i < len(lines):
        line = lines[i]
        output.append(line)

        match = re.match(r"^(\s*)def\s+.+:\s*$", line)
        if match:
            indent = match.group(1)
            body_indent = indent + " " * 4

            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1

            if j >= len(lines) or not lines[j].startswith(body_indent):
                output.append(body_indent + "pass")

        i += 1

    return "\n".join(output).rstrip() + "\n"


def build_fallback_solution() -> str:
    return (
        "class Solution:\n"
        "    def method_name(self, ...):\n"
        "        pass\n"
    )


# ---------- Scaffold ----------

def create_problem(cli_arg: Optional[str] = None) -> None:
    base_dir = Path(__file__).parent.resolve()

    problem_number = cli_arg if cli_arg else input("Enter problem number: ").strip()
    if not problem_number.isdigit():
        print("Problem number must be numeric.")
        return

    slug, title = fetch_slug_title(problem_number)

    if slug and title:
        module_name = sanitize_name(slug)
        problem_url = f"https://leetcode.com/problems/{slug}/"
        stub = fetch_python_stub(slug)
    else:
        manual_name = input("Problem name: ").strip()
        if not manual_name:
            return
        module_name = sanitize_name(manual_name)
        title = manual_name
        problem_url = ""
        stub = None

    folder_name = f"{problem_number.zfill(4)}_{module_name}"
    target_dir = base_dir / folder_name

    if target_dir.exists():
        print("Folder already exists.")
        return

    target_dir.mkdir()

    if stub:
        stub = fix_typing_generics(stub)
        stub = ensure_stub_is_runnable(stub)
    else:
        stub = build_fallback_solution()

    solution_content = (
        f'"""\nLeetCode {problem_number}: {title}\n{problem_url}\n"""\n\n'
        "# ---------- STARTER CODE ----------\n\n"
        + stub
    )

    test_content = f"""import pytest
from {module_name} import Solution


def test_basic_case():
    sol = Solution()
    pytest.fail("Test not implemented yet")
"""

    (target_dir / f"{module_name}.py").write_text(solution_content, encoding="utf-8")
    (target_dir / f"test_{module_name}.py").write_text(test_content, encoding="utf-8")

    print(f"Created {folder_name}")
    print(f"Run tests: pytest {folder_name}")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    create_problem(arg)
