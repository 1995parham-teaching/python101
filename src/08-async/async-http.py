"""
Topic: Async HTTP Requests with aiohttp
Concepts: aiohttp, async context managers, concurrent HTTP requests
Learning objectives:
    - Make async HTTP requests with aiohttp
    - Use async context managers (async with)
    - Fetch multiple URLs concurrently

Note: Requires 'pip install aiohttp' to run.

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import asyncio

# Note: aiohttp must be installed: pip install aiohttp
try:
    import aiohttp

    AIOHTTP_AVAILABLE = True
except ImportError:
    AIOHTTP_AVAILABLE = False
    print("aiohttp not installed. Run: pip install aiohttp")


async def fetch_url(session: "aiohttp.ClientSession", url: str) -> dict:
    """
    Fetch a single URL asynchronously.

    Args:
        session: aiohttp client session (reuse for connection pooling)
        url: URL to fetch

    Returns:
        Dictionary with URL, status code, and content length
    """
    async with session.get(url) as response:
        content = await response.text()
        return {
            "url": url,
            "status": response.status,
            "length": len(content),
        }


async def fetch_all(urls: list[str]) -> list[dict | BaseException]:
    """
    Fetch multiple URLs concurrently.

    Uses a single session for all requests (better performance).
    """
    async with aiohttp.ClientSession() as session:
        # Create tasks for all URLs
        tasks = [fetch_url(session, url) for url in urls]
        # Wait for all tasks to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results


async def main():
    """Demonstrate concurrent HTTP fetching."""
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/ip",
        "https://httpbin.org/user-agent",
        "https://httpbin.org/headers",
    ]

    print(f"Fetching {len(urls)} URLs concurrently...\n")

    import time

    start = time.perf_counter()
    results = await fetch_all(urls)
    elapsed = time.perf_counter() - start

    for result in results:
        if isinstance(result, Exception):
            print(f"Error: {result}")
        else:
            print(f"URL: {result['url']}")
            print(f"  Status: {result['status']}")
            print(f"  Length: {result['length']} bytes\n")

    print(f"Fetched {len(urls)} URLs in {elapsed:.2f}s")


if __name__ == "__main__":
    if AIOHTTP_AVAILABLE:
        asyncio.run(main())


# === Expected Output ===
# Fetching 4 URLs concurrently...
#
# URL: https://httpbin.org/get
#   Status: 200
#   Length: 350 bytes
#
# URL: https://httpbin.org/ip
#   Status: 200
#   Length: 50 bytes
#
# (... more URLs ...)
#
# Fetched 4 URLs in 0.45s

# === Exercises ===
# 1. Add timeout handling using asyncio.wait_for()
# 2. Implement rate limiting to avoid overwhelming servers
