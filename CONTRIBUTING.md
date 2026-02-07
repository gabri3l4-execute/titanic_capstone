# CONTRIBUTING.md

This document defines how the team collaborates, reviews code, and maintains a clean, reproducible project.

---

## Collaboration principles

- One branch per task to keep work isolated and reviewable
- Small, focused commits that tell a clear story
- At least one pull request per person per task
- No direct commits to `main`
- Every pull request requires review and approval from a teammate

---

## Branching rules

- Branch names follow a consistent pattern:
  - `feature/<task-name>`
  - `fix/<bug-name>`
  - `refactor/<scope>`
- Each Trello/Notion task corresponds to one branch
- Branches stay short‑lived and are merged as soon as the task is complete
- After merging, the branch is deleted

---

## Commit rules

- Commit messages use conventional prefixes:
  - **feat:** new feature
  - **fix:** bug fix
  - **refactor:** structural changes without new behavior
  - **docs:** documentation updates
  - **test:** tests added or updated
  - **chore:** maintenance tasks
- Write messages in imperative form (“Add feature”, not “Added feature”)
- Keep commits small, atomic, and logically grouped

---

## Pull request workflow

- PR title describes the change clearly
- PR links to the corresponding task
- PR includes a short summary of what changed and why
- Code must run without errors before requesting review
- At least one teammate reviews and approves before merging
- No self‑merging unless explicitly agreed by the team
- Branch is deleted after merge

---

## Code style and structure

- Follow the project folder layout:
  - `ml/` for production ML code
  - `webapp/` for Django application code
  - `notebooks/` for exploratory work
- Keep notebooks out of production modules
- Move stable logic from notebooks into Python files under `ml/`
- Follow PEP8 for Python code
- Keep functions small, clear, and testable

---

## Environment and reproducibility

- Never commit secrets or `.env` files
- Update `environment.yml` only when adding or removing dependencies
- Regenerate `environment.lock.yml` after major environment changes
- Always activate the project environment before running notebooks or Django

---

## Documentation expectations

- Update `README.md` when adding new features or changing setup steps
- Add comments to complex functions or non‑obvious logic
- Keep notebooks annotated with markdown explaining decisions and findings

---

## Communication

- Use clear, concise messages in pull requests and commits
- Ask questions early when blocked
- Keep discussions respectful and focused on the work
