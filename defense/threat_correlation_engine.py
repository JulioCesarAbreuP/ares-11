# defense/threat_correlation_engine.py
"""
Threat Correlation Engine: Correlaciona eventos de red, identidad y memoria táctica.
Eleva el riesgo si detecta patrones coordinados o persistentes.
"""
import json
from brain.tactical_memory import TacticalMemory

def correlate_threats(event, identity_events=None):
    """
    event: dict con datos de red (banner, ip, hostname, device, etc)
    identity_events: lista de dicts con eventos de identidad recientes
    """
    signals = {
        "threat_correlated": False,
        "multi_hop_risk": False,
        "correlation_details": None
    }
    memory = TacticalMemory()
    # 1. Correlación con memoria táctica
    match = memory.compare_with_past(json.dumps(event))
    if match["match"]:
        signals["threat_correlated"] = True
        signals["correlation_details"] = match
    # 2. Correlación con identidad (simulado)
    if identity_events:
        for idev in identity_events:
            if idev.get("src_ip") == event.get("ip") or idev.get("user") == event.get("user"):
                signals["multi_hop_risk"] = True
                signals["correlation_details"] = {"identity_link": idev}
    return signals
