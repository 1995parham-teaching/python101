"""
Topic: JSON Handling in Python
Concepts: json.loads, json.dumps, json.load, json.dump, custom encoders
Learning objectives:
    - Parse JSON strings and files
    - Serialize Python objects to JSON
    - Handle custom objects with JSON encoders

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime

# === Basic JSON Operations ===
print("=== JSON Parsing (loads) ===")

# Parse JSON string to Python dict
json_string = '{"name": "Alice", "age": 30, "active": true, "scores": [95, 87, 92]}'
data = json.loads(json_string)

print(f"Type: {type(data)}")
print(f"Name: {data['name']}")
print(f"Scores: {data['scores']}")


print("\n=== JSON Serialization (dumps) ===")

# Convert Python dict to JSON string
python_dict = {
    "product": "Widget",
    "price": 29.99,
    "in_stock": True,
    "tags": ["sale", "new"],
}

json_output = json.dumps(python_dict)
print(f"Compact: {json_output}")

# Pretty print with indentation
json_pretty = json.dumps(python_dict, indent=2)
print(f"Pretty:\n{json_pretty}")


# === Working with Files ===
print("\n=== JSON Files ===")

# Write to file
with open("data.json", "w") as f:
    json.dump(python_dict, f, indent=2)
print("Wrote data.json")

# Read from file
with open("data.json") as f:
    loaded = json.load(f)
print(f"Loaded: {loaded}")

# Cleanup
os.remove("data.json")


# === Custom Object Serialization ===
print("\n=== Custom Encoder ===")


@dataclass
class User:
    """User dataclass for JSON serialization example."""

    name: str
    email: str
    created_at: datetime


class CustomEncoder(json.JSONEncoder):
    """Custom encoder that handles datetime and dataclasses."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        return super().default(obj)


user = User(name="Bob", email="bob@example.com", created_at=datetime.now())

# Using custom encoder
user_json = json.dumps(user, cls=CustomEncoder, indent=2)
print(f"Custom serialized:\n{user_json}")


# === Handling Nested Data ===
print("\n=== Nested Data ===")

nested_data = """
{
    "users": [
        {"id": 1, "name": "Alice", "department": {"id": 10, "name": "Engineering"}},
        {"id": 2, "name": "Bob", "department": {"id": 20, "name": "Marketing"}}
    ]
}
"""

data = json.loads(nested_data)
for user in data["users"]:
    print(f"{user['name']} works in {user['department']['name']}")


# === Expected Output ===
# === JSON Parsing (loads) ===
# Type: <class 'dict'>
# Name: Alice
# Scores: [95, 87, 92]
#
# === JSON Serialization (dumps) ===
# Compact: {"product": "Widget", "price": 29.99, ...}
# Pretty:
# {
#   "product": "Widget",
#   ...
# }
#
# === JSON Files ===
# Wrote data.json
# Loaded: {...}
#
# === Custom Encoder ===
# Custom serialized:
# {
#   "name": "Bob",
#   "email": "bob@example.com",
#   "created_at": "2024-01-15T10:30:00"
# }
#
# === Nested Data ===
# Alice works in Engineering
# Bob works in Marketing

# === Exercises ===
# 1. Create a custom decoder (object_hook) to parse dates back to datetime
# 2. Handle JSON with single quotes (invalid JSON) using ast.literal_eval
