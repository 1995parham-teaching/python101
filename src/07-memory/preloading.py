"""
Topic: Partial Function Application
Concepts: functools.partial, argument preloading, higher-order functions
Learning objectives:
    - Use functools.partial to create specialized functions
    - Understand partial application vs currying
    - Pre-fill function arguments for convenience

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import functools


def main_function(arg1, arg2, arg3):
    """
    Function with three arguments for demonstration.

    Args:
        arg1: First argument
        arg2: Second argument
        arg3: Third argument
    """
    print("arg1 :", str(arg1))
    print("arg2 :", str(arg2))
    print("arg3 :", str(arg3))


# Create a partial function with arg3 pre-filled
# partial_function only needs arg1 and arg2 now
partial_function = functools.partial(main_function, arg3=10)

print("=== Using partial function ===")
partial_function(20, 30)  # arg1=20, arg2=30, arg3=10 (pre-filled)

# Can also pre-fill positional arguments
print("\n=== Partial with positional args ===")
partial_with_first = functools.partial(main_function, 100)  # arg1=100
partial_with_first(200, 300)  # arg1=100 (fixed), arg2=200, arg3=300

# Real-world example: creating specialized print functions
print("\n=== Real-world example ===")
print_error = functools.partial(print, "[ERROR]")
print_warning = functools.partial(print, "[WARNING]")

print_error("Something went wrong!")
print_warning("This might cause issues")


# === Expected Output ===
# === Using partial function ===
# arg1 : 20
# arg2 : 30
# arg3 : 10
#
# === Partial with positional args ===
# arg1 : 100
# arg2 : 200
# arg3 : 300
#
# === Real-world example ===
# [ERROR] Something went wrong!
# [WARNING] This might cause issues

# === Exercises ===
# 1. Create a partial function for int() that always uses base=16 (hex parsing)
# 2. Implement your own partial function without using functools
