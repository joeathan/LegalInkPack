# Contributing to LegalInkPack

Thank you for your interest in contributing to LegalInkPack! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

* **Clear title and description**
* **Steps to reproduce** the problem
* **Expected behavior** vs actual behavior
* **Environment details** (OS, Python version, etc.)
* **Code samples** or error messages
* **Screenshots** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

* **Clear title and description**
* **Use case** and rationale
* **Proposed solution** or approach
* **Alternative solutions** considered
* **Additional context** or examples

### Pull Requests

1. **Fork** the repository
2. **Create a branch** for your changes (`git checkout -b feature/amazing-feature`)
3. **Make your changes** following our coding standards
4. **Add tests** for new functionality
5. **Ensure tests pass** and code is linted
6. **Commit your changes** with clear messages
7. **Push to your branch** (`git push origin feature/amazing-feature`)
8. **Open a Pull Request** with a clear description

#### Pull Request Guidelines

* Follow the existing code style
* Write clear, descriptive commit messages
* Include tests for new features
* Update documentation as needed
* Keep pull requests focused on a single concern
* Link related issues in the PR description

## Development Process

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/joeathan/LegalInkPack.git
cd LegalInkPack

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=legalinkpack

# Run specific test file
pytest tests/test_specific.py
```

### Code Style

This project uses:

* **Black** for code formatting
* **isort** for import sorting
* **flake8** for linting
* **mypy** for type checking

Run all checks:

```bash
# Format code
black legalinkpack tests

# Sort imports
isort legalinkpack tests

# Lint code
flake8 legalinkpack tests

# Type check
mypy legalinkpack
```

### Commit Message Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation changes
* `style`: Code style changes (formatting, etc.)
* `refactor`: Code refactoring
* `test`: Adding or updating tests
* `chore`: Maintenance tasks

Example:
```
feat(parser): add support for new document format

Implement parsing for PDF documents with embedded metadata.
Includes validation and error handling.

Closes #123
```

## Legal Requirements

### Contributor License Agreement

By contributing to LegalInkPack, you agree that:

1. Your contributions will be licensed under the Apache License 2.0
2. You have the right to submit the code
3. Your contributions are your original work or properly attributed

### Copyright

* Add copyright headers to new files:
  ```python
  # Copyright 2025 joeathan
  #
  # Licensed under the Apache License, Version 2.0 (the "License");
  # you may not use this file except in compliance with the License.
  # You may obtain a copy of the License at
  #
  #     http://www.apache.org/licenses/LICENSE-2.0
  #
  # Unless required by applicable law or agreed to in writing, software
  # distributed under the License is distributed on an "AS IS" BASIS,
  # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  # See the License for the specific language governing permissions and
  # limitations under the License.
  ```

### Third-Party Code

* Do not include code with incompatible licenses
* Document any third-party code or dependencies
* Include attribution as required by licenses

## Review Process

1. **Automated Checks**: CI runs tests, linting, and security scans
2. **Code Review**: Maintainers review code quality and design
3. **Testing**: Verify functionality and test coverage
4. **Documentation**: Check for adequate documentation
5. **Legal Compliance**: Ensure licensing requirements are met

## Community

* Be respectful and constructive
* Help others in discussions and issues
* Share knowledge and best practices
* Follow our Code of Conduct

## Questions?

* Open an issue for questions about contributing
* Check existing documentation and issues first
* Be patient and respectful in communications

## Recognition

Contributors are recognized in:
* CHANGELOG.md
* GitHub contributors page
* Release notes for significant contributions

Thank you for contributing to LegalInkPack!
