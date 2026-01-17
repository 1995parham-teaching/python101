"""
Topic: Async Producer-Consumer Pattern
Concepts: asyncio.Queue, producer-consumer, task coordination
Learning objectives:
    - Use asyncio.Queue for async communication
    - Implement the producer-consumer pattern
    - Coordinate multiple async workers

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import asyncio
import random


async def producer(queue: asyncio.Queue, name: str, count: int):
    """
    Producer coroutine that adds items to the queue.

    Args:
        queue: Async queue to put items into
        name: Producer identifier
        count: Number of items to produce
    """
    for i in range(count):
        # Simulate work
        await asyncio.sleep(random.uniform(0.1, 0.5))
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"[{name}] Produced: {item}")
    print(f"[{name}] Finished producing")


async def consumer(queue: asyncio.Queue, name: str):
    """
    Consumer coroutine that processes items from the queue.

    Args:
        queue: Async queue to get items from
        name: Consumer identifier
    """
    while True:
        # Wait for an item from the queue
        item = await queue.get()

        # Simulate processing
        await asyncio.sleep(random.uniform(0.2, 0.4))
        print(f"  [{name}] Consumed: {item}")

        # Mark the task as done
        queue.task_done()


async def main():
    """
    Coordinate producers and consumers.
    """
    # Create a queue with max size (backpressure)
    queue = asyncio.Queue(maxsize=5)

    # Create producer tasks
    producers = [
        asyncio.create_task(producer(queue, "P1", 3)),
        asyncio.create_task(producer(queue, "P2", 3)),
    ]

    # Create consumer tasks
    consumers = [
        asyncio.create_task(consumer(queue, "C1")),
        asyncio.create_task(consumer(queue, "C2")),
    ]

    # Wait for all producers to finish
    await asyncio.gather(*producers)
    print("\nAll producers finished. Waiting for queue to drain...")

    # Wait for all items to be processed
    await queue.join()
    print("All items processed!")

    # Cancel consumers (they run forever)
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    asyncio.run(main())


# === Expected Output ===
# [P1] Produced: P1-item-0
# [P2] Produced: P2-item-0
#   [C1] Consumed: P1-item-0
# [P1] Produced: P1-item-1
#   [C2] Consumed: P2-item-0
# (... interleaved output ...)
#
# All producers finished. Waiting for queue to drain...
# All items processed!

# === Exercises ===
# 1. Add a poison pill pattern to gracefully stop consumers
# 2. Implement priority queue using asyncio.PriorityQueue
