# defense/identity_fusion_engine.py
"""
Identity Fusion Engine: Correlaciona eventos de red, identidad y permisos para detectar riesgos de movimiento lateral y abuso de privilegios.
Genera señales doctrinales y eleva el riesgo si detecta patrones sospechosos.
"""
from brain.tactical_memory import TacticalMemory

def identity_fusion(event, identity_context=None):
    signals = {
        "identity_fusion_risk": False,
        "fusion_details": None
    }
    # Simulación: correlación de IP, usuario y permisos
    if identity_context:
        for idev in identity_context:
            if (idev.get("src_ip") == event.get("ip") or
                idev.get("user") == event.get("user") or
                set(idev.get("roles", [])) & set(event.get("roles", []))):
                signals["identity_fusion_risk"] = True
                signals["fusion_details"] = {
                    "identity_link": idev,
                    "risk_reason": "Correlación de red e identidad con privilegios elevados"
                }
    # Integración con memoria táctica
    memory = TacticalMemory()
    match = memory.compare_with_past(str(event))
    if match["match"]:
        signals["identity_fusion_risk"] = True
        signals["fusion_details"] = {"memory_link": match}
    return signals
