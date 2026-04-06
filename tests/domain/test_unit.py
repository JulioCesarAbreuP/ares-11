import pytest
from domain.decision_engine.tactical_memory import TacticalMemory
from domain.risk_engine.device_reputation import DeviceReputation

def test_tactical_memory_store_and_compare():
    mem = TacticalMemory()
    mem.store_incident("id1", "desc", {"meta": 1})
    result = mem.compare_with_past("desc")
    assert result["match"]

def test_device_reputation_risk():
    rep = DeviceReputation()
    score = rep.calculate_risk("dev1", "activity")
    assert 0 <= score <= 1
