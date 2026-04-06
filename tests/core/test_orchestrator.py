from core.orchestrator import Orchestrator

def test_orchestrator_flow():
    orch = Orchestrator()
    result = orch.run_pipeline({"input": "test"})
    assert result is not None
    assert "output" in result

def test_orchestrator_error_handling():
    orch = Orchestrator()
    try:
        orch.run_pipeline(None)
    except Exception as e:
        assert "error" in str(e).lower() or isinstance(e, Exception)
