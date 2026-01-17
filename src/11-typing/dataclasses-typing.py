"""
Topic: Dataclasses with Type Hints
Concepts: @dataclass, field(), frozen, default_factory, post_init
Learning objectives:
    - Create type-annotated dataclasses
    - Use field options for default values and factories
    - Understand frozen (immutable) dataclasses

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

from dataclasses import asdict, astuple, dataclass, field
from datetime import datetime
from typing import ClassVar


# === Basic Dataclass ===
@dataclass
class Point:
    """
    A simple 2D point.

    Dataclasses automatically generate:
    - __init__()
    - __repr__()
    - __eq__()
    """

    x: float
    y: float


p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(f"Point: {p1}")  # Point(x=1.0, y=2.0)
print(f"Equal: {p1 == p2}")  # True (compares by value)


# === Default Values ===
@dataclass
class User:
    """User with default values."""

    name: str
    email: str
    age: int = 0  # Default value
    active: bool = True


user = User("Alice", "alice@example.com")
print(f"User: {user}")


# === Default Factory for Mutable Defaults ===
@dataclass
class Team:
    """
    Team with a list of members.

    Use field(default_factory=list) for mutable defaults.
    Never use [] as default - it would be shared between instances!
    """

    name: str
    members: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)


team1 = Team("Engineering")
team1.members.append("Alice")

team2 = Team("Marketing")
print(f"Team1 members: {team1.members}")  # ['Alice']
print(f"Team2 members: {team2.members}")  # [] (not shared!)


# === Field Options ===
@dataclass
class Product:
    """Product with various field options."""

    name: str
    price: float
    # Not included in __init__, but included in __repr__
    id: int = field(init=False, default=0)
    # Excluded from __repr__
    internal_code: str = field(default="", repr=False)
    # Excluded from comparison
    description: str = field(default="", compare=False)


product = Product("Widget", 29.99)
print(f"Product: {product}")


# === Frozen (Immutable) Dataclass ===
@dataclass(frozen=True)
class Config:
    """
    Immutable configuration.

    frozen=True makes all fields read-only after creation.
    Attempting to modify raises FrozenInstanceError.
    """

    host: str
    port: int
    debug: bool = False


config = Config("localhost", 8080)
print(f"Config: {config}")

# This would raise FrozenInstanceError:
# config.port = 9090


# === Post-init Processing ===
@dataclass
class Rectangle:
    """Rectangle with computed area."""

    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self) -> None:
        """Called after __init__ to compute derived values."""
        self.area = self.width * self.height


rect = Rectangle(10, 20)
print(f"Rectangle area: {rect.area}")  # 200


# === Class Variables ===
@dataclass
class Counter:
    """Dataclass with class variable."""

    name: str
    # ClassVar marks class-level variables (not instance variables)
    total_count: ClassVar[int] = 0

    def __post_init__(self) -> None:
        Counter.total_count += 1


c1 = Counter("first")
c2 = Counter("second")
print(f"Total counters: {Counter.total_count}")  # 2


# === Conversion Utilities ===
@dataclass
class Person:
    """Person for conversion examples."""

    name: str
    age: int


person = Person("Bob", 30)

# Convert to dictionary
person_dict = asdict(person)
print(f"As dict: {person_dict}")

# Convert to tuple
person_tuple = astuple(person)
print(f"As tuple: {person_tuple}")


# === Inheritance ===
@dataclass
class Employee(Person):
    """Employee extends Person."""

    department: str
    salary: float = 0.0


emp = Employee("Charlie", 35, "Engineering", 75000.0)
print(f"Employee: {emp}")


# === Expected Output ===
# Point: Point(x=1.0, y=2.0)
# Equal: True
# User: User(name='Alice', email='alice@example.com', age=0, active=True)
# Team1 members: ['Alice']
# Team2 members: []
# Product: Product(name='Widget', price=29.99, id=0)
# Config: Config(host='localhost', port=8080, debug=False)
# Rectangle area: 200.0
# Total counters: 2
# As dict: {'name': 'Bob', 'age': 30}
# As tuple: ('Bob', 30)
# Employee: Employee(name='Charlie', age=35, department='Engineering', salary=75000.0)

# === Exercises ===
# 1. Create a dataclass that validates field values in __post_init__
# 2. Implement a dataclass with slots=True for memory efficiency
