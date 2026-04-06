from infrastructure.api.notifier import notify_telegram
import pytest

def test_notify_telegram(monkeypatch):
    called = {}
    def fake_post(url, data, timeout):
        called["url"] = url
        return type("Resp", (), {"status_code": 200, "text": "ok"})()
    import requests
    monkeypatch.setattr(requests, "post", fake_post)
    req = type("Req", (), {"message": "msg", "bot_token": "token", "chat_id": "id"})
    result = notify_telegram(req)
    assert result.success
