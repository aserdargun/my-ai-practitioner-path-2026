"""Tests for API routes."""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    """Test health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_predict_success():
    """Test successful prediction."""
    response = client.post(
        "/api/predict",
        json={"text": "Hello world test"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["result"] == 3  # 3 words


def test_predict_empty_text():
    """Test prediction with empty text."""
    response = client.post(
        "/api/predict",
        json={"text": ""}
    )
    assert response.status_code == 400


def test_list_items():
    """Test listing items."""
    response = client.get("/api/items")
    assert response.status_code == 200
    assert "items" in response.json()


def test_get_item():
    """Test getting a specific item."""
    response = client.get("/api/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
