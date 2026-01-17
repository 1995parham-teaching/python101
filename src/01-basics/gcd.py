"""
Topic: Greatest Common Divisor (GCD)
Concepts: recursion, Euclidean algorithm, mathematical functions
Learning objectives:
    - Implement the Euclidean algorithm recursively
    - Understand recursive function calls
    - Learn about mathematical algorithms in Python

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.

    The algorithm is based on the principle that GCD(a, b) = GCD(b, a % b)
    and GCD(a, 0) = a.

    Args:
        a: First positive integer
        b: Second positive integer

    Returns:
        The greatest common divisor of a and b
    """
    # Base case: if b divides a evenly, b is the GCD
    if a % b == 0:
        return b
    else:
        # Recursive case: GCD(a, b) = GCD(b, a mod b)
        return gcd(b, a % b)


print(gcd(10, 3))  # GCD of 10 and 3
print(gcd(48, 18))  # GCD of 48 and 18
print(gcd(100, 25))  # GCD of 100 and 25


# === Expected Output ===
# 1
# 6
# 25

# === Exercises ===
# 1. Convert this recursive function to an iterative version using a while loop
# 2. Implement LCM (Least Common Multiple) using the GCD function: LCM(a,b) = (a*b) / GCD(a,b)
