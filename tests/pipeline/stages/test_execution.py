from pipeline.stages.execution import execute_action

def test_execution():
    data = {"input": "test"}
    result = execute_action(data)
    assert "executed" in result
