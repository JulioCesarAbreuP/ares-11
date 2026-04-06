import pytest
from core.contracts import SignalIngest
from pipeline.stages.ai_gateway.gateway import ai_gateway_stage

class DummySignal(SignalIngest):
    pass

def test_ai_gateway_pass(monkeypatch):
    signal = DummySignal(source="sensor1", data="normal data")
    result = ai_gateway_stage(signal)
    assert result.data == "normal data"

def test_ai_gateway_dlp_block(monkeypatch):
    signal = DummySignal(source="sensor1", data="123-45-6789")  # SSN pattern
    with pytest.raises(ValueError) as e:
        ai_gateway_stage(signal)
    assert "DLP" in str(e.value)

def test_ai_gateway_prompt_injection(monkeypatch):
    signal = DummySignal(source="sensor1", data="system: {malicious}")
    with pytest.raises(ValueError) as e:
        ai_gateway_stage(signal)
    assert "Prompt" in str(e.value)

def test_ai_gateway_circuit_breaker(monkeypatch):
    # Forzar 3 fallos seguidos para abrir el breaker
    signal = DummySignal(source="sensor1", data="123-45-6789")
    for _ in range(3):
        with pytest.raises(ValueError):
            ai_gateway_stage(signal)
    # Ahora el breaker debe estar abierto
    with pytest.raises(RuntimeError):
        ai_gateway_stage(signal)
