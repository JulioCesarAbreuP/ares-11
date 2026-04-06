# pipeline/stages/correlation/threat_correlation_engine.py
"""
Threat Correlation Engine: Correlaciona eventos de red, identidad y memoria táctica.
Formalizado para arquitectura enterprise.
"""
import json
from domain.decision_engine.tactical_memory import TacticalMemory
from core.contracts import CorrelationOutput
from core.events import EventBus

def correlate_threats(event: dict, identity_events: list = None) -> CorrelationOutput:
    details = {}
    threat_correlated = False
    multi_hop_risk = False
    memory = TacticalMemory()
    match = memory.compare_with_past(json.dumps(event))
    if match["match"]:
        threat_correlated = True
        details["memory_match"] = match
    if identity_events:
        for idev in identity_events:
            if idev.get("src_ip") == event.get("ip") or idev.get("user") == event.get("user"):
                multi_hop_risk = True
                details["identity_link"] = idev
    EventBus().publish("correlation.completed", details)
    return CorrelationOutput(correlation_id="corr-001", risk_level="high" if threat_correlated or multi_hop_risk else "low", related_events=identity_events or [], details=details)
