"""
Topic: HTTP Requests with the requests Library
Concepts: GET, POST, JSON handling, response objects, error handling
Learning objectives:
    - Make HTTP requests using the requests library
    - Handle JSON responses
    - Use proper error handling for network operations

Note: Requires 'pip install requests' to run.

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

try:
    import requests

    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("requests not installed. Run: pip install requests")


def get_example():
    """Demonstrate GET request with query parameters."""
    print("=== GET Request ===")

    # Simple GET request
    response = requests.get("https://httpbin.org/get")
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers['Content-Type']}")

    # Parse JSON response
    data = response.json()
    print(f"Origin IP: {data['origin']}")

    # GET with query parameters
    params = {"name": "Python", "version": "3.12"}
    response = requests.get("https://httpbin.org/get", params=params)
    print(f"\nWith params: {response.url}")


def post_example():
    """Demonstrate POST request with JSON data."""
    print("\n=== POST Request ===")

    # POST with JSON body
    payload = {"username": "alice", "email": "alice@example.com"}

    response = requests.post("https://httpbin.org/post", json=payload)

    data = response.json()
    print(f"Sent JSON: {data['json']}")
    print(f"Content-Type sent: {data['headers']['Content-Type']}")


def error_handling():
    """Demonstrate proper error handling."""
    print("\n=== Error Handling ===")

    try:
        # Set timeout to avoid hanging
        response = requests.get("https://httpbin.org/status/404", timeout=5)

        # Raise exception for 4xx/5xx status codes
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")


def session_example():
    """Demonstrate using sessions for connection reuse."""
    print("\n=== Session Example ===")

    # Sessions reuse TCP connections (faster for multiple requests)
    with requests.Session() as session:
        # Set default headers for all requests
        session.headers.update({"User-Agent": "Python101/1.0"})

        # Make multiple requests using the same session
        session.get("https://httpbin.org/headers")
        response2 = session.get("https://httpbin.org/user-agent")

        print(f"User-Agent seen: {response2.json()['user-agent']}")


if __name__ == "__main__":
    if REQUESTS_AVAILABLE:
        get_example()
        post_example()
        error_handling()
        session_example()


# === Expected Output ===
# === GET Request ===
# Status Code: 200
# Content-Type: application/json
# Origin IP: x.x.x.x
#
# With params: https://httpbin.org/get?name=Python&version=3.12
#
# === POST Request ===
# Sent JSON: {'username': 'alice', 'email': 'alice@example.com'}
# Content-Type sent: application/json
#
# === Error Handling ===
# HTTP Error: 404 Client Error: NOT FOUND for url: ...
#
# === Session Example ===
# User-Agent seen: Python101/1.0

# === Exercises ===
# 1. Add authentication headers (Bearer token or Basic auth)
# 2. Download a file with progress reporting using iter_content()
