---
marp: true
theme: default
paginate: true
header: "Python 101"
footer: "Async Programming & Popular Libraries"
---

# Python 101: Week 3

**Async Programming & Popular Libraries**

---

# Async Programming

---

## Why Async?

**Problem with synchronous code:**
```python
# Each request waits for the previous one
fetch_url("url1")  # 1 second
fetch_url("url2")  # 1 second
fetch_url("url3")  # 1 second
# Total: 3 seconds
```

**With async:**
```python
# All requests run concurrently
await asyncio.gather(
    fetch_url("url1"),
    fetch_url("url2"),
    fetch_url("url3"),
)
# Total: ~1 second
```

---

## async/await Basics

```python
import asyncio

# Define a coroutine with 'async def'
async def say_hello(name, delay):
    await asyncio.sleep(delay)  # Non-blocking sleep
    return f"Hello, {name}!"

# Run a coroutine
async def main():
    result = await say_hello("Alice", 1)
    print(result)

# Entry point
asyncio.run(main())
```

---

## Concurrent Execution

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    # Run multiple coroutines concurrently
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
    )
    print(results)

asyncio.run(main())
# Takes ~1 second instead of 3!
```

---

## Creating Tasks

```python
import asyncio

async def worker(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} finished")

async def main():
    # Create tasks - they start immediately
    task1 = asyncio.create_task(worker("Task 1"))
    task2 = asyncio.create_task(worker("Task 2"))

    # Do other work...

    # Wait for tasks to complete
    await task1
    await task2

asyncio.run(main())
```

---

## Async Queues

```python
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(f"item-{i}")
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Processing: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    # Start producer and consumer
    prod = asyncio.create_task(producer(queue))
    cons = asyncio.create_task(consumer(queue))

    await prod
    await queue.join()  # Wait for all items
    cons.cancel()
```

---

# Popular Libraries

---

## requests - HTTP Made Easy

```python
import requests

# GET request
response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())       # Parse JSON

# POST with data
response = requests.post(
    "https://httpbin.org/post",
    json={"name": "Alice", "age": 30}
)

# With headers and timeout
response = requests.get(
    "https://api.example.com",
    headers={"Authorization": "Bearer token"},
    timeout=5
)
```

---

## aiohttp - Async HTTP

```python
import aiohttp
import asyncio

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        return await asyncio.gather(*tasks)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

urls = ["url1", "url2", "url3"]
results = asyncio.run(fetch_all(urls))
```

---

## json - Data Serialization

```python
import json

# Parse JSON string
data = json.loads('{"name": "Alice", "age": 30}')

# Convert to JSON string
json_str = json.dumps({"name": "Bob"}, indent=2)

# Read from file
with open("data.json") as f:
    data = json.load(f)

# Write to file
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## pathlib - Modern Path Handling

```python
from pathlib import Path

# Create paths
home = Path.home()
project = Path.cwd() / "myproject"

# Path operations
path = Path("data/file.txt")
print(path.name)      # file.txt
print(path.stem)      # file
print(path.suffix)    # .txt
print(path.parent)    # data

# File operations
path.read_text()
path.write_text("content")

# Find files
for py_file in Path(".").rglob("*.py"):
    print(py_file)
```

---

## datetime - Date and Time

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
utc = datetime.utcnow()

# Create specific datetime
dt = datetime(2024, 1, 15, 10, 30)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# Parsing
parsed = datetime.strptime("2024-01-15", "%Y-%m-%d")

# Arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
```

---

## dataclasses - Easy Data Classes

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    email: str
    age: int = 0
    tags: List[str] = field(default_factory=list)

# Auto-generates __init__, __repr__, __eq__
user = User("Alice", "alice@example.com", 30)
print(user)  # User(name='Alice', email='...', ...)

# Frozen (immutable)
@dataclass(frozen=True)
class Config:
    host: str
    port: int
```

---

## collections - Data Structures

```python
from collections import Counter, defaultdict, deque

# Counter - count occurrences
words = ["apple", "banana", "apple", "cherry"]
counter = Counter(words)
print(counter.most_common(2))  # [('apple', 2), ...]

# defaultdict - dict with default values
graph = defaultdict(list)
graph["a"].append("b")

# deque - efficient double-ended queue
queue = deque(maxlen=3)
queue.append(1)
queue.appendleft(0)
```

---

## itertools - Iterator Utilities

```python
from itertools import chain, groupby, combinations

# Chain iterables
combined = chain([1, 2], [3, 4], [5])
# [1, 2, 3, 4, 5]

# Group by key
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# Combinations
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```

---

## logging - Professional Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Log messages
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# With exception info
try:
    raise ValueError("Oops!")
except Exception:
    logger.exception("An error occurred")
```

---

# Virtual Environments

---

## Why Virtual Environments?

- Isolate project dependencies
- Avoid version conflicts
- Reproducible environments

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install packages
pip install requests

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

---

# Practice Exercises

1. Fetch multiple URLs concurrently with aiohttp
2. Build a JSON configuration loader with pathlib
3. Create a logging decorator for functions
4. Implement an async producer-consumer pattern

---

# Next: Testing & Best Practices

See `src/09-libraries/` for examples!
