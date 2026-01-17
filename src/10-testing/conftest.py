"""
Topic: Pytest Configuration and Shared Fixtures
Concepts: conftest.py, shared fixtures, fixture scope, autouse
Learning objectives:
    - Understand conftest.py role in pytest
    - Share fixtures across multiple test files
    - Use different fixture scopes

Note: This file is automatically loaded by pytest.
      Fixtures defined here are available to all tests in this directory.

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import pytest


# === Shared Fixtures ===
@pytest.fixture
def sample_user():
    """
    Provide a sample user dictionary for tests.

    This fixture is available to all tests in this directory.
    """
    return {"id": 1, "name": "Test User", "email": "test@example.com", "active": True}


@pytest.fixture
def sample_users():
    """Provide a list of sample users."""
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    ]


# === Fixture Scopes ===
@pytest.fixture(scope="module")
def database_connection():
    """
    Fixture with module scope - created once per test module.

    Useful for expensive setup like database connections.
    """
    print("\n[Setup] Creating database connection")
    connection = {"host": "localhost", "port": 5432, "connected": True}
    yield connection
    print("\n[Teardown] Closing database connection")
    connection["connected"] = False


@pytest.fixture(scope="session")
def app_config():
    """
    Fixture with session scope - created once for the entire test session.

    Useful for global configuration that doesn't change.
    """
    return {
        "debug": True,
        "testing": True,
        "database_url": "sqlite:///:memory:",
    }


# === Autouse Fixtures ===
@pytest.fixture(autouse=True)
def reset_environment():
    """
    Fixture that runs automatically for every test.

    autouse=True means tests don't need to request this fixture.
    """
    # Setup: runs before each test
    yield
    # Teardown: runs after each test (cleanup)


# === Parametrized Fixtures ===
@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database_type(request):
    """
    Parametrized fixture - test runs once for each parameter.

    request.param contains the current parameter value.
    """
    return request.param


# === Example test using these fixtures ===
def test_sample_user_fixture(sample_user):
    """Test that sample_user fixture works."""
    assert sample_user["name"] == "Test User"
    assert sample_user["active"] is True


def test_sample_users_count(sample_users):
    """Test that sample_users fixture provides multiple users."""
    assert len(sample_users) == 3


def test_database_types(database_type):
    """Test runs 3 times - once for each database type."""
    assert database_type in ["sqlite", "postgres", "mysql"]


# === Exercises ===
# 1. Create a fixture that provides a temporary directory (use tmp_path)
# 2. Create a fixture that mocks environment variables
