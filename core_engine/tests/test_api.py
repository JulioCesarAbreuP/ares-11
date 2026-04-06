import pytest
from fastapi.testclient import TestClient
from core_engine.api.api import app

def test_health():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_scan():
    client = TestClient(app)
    r = client.post("/scan", json={"target": "127.0.0.1"})
    assert r.status_code == 200
    assert "inference" in r.json()
