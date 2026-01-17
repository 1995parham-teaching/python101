"""
Topic: Async/Await Basics
Concepts: async def, await, coroutines, asyncio.run(), asyncio.gather()
Learning objectives:
    - Understand the async/await syntax (Python 3.5+)
    - Write and run coroutines
    - Execute multiple coroutines concurrently with gather()

Author: Parham Alvani (parham.alvani@gmail.com)
"""
__author__ = "Parham Alvani"

import asyncio
import time


async def say_hello(name: str, delay: float) -> str:
    """
    A simple coroutine that waits and returns a greeting.

    The 'async def' creates a coroutine function.
    The 'await' keyword suspends execution until the awaited operation completes.
    """
    print(f"Starting hello for {name}...")
    await asyncio.sleep(delay)  # Non-blocking sleep
    message = f"Hello, {name}!"
    print(f"Completed hello for {name}")
    return message


async def main():
    """
    Main coroutine demonstrating different execution patterns.
    """
    print("=== Sequential Execution ===")
    start = time.perf_counter()

    # Sequential: one after another (slow)
    result1 = await say_hello("Alice", 1)
    result2 = await say_hello("Bob", 1)
    print(f"Results: {result1}, {result2}")
    print(f"Sequential took: {time.perf_counter() - start:.2f}s\n")

    print("=== Concurrent Execution ===")
    start = time.perf_counter()

    # Concurrent: both run at the same time (fast)
    results = await asyncio.gather(
        say_hello("Charlie", 1),
        say_hello("Diana", 1),
        say_hello("Eve", 1),
    )
    print(f"Results: {results}")
    print(f"Concurrent took: {time.perf_counter() - start:.2f}s")


# Run the main coroutine
# asyncio.run() creates an event loop, runs the coroutine, then closes the loop
if __name__ == "__main__":
    asyncio.run(main())


# === Expected Output ===
# === Sequential Execution ===
# Starting hello for Alice...
# Completed hello for Alice
# Starting hello for Bob...
# Completed hello for Bob
# Results: Hello, Alice!, Hello, Bob!
# Sequential took: 2.00s
#
# === Concurrent Execution ===
# Starting hello for Charlie...
# Starting hello for Diana...
# Starting hello for Eve...
# Completed hello for Charlie
# Completed hello for Diana
# Completed hello for Eve
# Results: ['Hello, Charlie!', 'Hello, Diana!', 'Hello, Eve!']
# Concurrent took: 1.00s

# === Exercises ===
# 1. Add error handling with try/except inside an async function
# 2. Use asyncio.create_task() instead of gather() and observe the difference
