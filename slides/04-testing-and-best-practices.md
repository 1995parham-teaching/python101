---
marp: true
theme: gaia
class: invert
paginate: true
header: "Python 101"
footer: "Testing & Best Practices"
style: |
  :root {
    --color-background: #1e1e2e;
    --color-foreground: #cdd6f4;
    --color-highlight: #ff6b35;
  }
  section {
    background-color: #1e1e2e;
  }
  h1, h2, h3, h4, h5, h6 {
    color: #ff6b35;
  }
  a {
    color: #fab387;
  }
  code {
    background-color: #313244;
  }
  blockquote {
    border-left-color: #ff6b35;
  }
---

# Python 101: Week 4

**Testing, Type Hints & Best Practices**

---

# Testing with pytest

---

## Why Test?

- **Catch bugs early** - before production
- **Refactor with confidence** - tests verify nothing broke
- **Documentation** - tests show how code should work
- **Design feedback** - hard to test = bad design

---

## Basic Tests

```python
# test_calculator.py
def add(a, b):
    return a + b

# Test functions start with 'test_'
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5
```

```bash
# Run tests
pytest test_calculator.py -v
```

---

## Testing Exceptions

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc:
        divide(10, 0)
    assert "zero" in str(exc.value)
```

---

## Fixtures

```python
import pytest

@pytest.fixture
def database():
    """Set up test database."""
    db = {"users": []}
    yield db  # Provide to test
    db.clear()  # Cleanup after test

def test_add_user(database):
    database["users"].append("Alice")
    assert len(database["users"]) == 1

def test_empty_database(database):
    assert len(database["users"]) == 0
```

---

## Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Runs 4 separate tests with different inputs
```

---

## Mocking

```python
from unittest.mock import patch, MagicMock

def fetch_user(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")
    return response.json()

def test_fetch_user():
    # Create mock
    mock_client = MagicMock()
    mock_client.get.return_value.json.return_value = {
        "id": 1,
        "name": "Alice"
    }

    result = fetch_user(mock_client, 1)

    assert result["name"] == "Alice"
    mock_client.get.assert_called_once_with("/users/1")
```

---

# Type Hints

---

## Why Type Hints?

- **Better IDE support** - autocomplete, error detection
- **Self-documenting code** - types are documentation
- **Catch bugs early** - with mypy static checker
- **No runtime cost** - hints are ignored at runtime

---

## Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Variable annotations
age: int = 25
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95}
```

---

## Optional and Union

```python
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    """Return user or None if not found."""
    users = {1: {"name": "Alice"}}
    return users.get(user_id)

# Union types (Python 3.10+)
def process(value: str | int) -> str:
    return str(value)

# Earlier Python
from typing import Union
def process(value: Union[str, int]) -> str:
    return str(value)
```

---

## Collections and Callables

```python
from typing import Callable
from collections.abc import Iterable

def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

def sum_values(values: Iterable[int]) -> int:
    return sum(values)

def apply(x: int, func: Callable[[int], int]) -> int:
    return func(x)

# Usage
apply(5, lambda x: x * 2)  # 10
```

---

## Generics with TypeVar

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    """Return first item, preserving type."""
    return items[0]

# Type is inferred:
num: int = first([1, 2, 3])
text: str = first(["a", "b"])
```

---

## Running mypy

```bash
# Install mypy
pip install mypy

# Check a file
mypy my_script.py

# Check with strict mode
mypy --strict my_script.py

# Configuration in pyproject.toml
[tool.mypy]
python_version = "3.12"
strict = true
```

---

# Best Practices

---

## PEP 8 Style Guide

```python
# Good naming
def calculate_total_price(items: list) -> float:
    pass

class UserAuthentication:
    pass

MAXIMUM_CONNECTIONS = 100

# Good formatting
result = long_function_name(
    argument_one,
    argument_two,
    argument_three,
)
```

---

## Code Formatting Tools

```bash
# Black - opinionated formatter
pip install black
black my_script.py

# Ruff - fast linter + formatter
pip install ruff
ruff check .
ruff format .

# Configure in pyproject.toml
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88
```

---

## Documentation

```python
def calculate_discount(
    price: float,
    discount_percent: float,
    min_price: float = 0
) -> float:
    """
    Calculate the discounted price.

    Args:
        price: Original price in dollars
        discount_percent: Discount percentage (0-100)
        min_price: Minimum allowed price

    Returns:
        The discounted price, at least min_price

    Raises:
        ValueError: If discount_percent is negative
    """
    if discount_percent < 0:
        raise ValueError("Discount cannot be negative")
    discounted = price * (1 - discount_percent / 100)
    return max(discounted, min_price)
```

---

## Error Handling

```python
# Specific exceptions
class UserNotFoundError(Exception):
    pass

def get_user(user_id: int) -> dict:
    if user_id not in database:
        raise UserNotFoundError(f"User {user_id} not found")
    return database[user_id]

# Handle at appropriate level
try:
    user = get_user(123)
except UserNotFoundError:
    logger.warning("User not found")
    user = create_default_user()
except DatabaseError:
    logger.error("Database connection failed")
    raise
```

---

## Project Structure

```
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── conftest.py
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## pyproject.toml

```toml
[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "aiohttp>=3.8",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "mypy>=1.0",
    "ruff>=0.1",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

## Design Principles

**SOLID:**
- **S**ingle Responsibility - one reason to change
- **O**pen/Closed - open for extension, closed for modification
- **L**iskov Substitution - subtypes must be substitutable
- **I**nterface Segregation - small, focused interfaces
- **D**ependency Inversion - depend on abstractions

**Keep it simple:**
- Avoid premature optimization
- Write readable code
- Prefer composition over inheritance

---

## Common Patterns

```python
# Context Manager
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")

with timer():
    do_work()

# Singleton
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

# Practice Exercises

1. Write tests for a shopping cart class
2. Add type hints to existing code and run mypy
3. Set up pre-commit hooks for formatting
4. Create a properly structured Python package

---

# Summary

- **Testing** - pytest for confidence and documentation
- **Type Hints** - better tooling and documentation
- **Code Quality** - black, ruff, mypy
- **Best Practices** - PEP 8, SOLID, clear structure

See `src/10-testing/` and `src/11-typing/` for examples!

---

# Thank You!

**Resources:**
- `src/` - All code examples
- `slides/` - These presentations
- Python docs: docs.python.org

Happy coding! 🐍
