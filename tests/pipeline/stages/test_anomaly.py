from pipeline.stages.anomaly import detect_anomalies

def test_detect_anomalies():
    data = {"input": "test"}
    result = detect_anomalies(data)
    assert "anomaly" in result
