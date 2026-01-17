"""
Topic: Line-by-Line File Reading
Concepts: readline(), while loops for file iteration, line counting
Learning objectives:
    - Read files one line at a time using readline()
    - Understand the sentinel pattern (empty string signals EOF)
    - Compare different file reading approaches

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

# Get filename from user
filename = input("Please enter your filename: ")

# Open file in read mode
fo = open(filename)

counter = 0
while True:
    # readline() returns empty string at end of file
    line = fo.readline()
    if not line:
        # Empty string is falsy - signals end of file
        break
    counter += 1
    print(line, end="")  # Line already has newline, prevent double spacing

print(f"\nTotal lines: {counter}")

# Don't forget to close the file!
fo.close()


# === Expected Output (with a 3-line file) ===
# Please enter your filename: sample.txt
# Line 1 content
# Line 2 content
# Line 3 content
# Total lines: 3

# === Exercises ===
# 1. Rewrite using a 'with' statement to automatically close the file
# 2. Modify to use 'for line in file:' syntax instead of while/readline
