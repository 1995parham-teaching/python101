# In The Name Of God
# ========================================
# [] File Name : streams.py
#
# [] Creation Date : 24-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import io

# Buffering:
# Pass 0 to switch buffering off (only allowed in binary mode),
# 1 to select line buffering (only usable in text mode),
# and an integer > 1 to indicate the size in bytes of a fixed-size chunk buffer.
# Encoding:
# encoding is the name of the encoding used to decode or encode the file.
# NewLine:
# newline controls how universal newlines mode works (it only applies to text mode).
# It can be None, '', '\n', '\r', and '\r\n'.

# Text IO
file = io.open("Hello.txt", "w")
if isinstance(file, io.TextIOBase):
    print("Text IO....")

# Binary IO
file = io.open("Hello.txt", "wb")
if isinstance(file, io.BufferedIOBase):
    print("Binary IO....")

# Raw IO
file = io.open("Hello.txt", "rb", buffering=0)
if isinstance(file, io.RawIOBase):
    print("Raw IO....")
