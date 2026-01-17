"""
Topic: Variable Arguments in Functions
Concepts: *args, **kwargs, variadic functions, argument unpacking
Learning objectives:
    - Use *args to accept any number of positional arguments
    - Use **kwargs to accept any number of keyword arguments
    - Understand how Python handles variable-length argument lists

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"


def var_sum(*args):
    """
    Sum any number of positional arguments.

    *args collects all positional arguments into a tuple.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        Sum of all provided arguments
    """
    answer = 0
    for i in args:
        answer += i
    return answer


def list_sum(number_list):
    """
    Sum all numbers in a list.

    Args:
        number_list: A list of numbers

    Returns:
        Sum of all numbers in the list
    """
    answer = 0
    for i in number_list:
        answer += i
    return answer


# Using *args - can pass any number of arguments
print(var_sum(1, 2, 3, 4, 5, 6))  # 21
print(var_sum())  # 0 - works with no arguments too

# Using a list requires passing an actual list
print(list_sum([1, 2, 3]))  # 6


def dic_sum(**kwargs):
    """
    Sum values from keyword arguments and display each key-value pair.

    **kwargs collects all keyword arguments into a dictionary.

    Args:
        **kwargs: Variable number of keyword arguments with numeric values

    Returns:
        Sum of all values
    """
    answer = 0
    for key, value in kwargs.items():
        # Display each key-value pair
        print("[" + str(key) + "]" + " = " + str(value))
        answer += value
    return answer


# Using **kwargs - can pass any named arguments
print(dic_sum(A=1, B=2, C=3))  # 6


# === Expected Output ===
# 21
# 0
# 6
# [A] = 1
# [B] = 2
# [C] = 3
# 6

# === Exercises ===
# 1. Create a function that accepts both *args and **kwargs and returns their combined sum
# 2. Modify var_sum to also accept a list using argument unpacking: var_sum(*my_list)
