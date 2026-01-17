"""
Topic: Memoization with Decorators
Concepts: decorators, caching, functools.wraps, closure
Learning objectives:
    - Implement a memoization decorator from scratch
    - Understand how closures capture state
    - Use functools.wraps to preserve function metadata

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import functools


def memoize(func):
    """
    Decorator that caches function results.

    When the decorated function is called with the same arguments,
    the cached result is returned instead of recomputing.

    Args:
        func: Function to decorate

    Returns:
        Wrapped function with caching behavior
    """
    # Cache is stored in the closure - persists between calls
    cache = {}

    @functools.wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args):
        if args in cache:
            # Cache hit - return stored result
            return cache[args]
        # Cache miss - compute and store
        print(f"Calling {func.__name__}()")  # For demonstration
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


if __name__ == "__main__":

    @memoize
    def multiply(x, y):
        """Multiply two numbers (demonstrating memoization)."""
        return x * y

    # First call - computes and caches
    print(multiply(2, 7))  # Prints "Calling multiply()" then 14

    # Second call with same args - uses cache
    print(multiply(2, 7))  # Just prints 14 (no "Calling...")

    # Different args - computes and caches
    print(multiply(2, 2))  # Prints "Calling multiply()" then 4

    # Verify function metadata is preserved
    print("\n--- Function Metadata ---")
    print("Name:", multiply.__name__)  # "multiply" (not "wrapper")
    print("Doc:", multiply.__doc__)

    # Real-world example: Fibonacci with memoization
    @memoize
    def fib(n):
        """Calculate nth Fibonacci number."""
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print("\n--- Fibonacci ---")
    print("fib(10):", fib(10))  # Only computes each value once!


# === Expected Output ===
# Calling multiply()
# 14
# 14
# Calling multiply()
# 4
#
# --- Function Metadata ---
# Name: multiply
# Doc: Multiply two numbers (demonstrating memoization).
#
# --- Fibonacci ---
# Calling fib()
# (multiple calls as it computes)
# fib(10): 55

# === Exercises ===
# 1. Add cache size limit - evict oldest entries when full (LRU cache)
# 2. Support keyword arguments in addition to positional arguments
