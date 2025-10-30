import pytest
from app import app as flask_app  # Import your app

@pytest.fixture
def client():
    """Create a test client for the app."""
    with flask_app.test_client() as client:
        yield client

def test_homepage_loads(client):
    """Test if the homepage (/) loads successfully (HTTP 200)."""
    response = client.get('/')
    assert response.status_code == 200

def test_homepage_content(client):
    """Test if the homepage contains the expected content."""
    response = client.get('/')
    assert b"Popular Books" in response.data  # Check if title is there
    assert b"Genres & Tags" in response.data # Check if your new section is there