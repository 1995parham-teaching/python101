"""
Topic: Integer Operations and Representations
Concepts: binary representation, hexadecimal, byte conversion, endianness
Learning objectives:
    - Convert integers to different number bases (binary, hex)
    - Understand byte representation of integers
    - Learn about big-endian vs little-endian byte ordering

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

A = 10

# Convert to binary string representation
print(bin(A))  # 0b1010 (prefix 0b indicates binary)

# Convert to hexadecimal string representation
print(hex(A))  # 0xa (prefix 0x indicates hex)

# Convert to bytes with different byte orderings
# Little-endian: least significant byte first (used by x86 processors)
print(A.to_bytes(2, byteorder="little"))  # b'\n\x00' (10 is ASCII newline)

# Big-endian: most significant byte first (network byte order)
print(A.to_bytes(2, byteorder="big"))  # b'\x00\n'


# === Expected Output ===
# 0b1010
# 0xa
# b'\n\x00'
# b'\x00\n'

# === Exercises ===
# 1. Convert the bytes back to an integer using int.from_bytes()
# 2. Write a function that displays a number in binary, octal, decimal, and hex
