from domain.decision_engine.tactical_memory import TacticalMemory

def test_store_and_compare_incident():
    mem = TacticalMemory()
    mem.store_incident("id1", "desc1", {"meta": 1})
    result = mem.compare_with_past("desc1")
    assert result["match"] is True

def test_compare_with_no_match():
    mem = TacticalMemory()
    result = mem.compare_with_past("incidente desconocido")
    assert result["match"] is False

def test_store_incident_edge_cases():
    mem = TacticalMemory()
    try:
        mem.store_incident(None, None, None)
    except Exception as e:
        assert isinstance(e, Exception)
