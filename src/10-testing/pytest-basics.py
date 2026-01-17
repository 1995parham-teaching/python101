"""
Topic: Testing with pytest
Concepts: test functions, assertions, fixtures, parametrize
Learning objectives:
    - Write test functions following pytest conventions
    - Use assertions for test verification
    - Create fixtures for test setup
    - Use parametrize for data-driven tests

Note: Run with 'pytest pytest-basics.py -v' (requires 'pip install pytest')

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import pytest


# === Code to Test ===
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """Simple calculator class for testing."""

    def __init__(self):
        self.history = []

    def add(self, a: int, b: int) -> int:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def clear_history(self):
        self.history = []


# === Basic Tests ===
def test_add_positive_numbers():
    """Test adding two positive numbers."""
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0


def test_add_with_zero():
    """Test adding with zero."""
    assert add(0, 5) == 5
    assert add(5, 0) == 5


# === Testing Exceptions ===
def test_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "Cannot divide by zero" in str(exc_info.value)


def test_divide_normal():
    """Test normal division."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


# === Fixtures ===
@pytest.fixture
def calculator():
    """Create a Calculator instance for testing."""
    calc = Calculator()
    yield calc  # Provide the fixture
    # Cleanup after test (optional)
    calc.clear_history()


def test_calculator_add(calculator):
    """Test calculator addition using fixture."""
    result = calculator.add(2, 3)
    assert result == 5
    assert len(calculator.history) == 1


def test_calculator_history(calculator):
    """Test calculator history tracking."""
    calculator.add(1, 2)
    calculator.add(3, 4)
    assert len(calculator.history) == 2
    assert "1 + 2 = 3" in calculator.history


# === Parametrized Tests ===
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (-5, -5, -10),
    ],
)
def test_add_parametrized(a, b, expected):
    """Test add function with multiple input combinations."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (7, 2, 3.5),
        (-10, 2, -5.0),
    ],
)
def test_divide_parametrized(a, b, expected):
    """Test divide function with multiple inputs."""
    assert divide(a, b) == expected


# === Run Tests (for demonstration) ===
if __name__ == "__main__":
    # You can run with: pytest pytest-basics.py -v
    # Or run this file directly for a quick check
    print("Running basic assertions...")
    assert add(2, 3) == 5
    assert divide(10, 2) == 5.0
    print("All basic checks passed!")
    print("\nFor full test output, run: pytest pytest-basics.py -v")


# === Expected Output (with pytest -v) ===
# pytest-basics.py::test_add_positive_numbers PASSED
# pytest-basics.py::test_add_negative_numbers PASSED
# pytest-basics.py::test_add_with_zero PASSED
# pytest-basics.py::test_divide_by_zero PASSED
# pytest-basics.py::test_divide_normal PASSED
# pytest-basics.py::test_calculator_add PASSED
# pytest-basics.py::test_calculator_history PASSED
# pytest-basics.py::test_add_parametrized[1-1-2] PASSED
# pytest-basics.py::test_add_parametrized[0-0-0] PASSED
# ... (more parametrized tests)

# === Exercises ===
# 1. Add a fixture with scope="module" that sets up a database connection
# 2. Write tests for edge cases (very large numbers, floats, etc.)
