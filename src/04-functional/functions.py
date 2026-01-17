"""
Topic: Functions and Bytecode Inspection
Concepts: isinstance, hasattr, duck typing, dis module, bytecode
Learning objectives:
    - Compare type checking vs duck typing approaches
    - Inspect function bytecode using the dis module
    - Understand function metadata attributes

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import dis


def square(x):
    """
    Calculate the square using strict type checking (isinstance).

    This approach is LBYL (Look Before You Leap) - check type first.
    """
    if not isinstance(x, int):
        print(f"Error: x is a {type(x)} instead of int.")
    else:
        return x * x


def square2(x):
    """
    Calculate the square using duck typing (hasattr).

    This approach checks if the object supports multiplication,
    regardless of its actual type. More Pythonic!
    """
    if not hasattr(x, "__mul__"):
        print("Error: your object does not support multiplication")
    else:
        return x * x


# Test both approaches
print(square(10))  # Works with int
print(square2(10.1))  # Works with float (duck typing wins!)
print(square.__module__)  # Shows which module the function belongs to

# === Bytecode Inspection ===
# Python compiles functions to bytecode - let's examine it!
print("\n--- Bytecode Inspection ---")

# Raw bytecode bytes
print("Bytecode:", square.__code__.co_code)

# Variable names used in the function
print("Variables:", square.__code__.co_varnames)

# Number of arguments
print("Arg count:", square.__code__.co_argcount)

# Constants used in the function
print("Constants:", square.__code__.co_consts)

# Human-readable disassembly
print("\n--- Disassembly ---")
dis.dis(square.__code__)


# === Expected Output ===
# 100
# 102.01
# __main__
#
# --- Bytecode Inspection ---
# Bytecode: b'...'
# Variables: ('x',)
# Arg count: 1
# Constants: (None, 'Error: x is a %s instead of int.')
#
# --- Disassembly ---
#  (bytecode instructions...)

# === Exercises ===
# 1. Compare bytecode of square vs square2 - which is more efficient?
# 2. Use dis.dis() on a lambda function and compare to a regular function
