---
marp: true
theme: default
paginate: true
header: "Python 101"
footer: "Introduction to Python"
---

# Python 101: Introduction

**A Practical Guide to Python Programming**

---

## What is Python?

> Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable.

- Easy to learn and read
- Interpreted (no compilation needed)
- Object-oriented
- Large standard library

---

## Python Environment

```python
$ python3
Python 3.12.0 (main, Oct  2 2023)
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
```

---

## Variable Types

Python has several built-in data types:

- **Numbers** - `int`, `float`, `complex`
- **String** - `str`
- **List** - `list` (mutable sequence)
- **Tuple** - `tuple` (immutable sequence)
- **Dictionary** - `dict` (key-value pairs)

---

## Numbers

```python
# Integer
age = 25

# Float
price = 19.99

# Complex
z = 3 + 4j

# Operations
print(10 / 3)    # 3.333...
print(10 // 3)   # 3 (floor division)
print(10 % 3)    # 1 (modulo)
print(2 ** 10)   # 1024 (power)
```

---

## Strings

```python
# Creating strings
name = "Python"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# String operations
print(name.upper())        # PYTHON
print(name.lower())        # python
print(len(name))           # 6
print(name[0])             # P
print(name[-1])            # n
print(name[0:3])           # Pyt
```

---

## Lists

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])     # apple
print(fruits[-1])    # cherry

# Modifying lists
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")

# List slicing
print(fruits[1:3])
```

---

## Tuples

```python
# Tuples are immutable sequences
coordinates = (10, 20)
rgb = (255, 128, 0)

# Accessing elements
x, y = coordinates  # Unpacking
print(x)  # 10

# Tuples can't be modified
# coordinates[0] = 5  # Error!

# Use cases: function returns, dict keys
```

---

## Dictionaries

```python
# Key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "Tehran"
}

# Accessing values
print(person["name"])         # Alice
print(person.get("email", "N/A"))  # N/A

# Modifying
person["email"] = "alice@example.com"
del person["city"]
```

---

# Flow Control

---

## If/Else Statements

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

## Comparison Chaining

Python allows elegant comparison chaining:

```python
x = 5

# Instead of:
if x > 0 and x < 10:
    print("Valid")

# Use:
if 0 < x < 10:
    print("Valid")

# More examples:
print(1 < x < 10)        # True
print(5 == x > 4)        # True
```

---

## For Loops

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range function
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# For-else construct
for i in range(2, 10):
    if 10 % i == 0:
        break
else:
    print("10 is prime")  # Won't print
```

---

## While Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1

# With break and continue
while True:
    response = input("Enter 'q' to quit: ")
    if response == 'q':
        break
    print(f"You entered: {response}")
```

---

# Functions

---

## Defining Functions

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def square(x):
    return x * x

# Calling functions
print(greet("Alice"))  # Hello, Alice!
print(square(5))       # 25
```

---

## Function Arguments

```python
# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9
print(power(2, 10))  # 1024

# Variable arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# Keyword arguments
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

---

## Lambda Functions

```python
# Anonymous functions
square = lambda x: x * x
print(square(5))  # 25

# With built-in functions
numbers = [1, 2, 3, 4, 5]

# Map
squared = list(map(lambda x: x**2, numbers))

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Sort with key
names = ["Bob", "Alice", "Charlie"]
names.sort(key=lambda x: len(x))
```

---

# Classes

---

## Defining Classes

```python
class Person:
    """A simple Person class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

    def __str__(self):
        return f"Person({self.name}, {self.age})"

# Usage
person = Person("Alice", 30)
print(person.greet())
```

---

## Special Methods (Dunder Methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

---

## Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!
```

---

## Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# MRO: D -> B -> C -> A -> object
print(D.__mro__)
print(D().method())  # B
```

---

# Memory Management

---

## Garbage Collection

```python
import gc

# Python uses reference counting
a = [1, 2, 3]
b = a  # b references same list

# del removes reference, not object
del a
print(b)  # [1, 2, 3] - still exists

# Garbage collector handles cycles
class Node:
    def __init__(self):
        self.ref = None

n1 = Node()
n2 = Node()
n1.ref = n2
n2.ref = n1  # Circular reference

del n1, n2
gc.collect()  # Clean up cycles
```

---

## Data Hiding

```python
class Counter:
    def __init__(self):
        self.__count = 0  # Private attribute

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count

c = Counter()
c.increment()
# c.__count  # AttributeError!
# But accessible via name mangling:
print(c._Counter__count)  # 1
```

---

# Practice Exercises

1. Write a function that checks if a string is a palindrome
2. Create a `BankAccount` class with deposit/withdraw methods
3. Implement a simple calculator using operator overloading
4. Write a program that finds prime numbers up to N

---

# Next Steps

- **Week 2**: File I/O, Iterators, Modules
- **Week 3**: Libraries, Async Programming
- **Week 4**: Testing, Best Practices

See examples in `src/` directory!
