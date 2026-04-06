from pipeline.stages.tactical_ai import tactical_decision

def test_tactical_ai():
    data = {"input": "test"}
    result = tactical_decision(data)
    assert "decision" in result
