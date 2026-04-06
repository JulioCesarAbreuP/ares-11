import pytest
from core.contracts import AnalysisResult
from domain.execution.orchestrator import ExecutionOrchestrator
from domain.ai_gateway.validator import AIGatewayMiddleware

class DummySignal:
    def __init__(self, data):
        self.source = "sensor1"
        self.data = data
    def dict(self):
        return {"source": self.source, "data": self.data}

@pytest.mark.parametrize("asset_id,should_fail", [("host1", False), ("fail", True)])
def test_pipeline_end_to_end(asset_id, should_fail):
    # Paso 1: Ingesta y validación DLP
    ai_gateway = AIGatewayMiddleware()
    signal = DummySignal(f"user: john.doe@example.com asset: {asset_id}")
    try:
        clean_signal = ai_gateway.validate(signal)
    except ValueError as e:
        assert "DLP" in str(e) or "Prompt" in str(e)
        return
    # Paso 2: Correlación simulada
    analysis = AnalysisResult(
        incident_id="INC123",
        timestamp="2026-04-06T12:00:00Z",
        affected_assets=[asset_id],
        threat_level="high",
        findings=[{"desc": "anomaly"}],
        recommended_actions=["isolate_asset", "notify_easm"]
    )
    # Paso 3: Ejecución con resiliencia
    orchestrator = ExecutionOrchestrator()
    if should_fail:
        with pytest.raises(Exception):
            orchestrator.execute(analysis)
    else:
        result = orchestrator.execute(analysis)
        assert "isolate" in str(result.actions) and "EASM" in str(result.actions)
