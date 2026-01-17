"""
Topic: Introspection in Python
Concepts: __name__, __doc__, inspect module, runtime reflection
Learning objectives:
    - Access function/class metadata at runtime
    - Use the inspect module for detailed introspection
    - Understand docstrings and their accessibility

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import inspect


def example():
    """
    Example function demonstrating docstrings.

    This docstring can be accessed at runtime using
    the __doc__ attribute or inspect.getdoc().
    """
    pass


# Access function name
print(example.__name__)  # "example"

# Access raw docstring (includes indentation)
print(example.__doc__)

# Access cleaned docstring (removes indentation)
print(inspect.getdoc(example))

# Lambda functions have a generic name
print((lambda: None).__name__)  # "<lambda>"

# Additional introspection capabilities
print("\n--- More Introspection ---")
print("Module:", example.__module__)
print("Annotations:", example.__annotations__)
print("Is function:", inspect.isfunction(example))


# === Expected Output ===
# example
#
#     Example function demonstrating docstrings.
#
#     This docstring can be accessed at runtime using
#     the __doc__ attribute or inspect.getdoc().
#
# Example function demonstrating docstrings.
#
# This docstring can be accessed at runtime using
# the __doc__ attribute or inspect.getdoc().
# <lambda>
#
# --- More Introspection ---
# Module: __main__
# Annotations: {}
# Is function: True

# === Exercises ===
# 1. Use inspect.signature() to get the function's parameter information
# 2. Create a decorator that prints introspection info before calling a function
