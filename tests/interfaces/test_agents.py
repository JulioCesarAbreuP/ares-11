from interfaces.agents.anomaly_agent import handle_ingest
from interfaces.agents.correlation_agent import handle_anomaly
from interfaces.agents.external_surface_agent import handle_external_surface

def test_handle_ingest():
    result = handle_ingest({"data": "test"})
    assert result is None or isinstance(result, dict)

def test_handle_anomaly():
    result = handle_anomaly({"data": "test"})
    assert result is None or isinstance(result, dict)

def test_handle_external_surface():
    result = handle_external_surface("8.8.8.8")
    assert result is None or isinstance(result, dict)
