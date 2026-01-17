"""
Topic: Class vs Instance Attributes
Concepts: class attributes, instance attributes, attribute shadowing
Learning objectives:
    - Understand the difference between class and instance attributes
    - Learn how Python looks up attributes (instance → class → parent classes)
    - Recognize attribute shadowing behavior

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"


class Fields:
    """Demonstrates class vs instance attributes."""

    # Class attribute - shared by all instances (until shadowed)
    static_field = 0

    def __init__(self):
        # Instance attribute - unique to each instance
        self.non_static_field = 0


# Modify the class attribute directly
Fields.static_field = 10

# Create first instance
f1 = Fields()

# This creates an INSTANCE attribute that shadows the class attribute
f1.static_field = 20
print("f1.static_field: " + str(f1.static_field))  # 20 (instance attr)

f1.non_static_field = 10
print("f1.non_static_field: " + str(f1.non_static_field))  # 10

# Create second instance
f2 = Fields()

# f2 doesn't have instance attribute, so it reads class attribute
print("f2.static_field: " + str(f2.static_field))  # 10 (class attr)
print("f2.non_static_field: " + str(f2.non_static_field))  # 0

# Verify attribute locations
print("\n--- Attribute Inspection ---")
print("Fields.static_field:", Fields.static_field)  # 10
print("f1.__dict__:", f1.__dict__)  # Has 'static_field': 20
print("f2.__dict__:", f2.__dict__)  # No 'static_field'


# === Expected Output ===
# f1.static_field: 20
# f1.non_static_field: 10
# f2.static_field: 10
# f2.non_static_field: 0
#
# --- Attribute Inspection ---
# Fields.static_field: 10
# f1.__dict__: {'non_static_field': 10, 'static_field': 20}
# f2.__dict__: {'non_static_field': 0}

# === Exercises ===
# 1. Add a class method that modifies static_field for ALL instances
# 2. Create a counter that tracks how many instances have been created
