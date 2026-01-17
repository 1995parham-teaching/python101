<h1 align="center"> Python 101 </h1>

<p align="center">
  <img alt="banner" src="./.github/assets/banner.png" height="200px" />
  <br />
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/1995parham-teaching/python101/lint.yaml?style=for-the-badge&logo=github&label=lint">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/1995parham-teaching/python101/latex.yaml?style=for-the-badge&logo=github&label=latex">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/1995parham-teaching/python101/slides.yaml?style=for-the-badge&logo=github&label=slides">
</p>

## Introduction

This repository contains sample codes, presentation slides, and exercises for the Python 101 workshop.
It covers Python fundamentals from basic syntax to advanced topics like async programming and testing.

**Online Slides:** [https://1995parham-teaching.github.io/python101/](https://1995parham-teaching.github.io/python101/)

## Repository Structure

```
python101/
├── src/                    # Python code examples
│   ├── 01-basics/          # Variables, flow control, functions
│   ├── 02-oop/             # Object-oriented programming
│   ├── 03-advanced-oop/    # Metaclasses, MRO, descriptors
│   ├── 04-functional/      # Functions, iterators, decorators
│   ├── 05-io-files/        # File I/O, pickling
│   ├── 06-networking/      # Socket programming
│   ├── 07-memory/          # Garbage collection, references
│   ├── 08-async/           # Async/await, asyncio
│   ├── 09-libraries/       # Popular libraries (requests, pathlib)
│   ├── 10-testing/         # pytest, mocking
│   └── 11-typing/          # Type hints, generics, dataclasses
├── slides/                 # Marp markdown slides
├── presentation/           # LaTeX presentations (legacy)
└── .github/workflows/      # CI/CD workflows
```

## Course Curriculum

### Week 1-2: Python Fundamentals

- Basic syntax and data types
- Flow control (if/else, loops)
- Functions and lambda expressions
- Object-oriented programming
- Classes, inheritance, and MRO

**Examples:** `src/01-basics/`, `src/02-oop/`, `src/03-advanced-oop/`

### Week 3: Libraries & Async Programming

- File I/O and pathlib
- Working with JSON
- HTTP requests with `requests` library
- Async programming with `asyncio`

**Examples:** `src/05-io-files/`, `src/08-async/`, `src/09-libraries/`

### Week 4: Best Practices

- Testing with pytest
- Type hints and mypy
- Code quality tools (ruff, black)
- Design patterns

**Examples:** `src/10-testing/`, `src/11-typing/`

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Setup

```bash
# Clone the repository
git clone https://github.com/1995parham-teaching/python101.git
cd python101

# Install dependencies (uv handles the virtual environment)
uv sync --all-extras
```

### Running Examples

Each Python file in `src/` is self-contained and can be run directly:

```bash
uv run python src/01-basics/flow-control.py
uv run python src/04-functional/iterators.py
```

### Running Tests

```bash
# Run tests (pytest is included in dev dependencies)
uv run pytest src/10-testing/ -v
```

## Building Slides

### Marp Slides (HTML)

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Build all slides
for file in slides/*.md; do
  marp "$file" --html
done
```

### LaTeX Presentations (PDF)

```bash
# Install Tectonic
# See: https://tectonic-typesetting.github.io/

# Build presentations
cd presentation/introduction && tectonic -X build
cd presentation/packages && tectonic -X build
```

## Presented At

- 7th Amirkabir Linux Festival -- 2015
- [Diginext Software Engineering Bootcamp](https://github.com/orgs/1995parham-teaching/projects/1?pane=info) -- 2023

## Contributing

Thank you for your interest in contributing to Python 101! This section provides guidelines for contributing to this educational repository.

### Ways to Contribute

#### 1. Improve Existing Examples

- Fix bugs or typos in code examples
- Add clearer comments or explanations
- Improve docstrings and documentation
- Add expected output comments
- Create additional exercises

#### 2. Add New Content

- New code examples demonstrating Python concepts
- Additional slides for topics not covered
- Translations of existing content

#### 3. Report Issues

- Report bugs in code examples
- Suggest improvements or clarifications
- Request new topics to be covered

### Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/python101.git
cd python101

# Add upstream remote
git remote add upstream https://github.com/1995parham-teaching/python101.git
```

### Set Up Development Environment

```bash
# Install development dependencies (uv handles the virtual environment)
uv sync --all-extras
```

### Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### Code Guidelines

#### Python Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add type hints where appropriate
- Include docstrings for modules, classes, and functions

#### Example File Template

Each Python file should follow this structure:

```python
"""
Topic: [Topic Name]
Concepts: [comma-separated list of concepts]
Learning objectives:
    - [Objective 1]
    - [Objective 2]

Author: [Your name] ([your email])
"""
__author__ = "[Your name]"

# ... code ...

# === Expected Output ===
# [Expected output as comments]

# === Exercises ===
# 1. [Exercise 1]
# 2. [Exercise 2]
```

#### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Reference issues when applicable

```
Add async HTTP example with aiohttp

- Demonstrates concurrent URL fetching
- Includes error handling pattern
- Closes #123
```

### Testing

Before submitting, ensure your code works:

```bash
# Run the Python file
uv run python src/path/to/your-file.py

# If adding tests, run pytest
uv run pytest src/10-testing/ -v

# Check types (if applicable)
uv run mypy src/path/to/your-file.py
```

### Submitting Changes

1. Push your branch to your fork
2. Create a Pull Request against the `main` branch
3. Provide a clear description of your changes
4. Wait for review and address any feedback

### Slide Contributions

#### Marp Slides

Slides are written in Markdown using [Marp](https://marp.app/).

```markdown
---
marp: true
theme: default
paginate: true
header: "Python 101"
footer: "Topic Name"
---

# Slide Title

Content here...

---

## Next Slide

More content...
```

#### Building Slides Locally

```bash
npm install -g @marp-team/marp-cli
marp slides/your-slide.md --html
```

### Questions?

If you have questions about contributing, please:

1. Check existing issues and pull requests
2. Open a new issue for discussion
3. Ask in the pull request

Thank you for helping improve Python education!

## Special Thanks To

- [Dr.Bakhshi](https://github.com/Bahador-Bakhshi) (Helped in holding classes)
- [Dr.Payberah](https://github.com/payberah) (Contributed to creating slides)
- [S.M.M.Ahmadpanah](https://github.com/smahmadpanah) (Contributed to editing slides)
- [E.Jalalpour](https://github.com/eljalalpour) (Contributed to editing slides)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
