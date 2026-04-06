import pytest
from pipeline.stages.anomaly.anomaly_detector import detect_anomaly
from pipeline.stages.correlation.correlation_engine import correlate
from pipeline.stages.ai_gateway.ai_gateway import ai_gateway_stage
from pipeline.stages.tactical_ai.tactical_ai import tactical_ai_stage
from pipeline.stages.execution.execution_engine import execute_action

def test_anomaly_detector():
    result = detect_anomaly({"ip": "192.168.1.1"})
    assert "anomaly" in result

def test_correlation_engine():
    result = correlate({"anomaly": True})
    assert "correlation" in result

def test_ai_gateway_stage():
    result = ai_gateway_stage({"input": "test"})
    assert "sanitized" in result

def test_tactical_ai_stage():
    result = tactical_ai_stage({"input": "test"})
    assert "decision" in result

def test_execution_engine():
    result = execute_action({"action": "block"})
    assert result["status"] == "executed"
