# WORKFLOW.md — LeetCode Git + GitHub + Pytest Workflow

This repository uses a **branch-per-problem** workflow with **GitHub Pull Requests** and **Squash & Merge**.

The goals:
- Clean Git history
- Realistic GitHub workflow practice
- Reproducible steps every time

---

## 📋 Repository Conventions

### Branch Naming
Use one branch per problem. Be consistent.
* `lc-XXXX` (e.g., `lc-0217`)
* `lc-0001-two-sum`

### File Structure
```text
python/
└── XXXX-problem-name/
    ├── solution.py
    └── test_solution.py
```

---

## 🚀 Standard Workflow (EVERY LeetCode problem)

### 0. Sync Main (Start here)
Never start new work without this step.
```bash
git checkout main
git pull --rebase
```

### 1. Create a New Branch
Never work directly on main.
```bash
git checkout -b lc-XXXX
```
*Verify with `git status` that you are on the new branch.*

### 2. Create Files and Solve
Create the directory and necessary files:
```bash
mkdir -p python/XXXX-problem-name
# Create solution.py and test_solution.py
```

### 3. Run Tests
Run `pytest` from the **repository root**:
```bash
pytest
```
> **Note:** If 0 items are collected, ensure file names and function names start with `test_`.

### 4. Stage Changes
Only stage files related to this problem.
```bash
git add python/XXXX-problem-name
```

### 5. Commit
One problem = one commit.
```bash
git commit -m "Solve LC XXXX Problem Name (Python)"
```

### 6. Push Branch
**First push:**
```bash
git push -u origin lc-XXXX
```
**Subsequent pushes:**
```bash
git push
```

### 7. Open Pull Request
Go to GitHub and open a PR:
* **Base branch:** `main`
* **Compare branch:** `lc-XXXX`
* **Merge method:** Squash and merge

### 8. Sync Local Main (REQUIRED)
Squash merge creates a new commit on GitHub. You must sync locally.
```bash
git checkout main
git pull --rebase
```

### 9. Delete the Branch
Cleanup your local and remote environment.
```bash
# Delete locally (use -D because of squash merge)
git branch -D lc-XXXX

# Delete remote
git push origin --delete lc-XXXX

# Optional cleanup
git fetch --prune
```

---

## 🧪 Pytest Template

### `solution.py`
```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

### `test_solution.py`
```python
from solution import Solution

def test_contains_duplicate():
    s = Solution()
    assert s.containsDuplicate([1, 2, 4, 5, 2]) is True
    assert s.containsDuplicate([1]) is False
    assert s.containsDuplicate([1, 2, 3]) is False
    assert s.containsDuplicate([]) is False
    assert s.containsDuplicate([-1, -1]) is True
```