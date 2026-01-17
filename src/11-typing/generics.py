"""
Topic: Generic Types and TypeVar
Concepts: TypeVar, Generic, bounded types, covariance
Learning objectives:
    - Create generic functions with TypeVar
    - Build generic classes
    - Understand type bounds and variance

Note: Run mypy for static type checking: mypy generics.py

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

from collections.abc import Sequence
from typing import Generic, SupportsFloat, TypeVar

# === TypeVar for Generic Functions ===
# T can be any type - determined by usage
T = TypeVar("T")


def first(items: Sequence[T]) -> T:
    """
    Return the first item from a sequence.

    T is a type variable - the return type matches the input element type.
    first([1,2,3]) returns int, first(["a","b"]) returns str.
    """
    return items[0]


# Type is inferred based on argument
num: int = first([1, 2, 3])  # T is int
text: str = first(["a", "b"])  # T is str
print(f"First number: {num}, First text: {text}")


def identity(value: T) -> T:
    """Return the same value - type is preserved."""
    return value


# === Multiple Type Variables ===
K = TypeVar("K")
V = TypeVar("V")


def swap(pair: tuple[K, V]) -> tuple[V, K]:
    """Swap elements in a pair, preserving types."""
    return (pair[1], pair[0])


result = swap(("hello", 42))  # Returns tuple[int, str]
print(f"Swapped: {result}")


# === Bounded TypeVar ===
# Restrict T to specific types
Number = TypeVar("Number", int, float)


def double(value: Number) -> Number:
    """
    Double a number.

    Number is constrained to int or float only.
    """
    return value * 2


print(f"Double 5: {double(5)}")
print(f"Double 3.14: {double(3.14)}")


# === Upper Bound TypeVar ===
Numeric = TypeVar("Numeric", bound=SupportsFloat)


def to_float(value: Numeric) -> float:
    """
    Convert to float.

    Numeric must support __float__ (be a subtype of SupportsFloat).
    """
    return float(value)


# === Generic Classes ===
ContentType = TypeVar("ContentType")


class Box(Generic[ContentType]):
    """
    A generic container class.

    Box[int] holds integers, Box[str] holds strings, etc.
    """

    def __init__(self, content: ContentType) -> None:
        self._content = content

    def get(self) -> ContentType:
        """Get the box content."""
        return self._content

    def set(self, content: ContentType) -> None:
        """Set new content."""
        self._content = content


# Type is specified when creating instance
int_box: Box[int] = Box(42)
str_box: Box[str] = Box("hello")

print(f"Int box: {int_box.get()}")
print(f"Str box: {str_box.get()}")


# === Generic Class with Multiple Type Parameters ===
class Pair(Generic[K, V]):
    """A generic pair/tuple class."""

    def __init__(self, first: K, second: V) -> None:
        self.first = first
        self.second = second

    def swap(self) -> "Pair[V, K]":
        """Return a new pair with swapped elements."""
        return Pair(self.second, self.first)


pair: Pair[str, int] = Pair("age", 25)
swapped: Pair[int, str] = pair.swap()
print(f"Original: ({pair.first}, {pair.second})")
print(f"Swapped: ({swapped.first}, {swapped.second})")


# === Generic Stack Example ===
class Stack(Generic[T]):
    """A type-safe stack implementation."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Push item onto stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Pop item from stack."""
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0


# Usage
stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
print(f"Popped: {stack.pop()}")  # 2


# === Expected Output ===
# First number: 1, First text: a
# Swapped: (42, 'hello')
# Double 5: 10
# Double 3.14: 6.28
# Int box: 42
# Str box: hello
# Original: (age, 25)
# Swapped: (25, age)
# Popped: 2

# === Exercises ===
# 1. Create a generic Queue class with enqueue/dequeue methods
# 2. Implement a generic cache (dict-like) with type-safe get/set
