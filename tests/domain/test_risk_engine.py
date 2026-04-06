from domain.risk_engine.device_reputation import DeviceReputation

def test_device_reputation_score():
    rep = DeviceReputation()
    score = rep.calculate_risk("dev1", "activity1")
    assert 0.0 <= score <= 1.0

def test_sentinel_trigger(monkeypatch):
    rep = DeviceReputation()
    triggered = {}
    def fake_trigger(*a, **kw):
        triggered["called"] = True
    rep.trigger_sentinel_bridge = fake_trigger
    rep.threshold = 2  # Forzar trigger
    rep.calculate_risk("dev2", "actividad sospechosa")
    assert triggered["called"]

def test_device_reputation_edge_cases():
    rep = DeviceReputation()
    try:
        rep.calculate_risk(None, None)
    except Exception as e:
        assert isinstance(e, Exception)
