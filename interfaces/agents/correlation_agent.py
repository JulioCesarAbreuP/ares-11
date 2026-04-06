# interfaces/agents/correlation_agent.py
"""
Agente de correlación de amenazas. Consume eventos de anomalía y publica eventos de correlación.
Formalizado para arquitectura enterprise.
"""

import time
from core.contracts import CorrelationOutput
from core.events import EventBus
from core.utils import log_event, trace, retry, sanitize_input

@trace(stage="agent.correlation")
@retry(retries=2, delay=1.0)
def handle_anomaly(payload):
    try:
        payload = sanitize_input(payload)
        correlated = payload.get('score', 0) > 0.7
        correlation = CorrelationOutput(
            correlation_id="dummy-001",
            risk_level="high" if correlated else "low",
            related_events=[],
            details={"anomaly_score": payload.get('score', 0)}
        )
        EventBus().publish("CorrelationEvent", correlation.dict())
        log_event("agent.correlation.published", correlation.dict(), context={"stage": "correlation_agent"})
    except Exception as e:
        log_event("agent.correlation.error", str(e), context={"stage": "correlation_agent"})
        print(f"[CorrelationAgent] Error: {e}")

if __name__ == "__main__":
    # Simulación de consumo de eventos
    while True:
        # Punto de extensión: integración con bus real, colas, SIEM
        time.sleep(1)
