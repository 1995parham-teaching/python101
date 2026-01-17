"""
Topic: Operator Overloading (Magic/Dunder Methods)
Concepts: __str__, __int__, __add__, __radd__, protocol methods
Learning objectives:
    - Understand Python's special/magic/dunder methods
    - Implement type conversion operators (__str__, __int__)
    - Implement arithmetic operators (__add__, __radd__)
    - Learn how Python resolves operator calls

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"


class Hello:
    """Demonstrates protocol methods (operator overloading) in Python."""

    def __init__(self):
        """Constructor - called when creating new instance."""
        print("Hello created")

    def __str__(self):
        """
        String representation - called by str() and print().
        Returns human-readable string.
        """
        return "Hello"

    def __int__(self):
        """
        Integer conversion - called by int().
        Returns integer representation of object.
        """
        return 110

    def __add__(self, other):
        """
        Addition operator - called for: self + other
        Here we simply return the other operand.
        """
        return other

    def __radd__(self, other):
        """
        Reflected addition - called for: other + self
        when other doesn't know how to add with self.
        """
        return other


if __name__ == "__main__":
    h = Hello()  # Prints "Hello created"

    # Type conversions
    print(str(h))  # Calls __str__ → "Hello"
    print(int(h))  # Calls __int__ → 110

    # Arithmetic operations
    print(h + 10)  # Calls h.__add__(10) → 10
    print(10 + h)  # Calls h.__radd__(10) → 10 (since int doesn't know Hello)


# === Expected Output ===
# Hello created
# Hello
# 110
# 10
# 10

# === Exercises ===
# 1. Add __repr__ method that returns "Hello()" for debugging
# 2. Implement __mul__ and __rmul__ for multiplication support
