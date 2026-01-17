"""
Topic: Method Resolution Order (MRO)
Concepts: multiple inheritance, C3 linearization, __mro__, diamond problem
Learning objectives:
    - Understand how Python resolves method calls in inheritance hierarchies
    - Learn the C3 linearization algorithm
    - Use __mro__ to inspect the method resolution order

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"


class Book:
    """Base class for all book types."""

    def __init__(self, title):
        self.title = title
        self.page = 1

    def read(self):
        """Default reading behavior."""
        return f"There sure are a lot of words on page {self.page}"

    def bookmark(self, page):
        """Save current page."""
        self.page = page


class Novel(Book):
    """Novel inherits from Book without overriding methods."""

    pass


class Mystery(Novel):
    """Mystery novel with custom read behavior."""

    def read(self):
        """Override read() for mystery-specific message."""
        return f"Page {self.page} and I still don't know who did it!"


class New(Mystery, Book):
    """
    Demonstrates multiple inheritance and MRO.

    Even though Book is listed as a parent, Mystery's read() is used
    because of the Method Resolution Order (C3 linearization).
    """

    pass


# Create instance and demonstrate MRO
book = New("The Little Prince")

# __mro__ shows the order Python searches for methods
# New → Mystery → Novel → Book → object
print("MRO:", New.__mro__)

# read() is found in Mystery (second in MRO after New)
print(book.read())

# Visual representation of the class hierarchy:
#        Book
#         |
#       Novel
#         |
#      Mystery
#        / \
#       New Book  (Book appears twice in inheritance, but MRO handles this)


# === Expected Output ===
# MRO: (<class '__main__.New'>, <class '__main__.Mystery'>, <class '__main__.Novel'>, <class '__main__.Book'>, <class 'object'>)
# Page 1 and I still don't know who did it!

# === Exercises ===
# 1. Add a 'Thriller' class and create a class that inherits from both Mystery and Thriller
# 2. Override bookmark() in Mystery and call super() to see how MRO affects it
