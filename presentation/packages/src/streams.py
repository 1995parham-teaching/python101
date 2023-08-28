import io

# Buffering:
# Pass 0 to switch buffering off (only allowed in binary mode),
# 1 to select line buffering (only usable in text mode),
# and an integer > 1 to indicate the size in bytes of a fixed-size chunk buffer.
#
# Encoding:
# encoding is the name of the encoding used to decode or encode the file.
#
# NewLine:
# newline controls how universal newlines mode works (it only applies to text mode).
# It can be None, '', '\n', '\r', and '\r\n'.

if __name__ == "__main__":
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
