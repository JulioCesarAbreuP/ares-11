# interfaces/agents/external_surface_agent.py
"""
Agente de análisis de superficie externa (antes SoulCrusher). Consume eventos y ejecuta análisis OSINT.
Formalizado para arquitectura enterprise.
"""

import os
from pipeline.stages.execution.external_surface_analyzer import ExternalSurfaceAnalyzer
from core.utils import log_event, trace, retry, sanitize_input
from core.events import EventBus

@trace(stage="agent.external_surface")
@retry(retries=2, delay=1.0)
def handle_external_surface(ip):
    try:
        ip = sanitize_input(ip)
        analyzer = ExternalSurfaceAnalyzer(os.getenv("SHODAN_API_KEY", "demo"))
        result = analyzer.analyze(ip)
        EventBus().publish("ExternalSurfaceAnalyzed", result.dict())
        log_event("agent.external_surface.published", result.dict(), context={"stage": "external_surface_agent"})
    except Exception as e:
        log_event("agent.external_surface.error", str(e), context={"stage": "external_surface_agent"})
        print(f"[ExternalSurfaceAgent] Error: {e}")
