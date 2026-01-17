"""
Topic: User Input and Exception Handling
Concepts: input() function, try/except/else blocks, string formatting
Learning objectives:
    - Read input from users using input()
    - Handle errors gracefully with try/except
    - Understand the else clause in exception handling

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

# Simple string input
name = input("Please enter your name: ")
print(f"Hello {name}")  # Old-style string formatting

# Input with type conversion and error handling
number = input("Please enter number: ")
try:
    # Attempt to convert string to integer
    number = int(number)
except ValueError:
    # This block runs if conversion fails
    print(f"{number} is not number")
else:
    # This block runs only if try block succeeds (no exception)
    print(f"Your number is {number}")


# === Expected Output (with inputs "Alice" and "42") ===
# Please enter your name: Alice
# Hello Alice
# Please enter number: 42
# Your number is 42

# === Expected Output (with inputs "Bob" and "hello") ===
# Please enter your name: Bob
# Hello Bob
# Please enter number: hello
# hello is not number

# === Exercises ===
# 1. Add a finally block that prints "Input processing complete"
# 2. Modify to accept floating-point numbers and handle both int and float
