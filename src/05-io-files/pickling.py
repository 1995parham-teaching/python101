"""
Topic: Object Serialization with Pickle
Concepts: pickle.dumps, pickle.loads, serialization, object persistence
Learning objectives:
    - Serialize Python objects to bytes using pickle
    - Deserialize bytes back to Python objects
    - Understand use cases and security considerations

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import pickle


class IntoBinary:
    """
    Sample class demonstrating pickling.

    Pickle can serialize most Python objects including custom classes.
    """

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "My number is " + str(self.number)


if __name__ == "__main__":
    # Create an instance
    my_object = IntoBinary(10)
    print("Original object:", my_object)

    # Serialize to bytes (dumps = dump string/bytes)
    pickled = pickle.dumps(my_object)
    print("Pickled bytes:", pickled)

    # Deserialize back to object (loads = load string/bytes)
    restored_object = pickle.loads(pickled)
    print("Restored object:", restored_object)

    # Verify it's a new object with same data
    print("\n--- Verification ---")
    print("Same object?", my_object is restored_object)  # False
    print("Same value?", my_object.number == restored_object.number)  # True

    # Saving to a file (dump/load without 's')
    print("\n--- File Pickling ---")
    with open("data.pkl", "wb") as f:
        pickle.dump(my_object, f)

    with open("data.pkl", "rb") as f:
        loaded = pickle.load(f)
    print("Loaded from file:", loaded)

    # Cleanup
    import os

    os.remove("data.pkl")


# === Expected Output ===
# Original object: My number is 10
# Pickled bytes: b'\x80\x04\x95...'
# Restored object: My number is 10
#
# --- Verification ---
# Same object? False
# Same value? True
#
# --- File Pickling ---
# Loaded from file: My number is 10

# === Exercises ===
# 1. Try pickling a class with __slots__ - what happens?
# 2. Implement __reduce__ to customize how your class is pickled
