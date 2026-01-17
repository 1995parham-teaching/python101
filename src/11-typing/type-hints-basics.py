"""
Topic: Type Hints in Python
Concepts: type annotations, typing module, generic types, Optional, Union
Learning objectives:
    - Add type hints to functions and variables
    - Use typing module for complex types
    - Understand type hints for documentation and tooling

Note: Type hints are not enforced at runtime - use mypy for static checking.
      Run: mypy type-hints-basics.py

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

from collections.abc import Callable, Iterable
from typing import Any


# === Basic Type Hints ===
def greet(name: str) -> str:
    """
    Function with type hints.

    Args:
        name: The name to greet (must be string)

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


# Variable annotations
age: int = 25
price: float = 19.99
is_active: bool = True
message: str = "Hello"

print(f"Greeting: {greet('Alice')}")


# === Collection Types ===
# Modern Python (3.9+) supports built-in generics
def process_names(names: list[str]) -> list[str]:
    """Process a list of names."""
    return [name.upper() for name in names]


def get_user_ages(users: dict[str, int]) -> list[int]:
    """Extract ages from user dictionary."""
    return list(users.values())


# Tuple with specific types
def get_coordinates() -> tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)


# Set type
def unique_words(text: str) -> set[str]:
    """Return unique words from text."""
    return set(text.lower().split())


# === Optional and Union ===
def find_user(user_id: int) -> dict | None:
    """
    Find user by ID.

    Optional[X] is equivalent to Union[X, None] - the value might be None.
    """
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)


def parse_value(value: str | int) -> str:
    """
    Parse a value that could be string or int.

    Union[X, Y] means the value can be either X or Y.
    Modern Python (3.10+) allows: str | int
    """
    return str(value)


# Python 3.10+ syntax
def parse_modern(value: str | int | None) -> str:
    """Using modern union syntax (3.10+)."""
    return str(value) if value is not None else "None"


# === Callable Types ===
def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """
    Apply an operation function to two numbers.

    Callable[[arg_types], return_type] specifies function signature.
    """
    return operation(x, y)


def add(a: int, b: int) -> int:
    return a + b


result = apply_operation(5, 3, add)
print(f"Apply operation: {result}")


# === Iterable and Iterator ===
def sum_values(values: Iterable[int]) -> int:
    """
    Sum any iterable of integers.

    Iterable is more flexible than list - accepts any iterable.
    """
    return sum(values)


print(f"Sum list: {sum_values([1, 2, 3])}")
print(f"Sum tuple: {sum_values((1, 2, 3))}")
print(f"Sum generator: {sum_values(x for x in range(4))}")


# === Any Type ===
def log_value(value: Any) -> None:
    """
    Log any value.

    Any disables type checking for this parameter.
    Use sparingly - defeats the purpose of type hints.
    """
    print(f"Value: {value}")


# === Type Aliases ===
# Create readable aliases for complex types
UserId = int
UserData = dict[str, str | int | bool]
UserList = list[UserData]


def get_users() -> UserList:
    """Return a list of user data."""
    return [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
    ]


# === Class Method Hints ===
class User:
    """Class with type hints."""

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "User":
        """Create User from dictionary. Note: return type is quoted (forward ref)."""
        return cls(data["name"], data["age"])


user = User("Alice", 30)
print(user.greet())


# === Expected Output ===
# Greeting: Hello, Alice!
# Apply operation: 8
# Sum list: 6
# Sum tuple: 6
# Sum generator: 6
# Hi, I'm Alice

# === Exercises ===
# 1. Run mypy on this file and fix any type errors
# 2. Create a generic function using TypeVar for a type-safe identity function
