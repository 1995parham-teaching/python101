"""
Topic: Classes and Inheritance in Python
Concepts: class definition, __init__, instance methods, static methods,
          inheritance, super(), method overriding
Learning objectives:
    - Define classes with constructors and instance methods
    - Understand the difference between static and instance methods
    - Implement inheritance and override methods
    - Use super() to call parent class methods

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"


class Contact:
    """A simple contact class demonstrating OOP basics."""

    def __init__(self, lname, fname, job):
        """
        Initialize a Contact with name and job information.

        Args:
            lname: Last name
            fname: First name
            job: Job title
        """
        self.lastName = lname
        self.firstName = fname
        self.job = job
        self.__private = 1  # Private attribute (name mangling)

    def get_name(self):
        """Return the full name of the contact."""
        return self.lastName + " " + self.firstName

    @staticmethod
    def static_method():
        """Static method - doesn't receive self, belongs to class."""
        return "Hello"

    def unbound_method():
        """Method without self - can only be called on class, not instance."""
        return "Bye"


# Create an instance and access its attributes
contact = Contact("Parham", "Alvani", "Nothing")
print(contact.firstName, contact.lastName)
print(contact.get_name())
print(contact.job)
print("==================")

# Inspect class and instance dictionaries
print(Contact.__dict__)  # Class attributes and methods
print(contact.__dict__)  # Instance attributes only
print("==================")
print("==================")

# Call static and unbound methods
print(contact.static_method())  # Can call on instance
print(Contact.unbound_method())  # Must call on class
print("==================")


class Student(Contact):
    """Student class inheriting from Contact, using super()."""

    def __init__(self, lname, fname):
        # Use super() to call parent's __init__ (preferred method)
        super().__init__(lname, fname, "Student")

    def get_name(self):
        """Override parent's get_name method."""
        return "New get_name() method"


student = Student("Alvani", "Parham")
print(student.get_name())  # Calls overridden method


class Worker(Contact):
    """Worker class using direct parent class call for __init__."""

    def __init__(self, lname, fname):
        # Alternative way to call parent's __init__ (less flexible)
        Contact.__init__(self, lname, fname, "Worker")


# === Expected Output ===
# Parham Alvani
# Parham Alvani
# Nothing
# ==================
# {...class dict...}
# {'lastName': 'Parham', 'firstName': 'Alvani', 'job': 'Nothing', '_Contact__private': 1}
# ==================
# ==================
# Hello
# Bye
# ==================
# New get_name() method

# === Exercises ===
# 1. Add a __str__ method to Contact that returns a formatted string representation
# 2. Create a Manager class that inherits from Worker and adds a department attribute
