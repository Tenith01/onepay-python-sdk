# Contributing to OnePay Python SDK

First off, thank you for considering contributing to OnePay! It's people like you that make this SDK a great tool for the community.

## Development Environment Setup

1. Fork the repository and clone it locally.
2. Ensure you have Python 3.9+ installed.
3. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
4. Install the package in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
5. Install `pre-commit` to ensure code quality before pushing:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Development Workflow

- **Code Style**: This project uses `ruff` for both linting and formatting. The pre-commit hooks will automatically format your code.
- **Type Checking**: We use `mypy` for static type checking. Ensure you add type hints to all new functions.
- **Testing**: We use `pytest`. All new features should have accompanying tests.
  ```bash
  pytest
  ```
  To check coverage:
  ```bash
  pytest --cov=src/onepay
  ```

## Pull Request Process

1. Create a new branch from `main` (e.g., `feature/add-new-endpoint` or `fix/handle-timeout`).
2. Make your changes and commit them with clear, descriptive messages.
3. Push your branch and open a Pull Request against the `main` branch.
4. Ensure all CI checks pass (linting, type checking, tests).
5. A maintainer will review your PR and provide feedback.

## Reporting Issues

If you find a bug or have a feature request, please use the issue templates provided in the `.github/ISSUE_TEMPLATE` directory.
