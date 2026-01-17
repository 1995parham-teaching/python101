"""
Topic: Memory Management and Garbage Collection
Concepts: id(), reference counting, del statement, gc module, __del__
Learning objectives:
    - Understand Python's reference-based memory model
    - Use id() to inspect object identity
    - Learn about the garbage collector and __del__ finalizer
    - Understand object aliasing and reference sharing

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import gc

# === Object Identity ===
# id() returns the memory address of an object
x_int = 10
print("id(10):", id(x_int))

# Reassigning creates a new object
x_str = "foo"
print("id('foo'):", id(x_str))

# None is a singleton - same id everywhere
x_none = None
print("id(None):", id(x_none))

# === Reference Sharing (Aliasing) ===
# Lists are mutable - assignment creates alias, not copy
a = [1, 2, 3]
b = a  # b points to the SAME list as a
b.append(4)

print("\n--- Aliasing ---")
print("a:", a)  # [1, 2, 3, 4] - a is also modified!
print("b:", b)  # [1, 2, 3, 4]
print("a is b:", a is b)  # True - same object

# del removes the reference, not the object (if other refs exist)
del a
print("After del a, b:", b)  # b still works


# === Garbage Collection and __del__ ===
class DelMe:
    """Demonstrates the __del__ finalizer (destructor)."""

    def __del__(self):
        """Called when the object is about to be garbage collected."""
        print("I am being deleted!")


print("\n--- Garbage Collection ---")
obj_a = DelMe()
del obj_a  # Remove the only reference
gc.collect()  # Force garbage collection
print("After deleting object a")

obj_b: DelMe | None = DelMe()
obj_b = None  # Setting to None also removes reference
print("After setting b to None")

# Force collection to see the __del__ call
gc.collect()


# === Expected Output ===
# id(10): 4376543216
# id('foo'): 4377123456
# id(None): 4374567890
#
# --- Aliasing ---
# a: [1, 2, 3, 4]
# b: [1, 2, 3, 4]
# a is b: True
# After del a, b: [1, 2, 3, 4]
#
# --- Garbage Collection ---
# I am being deleted!
# After deleting object a
# After setting b to None
# I am being deleted!

# === Exercises ===
# 1. Create a circular reference and observe when it gets collected
# 2. Use gc.get_referrers() to find what objects reference a given object
