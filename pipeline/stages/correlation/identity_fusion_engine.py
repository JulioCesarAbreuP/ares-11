# pipeline/stages/correlation/identity_fusion_engine.py
"""
Identity Fusion Engine: Correlaciona eventos de red, identidad y permisos para detectar riesgos de movimiento lateral y abuso de privilegios.
Formalizado para arquitectura enterprise.
"""
from domain.decision_engine.tactical_memory import TacticalMemory
from core.contracts import CorrelationOutput
from core.events import EventBus

def identity_fusion(event: dict, identity_context: list = None) -> CorrelationOutput:
    details = {}
    identity_fusion_risk = False
    if identity_context:
        for idev in identity_context:
            if (
                idev.get("src_ip") == event.get("ip") or
                idev.get("user") == event.get("user") or
                set(idev.get("roles", [])) & set(event.get("roles", []))
            ):
                identity_fusion_risk = True
                details["identity_link"] = idev
                details["risk_reason"] = "Correlación de red e identidad con privilegios elevados"
    memory = TacticalMemory()
    match = memory.compare_with_past(str(event))
    if match["match"]:
        identity_fusion_risk = True
        details["memory_link"] = match
    EventBus().publish("identity_fusion.completed", details)
    return CorrelationOutput(
        correlation_id="fusion-001",
        risk_level="high" if identity_fusion_risk else "low",
        related_events=identity_context or [],
        details=details
    )
