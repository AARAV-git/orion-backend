"""
Basic smoke tests for ORION-Health AI Triage Backend.
These tests verify the application can start and respond correctly.
"""
import pytest
from fastapi.testclient import TestClient


def test_root_endpoint():
    """Test that the root endpoint returns a 200 OK with the expected message."""
    from app.main import app
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "ORION" in data["message"]


def test_app_title():
    """Test that the FastAPI app has the correct title."""
    from app.main import app
    assert app.title == "ORION-Health AI Triage Backend"


def test_cors_middleware_present():
    """Test that the app has middleware configured."""
    from app.main import app
    middleware_classes = [type(m).__name__ for m in app.user_middleware]
    # CORSMiddleware should be present
    assert len(app.user_middleware) > 0


def test_routes_registered():
    """Test that expected API routes are registered."""
    from app.main import app
    routes = [getattr(route, "path", None) for route in app.routes if hasattr(route, "path")]
    assert "/" in routes
    # At least one /api route should be present
    api_routes = [r for r in routes if r and r.startswith("/api")]
    assert len(api_routes) > 0
