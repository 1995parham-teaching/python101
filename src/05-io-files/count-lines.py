"""
Topic: File Operations and Exception Handling
Concepts: file I/O, try/except/else/finally, logging, command-line arguments
Learning objectives:
    - Read files using open() with proper error handling
    - Understand the complete try/except/else/finally structure
    - Use the logging module for error reporting
    - Access command-line arguments via sys.argv

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import logging
import os
import sys
import time


def count_lines(filename):
    """
    Count the number of lines in a file.

    Demonstrates comprehensive exception handling with try/except/else/finally.

    Args:
        filename: Path to the file to count

    Returns:
        Number of lines in the file, or 0 if file cannot be read
    """
    input_file = None
    try:
        # Attempt to open and read the file
        input_file = open(filename)
        lines = input_file.readlines()
    except TypeError as exp:
        # Invalid filename type (e.g., None)
        logging.error(exp)
        return 0
    except OSError as exp:
        # File not found or permission denied
        logging.error(exp)
        return 0
    except UnicodeDecodeError as exp:
        # Binary file or encoding issues
        logging.error(exp)
        return 0
    else:
        # Only runs if no exception occurred
        return len(lines)
    finally:
        # Always runs - cleanup
        if input_file:
            input_file.close()


def count_words(filename):
    """
    Count the number of words in a file.

    Uses 'with' statement for automatic file closing (context manager).

    Args:
        filename: Path to the file

    Returns:
        Total word count
    """
    with open(filename) as input_file:
        words = 0
        lines = input_file.readlines()
        for line in lines:
            words += len(line.split(" "))
        return words


# Process files passed as command-line arguments
if __name__ == "__main__":
    i = 1
    while i < len(sys.argv):
        filepath = sys.argv[i]
        print(f"File: {os.path.abspath(filepath)}")
        print(f"Created: {time.ctime(os.path.getctime(filepath))}")
        print(f"Lines: {count_lines(filepath)}")
        print(f"Words: {count_words(filepath)}")
        print()
        i += 1


# === Expected Output (with this file as argument) ===
# File: /path/to/count-lines.py
# Created: Mon Jan 15 10:30:00 2024
# Lines: 85
# Words: 350

# === Exercises ===
# 1. Add a count_characters function that counts non-whitespace characters
# 2. Modify to accept a directory and process all .py files recursively
