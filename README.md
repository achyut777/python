# Python — Daily Practice Repository

Welcome! This repository is your personal / shared space for learning and practicing Python.
Add one Python file per day (or per exercise), keep each file focused and self-contained, and use the short guidelines below so the collection stays consistent and easy to navigate.

## What this repo is for

- Daily exercises, mini-projects, notes, and examples in Python.
- Each file should be a runnable Python script or a small module that demonstrates a concept.
- Use this repo as a learning journal: add files, commit, and (optionally) open PRs for review.

## Recommended file naming convention

Use a predictable filename so it's easy to find entries and sort by date:

- YYYY-MM-DD-topic.py  — e.g. `2025-10-26-string-methods.py`
- topic-YYYY-MM-DD.py  — if you prefer topic-first sorting
- or keep descriptive names like `python_basics.py` for broader lessons

Try to keep filenames lowercase, use hyphens for spaces, and avoid special characters.

## Example file in this repo

- `python_basics.py` — a comprehensive beginner-friendly walk through basic Python concepts.

## How to run a file (Windows PowerShell)

Open PowerShell in this repo folder and run:

```powershell
python .\python_basics.py
```

Or run any other file the same way, e.g.: `python .\2025-10-26-list-comprehensions.py`.

If you use Python 3.x as `python3` on your system, replace `python` with `python3`.

## How to contribute / add a daily file

1. Create a new branch: `git checkout -b feat/YYYY-MM-DD-topic`
2. Add your file following the naming convention above.
3. Keep the file focused: include a small header comment describing the goal and how to run it.
4. Run the file locally to verify it executes without errors.
5. Commit and push your branch, then open a PR for review (if collaborating).

Suggested small header for each file:

```python
"""
YYYY-MM-DD — short description of the exercise

How to run:
	python .\<filename>.py
"""
```

## Style and tips

- Keep scripts small and focused (one concept per file when possible).
- Add comments and a short docstring at the top explaining the purpose.
- Avoid putting large datasets into the repo; prefer small examples or generated data.
- If code grows, consider moving reusable parts into a `src/` package and adding tests.

## Optional: Tests & Automation

If you later add tests, create a `tests/` folder and a `requirements.txt` or `pyproject.toml` to manage dependencies.

## License

If this is your personal repo, choose a license you prefer (MIT is a common option). Add a `LICENSE` file if you want.

## Contact / Notes

If this is collaborative, add a short `CONTRIBUTING.md` and a CODE_OF_CONDUCT when you're ready.

Happy learning — add a new Python file today! 🚀

