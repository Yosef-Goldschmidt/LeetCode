# 🚀 LeetCode Solutions (Python)

A collection of LeetCode problems solved in Python, focusing on clean code, test-driven development (TDD), and a disciplined Git workflow.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Testing](https://img.shields.io/badge/Testing-pytest-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📂 Repository Structure

Each problem is isolated in its own directory under `python/`, containing both the solution and unit tests.

```text
.
├── python/
│   ├── 0001-two-sum/
│   │   ├── solution.py         # Source code
│   │   └── test_solution.py    # Unit tests
│   └── 0217-contains-duplicate/
│       ├── ...
├── WORKFLOW.md                 # Detailed Git & contribution guide
└── README.md
```

---

## 🛠️ Getting Started

### Prerequisites
* Python 3.8 or higher
* Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Install testing framework:**
    ```bash
    pip install pytest
    ```

---

## 🧪 Running Tests

This project uses `pytest` for testing. You can run tests at different levels:

**Run all tests (entire repo):**
```bash
pytest
```

**Run tests for a specific problem:**
```bash
pytest python/0001-two-sum/
```

**Run verbose mode (see individual test cases):**
```bash
pytest -v
```

---

## 📝 Workflow Summary

We follow a strict **Branch-per-Problem** workflow.

1.  **Sync** local main: `git checkout main && git pull --rebase`
2.  **Branch** out: `git checkout -b lc-XXXX`
3.  **Solve** & Test: `mkdir python/XXXX` ...
4.  **Commit**: `git commit -m "Solve LC XXXX..."`
5.  **PR**: Open Pull Request -> Squash & Merge.

> 📖 **Read the full guide:** For detailed commands and conventions, please refer to [WORKFLOW.md](WORKFLOW.md).

---

## ⚖️ License

This project is open source and available under the [MIT License](LICENSE).
