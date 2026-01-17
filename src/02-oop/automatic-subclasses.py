"""
Topic: Dynamic Subclass Selection with __new__
Concepts: __new__ method, __subclasses__(), factory pattern, metaclass-like behavior
Learning objectives:
    - Understand the difference between __new__ and __init__
    - Use __subclasses__() to discover child classes
    - Implement dynamic object creation based on runtime conditions

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import random


class Example:
    """
    Base class that randomly creates one of its subclasses.

    When you call Example(), it actually returns a Spam or Eggs instance!
    This demonstrates the factory pattern using __new__.
    """

    def __new__(cls, *args, **kwargs):
        """
        Called before __init__ to create the instance.

        __new__ is responsible for creating and returning the instance.
        Here we override it to return a random subclass instance instead.
        """
        # Get list of direct subclasses and pick one randomly
        cls = random.choice(cls.__subclasses__())
        # Create instance of the chosen subclass
        return super().__new__(cls, *args, **kwargs)


class Spam(Example):
    """First subclass of Example."""

    pass


class Eggs(Example):
    """Second subclass of Example."""

    pass


# Each call to Example() randomly creates either Spam or Eggs
print(Example())  # Might print: <__main__.Spam object at 0x...>
print(Example())  # Might print: <__main__.Eggs object at 0x...>

# Demonstrate __subclasses__()
print("\n--- Subclass Discovery ---")
print("Example subclasses:", Example.__subclasses__())


# === Expected Output (varies due to randomness) ===
# <__main__.Spam object at 0x...>
# <__main__.Eggs object at 0x...>
#
# --- Subclass Discovery ---
# Example subclasses: [<class '__main__.Spam'>, <class '__main__.Eggs'>]

# === Exercises ===
# 1. Modify to accept a 'type' argument that specifies which subclass to create
# 2. Add a registry pattern where subclasses register themselves with a name
