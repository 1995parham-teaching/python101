"""
Topic: Metaclasses in Python
Concepts: type, metaclass, class creation, __init__ in metaclass
Learning objectives:
    - Understand that classes are instances of metaclasses
    - Learn how to create custom metaclasses
    - See how metaclasses intercept class creation

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"


class SimpleMetaClass(type):
    """
    A simple metaclass that prints information when a class is created.

    Metaclasses are the 'classes of classes'. When Python creates a class,
    it uses a metaclass (default is 'type') to construct it.
    """

    def __init__(cls, name, bases, attrs):
        """
        Called when a new class using this metaclass is defined.

        Args:
            cls: The newly created class (not instance!)
            name: Name of the class being created
            bases: Tuple of base classes
            attrs: Dictionary of class attributes and methods
        """
        print(f"Creating class: {name}")
        print(f"Class object: {cls}")
        super().__init__(name, bases, attrs)


# This class uses SimpleMetaClass as its metaclass
# When Python reads this definition, it calls SimpleMetaClass.__init__
class Example(metaclass=SimpleMetaClass):
    """Example class created with our custom metaclass."""

    pass


# Subclasses also use the same metaclass
class SubExample(Example):
    """Subclass inherits the metaclass."""

    pass


# === Expected Output ===
# Creating class: Example
# Class object: <class '__main__.Example'>
# Creating class: SubExample
# Class object: <class '__main__.SubExample'>

# === Exercises ===
# 1. Add a __new__ method to the metaclass that modifies class attributes
# 2. Create a metaclass that automatically adds a 'created_at' timestamp to classes
