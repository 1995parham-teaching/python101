"""
Topic: Properties in Python
Concepts: @property decorator, getter/setter/deleter, computed attributes
Learning objectives:
    - Use @property to create read-only computed attributes
    - Define setters and deleters for controlled attribute access
    - Understand when to use properties vs regular attributes

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"


class Person:
    """Demonstrates Python properties for controlled attribute access."""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def name(self):
        """
        Getter - returns computed full name.
        Called when accessing person.name
        """
        return f"{self.last_name}, {self.first_name}"

    @name.setter
    def name(self, value):
        """
        Setter - called when assigning to person.name.
        Currently does nothing (read-only in practice).
        """
        pass  # Could parse "Last, First" and set both attributes

    @name.deleter
    def name(self):
        """
        Deleter - called when using 'del person.name'.
        Removes both name components.
        """
        del self.last_name
        del self.first_name


# Usage example
person = Person("Doe", "John")
print(person.name)  # Calls the getter

# Try to set (does nothing due to pass)
person.name = "Smith, Jane"
print(person.name)  # Still "Doe, John"

# Access underlying attributes directly
print(person.first_name)
print(person.last_name)


# === Expected Output ===
# Doe, John
# Doe, John
# John
# Doe

# === Exercises ===
# 1. Implement the setter to parse "Last, First" format and update both names
# 2. Add an 'age' property with validation that prevents negative values
