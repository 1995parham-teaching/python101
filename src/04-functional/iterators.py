"""
Topic: Iterators and the Iterator Protocol
Concepts: __iter__, __next__, StopIteration, generators, iterable vs iterator
Learning objectives:
    - Implement the iterator protocol manually
    - Understand the difference between iterables and iterators
    - Use generators as a simpler alternative to iterator classes
    - Implement __reversed__ for reverse iteration

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"


class YRange:
    """
    Iterator that generates numbers from 0 to n-1.

    Problem: This class is BOTH iterable AND iterator.
    Once exhausted, it cannot be reused!
    """

    def __init__(self, n):
        self.i = 0  # Current position (state)
        self.n = n  # Upper bound

    def __iter__(self):
        """Return self as the iterator."""
        return self

    def __next__(self):
        """Return next value or raise StopIteration."""
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


# Demonstrate the problem with combined iterable/iterator
y = YRange(3)
print("First iteration:", list(y))  # [0, 1, 2]
print("Second iteration:", list(y))  # [] - exhausted!


class ZRange:
    """
    Iterable that creates fresh iterators.

    This separates the iterable (ZRange) from the iterator (ZRangeIter).
    Each iteration creates a new iterator, so it's reusable!
    """

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        """Return a NEW iterator each time."""
        return ZRangeIter(self.n)


class ZRangeIter:
    """Iterator for ZRange - holds the iteration state."""

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        """Iterators should also be iterable (return self)."""
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


# Demonstrate reusability
z = ZRange(5)
print("\nZRange first iteration:", list(z))  # [0, 1, 2, 3, 4]
print("ZRange second iteration:", list(z))  # [0, 1, 2, 3, 4] - works again!


class Range:
    """
    Modern approach using generators.

    Generators automatically implement the iterator protocol!
    This is the cleanest and most Pythonic solution.
    """

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        """Generator function - yields values one at a time."""
        yield from range(self.max)

    def __len__(self):
        """Support len() function."""
        return self.max

    def __reversed__(self):
        """Support reversed() function."""
        yield from range(self.max - 1, -1, -1)


print("\nGenerator-based Range:", list(Range(4)))
print("Reversed Range:", list(reversed(Range(4))))


# === Expected Output ===
# First iteration: [0, 1, 2]
# Second iteration: []
#
# ZRange first iteration: [0, 1, 2, 3, 4]
# ZRange second iteration: [0, 1, 2, 3, 4]
#
# Generator-based Range: [0, 1, 2, 3, 4]
# Reversed Range: [3, 2, 1, 0]

# === Exercises ===
# 1. Add a 'step' parameter to Range for custom increments (like range(0, 10, 2))
# 2. Create an infinite iterator class that generates Fibonacci numbers
