from pipeline.stages.correlation import correlate

def test_correlation():
    data = {"input": "test"}
    result = correlate(data)
    assert "correlation" in result
