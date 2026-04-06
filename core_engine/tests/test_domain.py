import pytest
from core_engine.domain.models import TacticalInference, MitigationPriority

def test_tactical_inference_model():
    ti = TacticalInference(risk_score=0.9, vector_signature="SIG-1", mitigation_priority=MitigationPriority.HIGH)
    assert ti.risk_score == 0.9
    assert ti.vector_signature == "SIG-1"
    assert ti.mitigation_priority == MitigationPriority.HIGH
