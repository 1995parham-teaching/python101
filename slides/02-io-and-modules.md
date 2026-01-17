---
marp: true
theme: gaia
class: invert
paginate: true
header: "Python 101"
footer: "I/O, Iterators, and Modules"
style: |
  :root {
    --color-background: #1e1e2e;
    --color-foreground: #cdd6f4;
    --color-highlight: #ff6b35;
  }
  section {
    background-color: #1e1e2e;
  }
  h1, h2, h3, h4, h5, h6 {
    color: #ff6b35;
  }
  a {
    color: #fab387;
  }
  code {
    background-color: #313244;
  }
  blockquote {
    border-left-color: #ff6b35;
  }
---

# Python 101: I/O, Iterators, and Modules

**File Operations, Generators, and Code Organization**

---

# Input/Output

---

## Keyboard Input

```python
# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Converting input
age = int(input("Enter your age: "))
price = float(input("Enter price: "))

# Handling errors
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

---

## Opening Files

```python
# Basic file opening
file = open("example.txt", "r")  # Read mode
content = file.read()
file.close()

# Better: Using context manager
with open("example.txt", "r") as file:
    content = file.read()
# File automatically closed

# File modes:
# 'r' - Read (default)
# 'w' - Write (creates/overwrites)
# 'a' - Append
# 'rb'/'wb' - Binary mode
```

---

## Reading Files

```python
# Read entire file
with open("data.txt") as f:
    content = f.read()

# Read line by line
with open("data.txt") as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open("data.txt") as f:
    lines = f.readlines()

# Read specific number of bytes
with open("data.txt") as f:
    chunk = f.read(100)  # First 100 characters
```

---

## Writing Files

```python
# Write text
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Line 2\n")

# Write multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as f:
    f.writelines(line + "\n" for line in lines)

# Append to file
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

---

## File Positioning

```python
import io

with open("data.txt", "r") as f:
    # Read first 10 bytes
    print(f.read(10))

    # Get current position
    print(f.tell())

    # Go back to start
    f.seek(0, io.SEEK_SET)

    # Go to end
    f.seek(0, io.SEEK_END)

    # Relative position
    f.seek(-5, io.SEEK_CUR)
```

---

# Iterators & Generators

---

## The Iterator Protocol

```python
# iter() and next()
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator)  # StopIteration!

# For loops use iterators internally
for num in numbers:  # Calls iter(), then next()
    print(num)
```

---

## Creating Iterators

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1
```

---

## Generators (Simple Iterators)

```python
# Generator function (uses yield)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)

# Generator expression
squares = (x**2 for x in range(10))

# Generators are memory efficient
# Values computed on-demand, not stored
```

---

## Reading Large Files with Generators

```python
# BAD: Loads entire file into memory
def read_csv_bad(filename):
    with open(filename) as f:
        return f.read().split("\n")

# GOOD: Yields one line at a time
def read_csv_good(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Process millions of lines with minimal memory
for row in read_csv_good("huge_file.csv"):
    process(row)
```

---

## Generator Patterns

```python
# Infinite sequence
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

# Pipeline of generators
def numbers():
    for i in range(10):
        yield i

def squares(nums):
    for n in nums:
        yield n ** 2

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

# Chain them together
pipeline = evens(squares(numbers()))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

---

# Modules

---

## Creating Modules

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

```python
# main.py
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.PI)
print(mymodule.Calculator.add(2, 3))
```

---

## Import Styles

```python
# Import entire module
import math
print(math.sqrt(16))

# Import with alias
import numpy as np

# Import specific items
from math import sqrt, pi
print(sqrt(16))

# Import all (not recommended)
from math import *

# Relative imports (in packages)
from . import sibling_module
from ..parent import something
```

---

## Module Search Path

Python looks for modules in this order:

1. Current directory
2. `PYTHONPATH` environment variable
3. Standard library paths
4. Site-packages (installed packages)

```python
import sys
print(sys.path)  # List of search paths

# Add custom path
sys.path.append("/path/to/my/modules")
```

---

## Packages

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# Import from package
from mypackage import module1
from mypackage.subpackage import module3

# Package initialization
# __init__.py can expose package API
```

---

# Socket Programming

---

## TCP Server

```python
import socket

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(5)

print("Server listening on port 8080")

while True:
    client, address = server.accept()
    print(f"Connection from {address}")

    data = client.recv(1024)
    client.send(b"Hello from server!")
    client.close()
```

---

## TCP Client

```python
import socket

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

# Send and receive
client.send(b"Hello from client!")
response = client.recv(1024)
print(response.decode())

client.close()
```

---

# Multithreading

---

## Threading Basics

```python
import threading
import time

def worker(name, delay):
    print(f"{name} starting")
    time.sleep(delay)
    print(f"{name} finished")

# Create threads
t1 = threading.Thread(target=worker, args=("Thread-1", 2))
t2 = threading.Thread(target=worker, args=("Thread-2", 1))

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()
```

---

## Global Interpreter Lock (GIL)

> In CPython, only one thread can execute Python code at once.

**Use threading for:**
- I/O-bound tasks (network, file operations)

**Use multiprocessing for:**
- CPU-bound tasks (calculations)

```python
# For CPU-bound tasks
from multiprocessing import Pool

def compute(x):
    return x ** 2

with Pool(4) as p:
    results = p.map(compute, range(10))
```

---

# Practice Exercises

1. Write a file word counter using generators
2. Create a simple TCP chat server
3. Build a module with utility functions
4. Implement a producer-consumer pattern with threads

---

# Next: Async Programming

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "Data fetched!"

asyncio.run(fetch_data())
```

See `src/08-async/` for examples!
