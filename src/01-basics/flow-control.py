"""
Topic: Flow Control in Python
Concepts: if/else statements, for loops, break statement, for-else construct
Learning objectives:
    - Understand conditional branching with if/else
    - Learn Python's unique for-else construct
    - Use break to exit loops early

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

# Get user input and convert to integer
number_input = input("please enter number: ")
number = int(number_input)

# Check if number is even or odd using modulo operator
if number % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")

# Prime number check using for-else construct
# The else block executes only if the loop completes without break
for i in range(2, number // 2):
    if number % i == 0:
        # Found a divisor, not prime - exit the loop
        break
else:
    # No divisor found - number is prime
    # This else belongs to the for loop, not the if statement
    print("your number is prime")


# === Expected Output (with input 7) ===
# please enter number: 7
# your number is odd
# your number is prime

# === Expected Output (with input 12) ===
# please enter number: 12
# your number is even

# === Exercises ===
# 1. Modify the program to also check if the number is negative, zero, or positive
# 2. Add a while loop that keeps asking for numbers until the user enters 0
