"""
Topic: Descriptors in Python
Concepts: __get__, __set__, __delete__, descriptor protocol, lazy attributes
Learning objectives:
    - Understand the descriptor protocol
    - Implement custom attribute access behavior
    - Learn how properties are implemented using descriptors

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import datetime


class CurrentTime:
    """
    A descriptor that returns the current time whenever accessed.

    Descriptors are objects that define __get__, __set__, or __delete__.
    When accessed as a class attribute, Python calls these methods instead
    of returning the descriptor object itself.
    """

    def __get__(self, instance, owner):
        """
        Called when the attribute is accessed.

        Args:
            self: The descriptor instance
            instance: The instance accessing the attribute (None if class access)
            owner: The class that owns the descriptor

        Returns:
            The current datetime
        """
        print(f"Descriptor object: {self}")
        print(f"Instance accessing: {instance}")
        print(f"Owner class: {owner}")
        return datetime.datetime.now()


class Example:
    """Class using the CurrentTime descriptor."""

    # 'time' is a descriptor - accessing it calls CurrentTime.__get__
    time = CurrentTime()


# Accessing example.time calls CurrentTime.__get__()
print(Example().time)

# Each access returns a fresh timestamp
print("\n--- Multiple Accesses ---")
e = Example()
print(e.time)
print(e.time)  # Different time!


# === Expected Output ===
# Descriptor object: <__main__.CurrentTime object at 0x...>
# Instance accessing: <__main__.Example object at 0x...>
# Owner class: <class '__main__.Example'>
# 2024-01-15 10:30:45.123456
#
# --- Multiple Accesses ---
# Descriptor object: <__main__.CurrentTime object at 0x...>
# Instance accessing: <__main__.Example object at 0x...>
# Owner class: <class '__main__.Example'>
# 2024-01-15 10:30:45.234567
# ... (similar output with different time)

# === Exercises ===
# 1. Add __set__ to make this a data descriptor that stores a fixed time
# 2. Create a 'Cached' descriptor that computes a value once and caches it
