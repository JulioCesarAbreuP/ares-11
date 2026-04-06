import pytest
from fastapi.testclient import TestClient
from core_engine.api.api import app

def test_ws_connect():
    client = TestClient(app)
    with client.websocket_connect("/ws/tactical-feed") as ws:
        ws.send_text("ping")
