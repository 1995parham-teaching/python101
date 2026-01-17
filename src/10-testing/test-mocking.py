"""
Topic: Mocking in Tests
Concepts: unittest.mock, patch, MagicMock, side_effect
Learning objectives:
    - Use mocks to isolate units of code
    - Patch external dependencies
    - Verify mock calls and arguments

Note: Run with 'pytest test-mocking.py -v'

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

from unittest.mock import MagicMock, patch

import pytest


# === Code to Test ===
class UserService:
    """Service that interacts with an external API."""

    def __init__(self, api_client):
        self.api_client = api_client

    def get_user(self, user_id: int) -> dict:
        """Fetch user from API."""
        response = self.api_client.get(f"/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError(f"User {user_id} not found")

    def create_user(self, name: str, email: str) -> dict:
        """Create a new user via API."""
        response = self.api_client.post("/users", json={"name": name, "email": email})
        return response.json()


def fetch_data(url: str) -> str:
    """Function that makes HTTP request (we'll mock this)."""
    import requests

    response = requests.get(url)
    return response.text


def process_data(url: str) -> list:
    """Process data from URL - depends on fetch_data."""
    raw_data = fetch_data(url)
    return raw_data.split("\n")


# === Basic Mocking ===
def test_user_service_with_mock():
    """Test UserService with a mock API client."""
    # Create a mock API client
    mock_client = MagicMock()

    # Configure mock response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Alice"}

    # Set up the mock to return our response
    mock_client.get.return_value = mock_response

    # Test the service
    service = UserService(mock_client)
    user = service.get_user(1)

    # Verify the result
    assert user["name"] == "Alice"

    # Verify the mock was called correctly
    mock_client.get.assert_called_once_with("/users/1")


def test_user_service_not_found():
    """Test UserService when user is not found."""
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 404

    mock_client.get.return_value = mock_response

    service = UserService(mock_client)

    with pytest.raises(ValueError) as exc_info:
        service.get_user(999)

    assert "User 999 not found" in str(exc_info.value)


# === Using patch Decorator ===
@patch("__main__.fetch_data")
def test_process_data_with_patch(mock_fetch):
    """Test process_data by patching fetch_data."""
    # Configure what the mock returns
    mock_fetch.return_value = "line1\nline2\nline3"

    # Call the function
    result = process_data("http://example.com/data")

    # Verify result
    assert result == ["line1", "line2", "line3"]

    # Verify fetch_data was called with correct URL
    mock_fetch.assert_called_once_with("http://example.com/data")


# === Using side_effect for Multiple Calls ===
def test_multiple_api_calls():
    """Test handling multiple API calls with different responses."""
    mock_client = MagicMock()

    # side_effect allows returning different values for successive calls
    mock_client.get.side_effect = [
        MagicMock(status_code=200, json=lambda: {"id": 1, "name": "Alice"}),
        MagicMock(status_code=200, json=lambda: {"id": 2, "name": "Bob"}),
        MagicMock(status_code=404),
    ]

    service = UserService(mock_client)

    # First call returns Alice
    assert service.get_user(1)["name"] == "Alice"

    # Second call returns Bob
    assert service.get_user(2)["name"] == "Bob"

    # Third call raises exception
    with pytest.raises(ValueError):
        service.get_user(3)


# === Using side_effect for Exceptions ===
def test_api_error_handling():
    """Test handling API errors."""
    mock_client = MagicMock()

    # side_effect can also raise exceptions
    mock_client.get.side_effect = ConnectionError("Network error")

    service = UserService(mock_client)

    with pytest.raises(ConnectionError):
        service.get_user(1)


# === Verifying Call Arguments ===
def test_create_user_arguments():
    """Test that create_user sends correct data."""
    mock_client = MagicMock()
    mock_client.post.return_value = MagicMock(
        json=lambda: {"id": 1, "name": "Alice", "email": "alice@example.com"}
    )

    service = UserService(mock_client)
    service.create_user("Alice", "alice@example.com")

    # Verify call arguments
    mock_client.post.assert_called_once_with(
        "/users", json={"name": "Alice", "email": "alice@example.com"}
    )


if __name__ == "__main__":
    print("Run with: pytest test-mocking.py -v")


# === Expected Output (with pytest -v) ===
# test-mocking.py::test_user_service_with_mock PASSED
# test-mocking.py::test_user_service_not_found PASSED
# test-mocking.py::test_process_data_with_patch PASSED
# test-mocking.py::test_multiple_api_calls PASSED
# test-mocking.py::test_api_error_handling PASSED
# test-mocking.py::test_create_user_arguments PASSED

# === Exercises ===
# 1. Use patch.object() to mock a method on a class
# 2. Test a function that calls datetime.now() using freezegun or manual mocking
