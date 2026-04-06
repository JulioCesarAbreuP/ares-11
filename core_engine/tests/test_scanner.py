import pytest
import asyncio
from core_engine.adapters.advanced_scanner import AdvancedScanner

@pytest.mark.asyncio
async def test_scanner_ports(monkeypatch):
    scanner = AdvancedScanner(ports=[65535])
    async def fake_scan_port(port):
        return {"port": port, "banner": "test-banner"}
    monkeypatch.setattr(scanner, "_grab_banner", lambda r, w: "banner")
    result = await scanner.scan("127.0.0.1")
    assert isinstance(result, list)
    assert result[0]["port"] == 65535
