# interfaces/agents/anomaly_agent.py
"""
Agente de análisis de anomalías. Consume eventos de ingestión y publica eventos de anomalía.
Formalizado para arquitectura enterprise.
"""

import time
from core.contracts import AnomalyOutput
from core.events import EventBus
from core.utils import log_event, trace, retry, sanitize_input

@trace(stage="agent.anomaly")
@retry(retries=2, delay=1.0)
def handle_ingest(payload):
    try:
        # Sanitizar y validar input
        payload = sanitize_input(payload)
        anomaly_score = 0.8  # Dummy
        anomaly = AnomalyOutput(
            anomaly_type="dummy",
            score=anomaly_score,
            details={"detected": anomaly_score > 0.7}
        )
        EventBus().publish("AnomalyEvent", anomaly.dict())
        log_event("agent.anomaly.published", anomaly.dict(), context={"stage": "anomaly_agent"})
    except Exception as e:
        log_event("agent.anomaly.error", str(e), context={"stage": "anomaly_agent"})
        print(f"[AnomalyAgent] Error: {e}")

if __name__ == "__main__":
    # Simulación de consumo de eventos
    while True:
        # Punto de extensión: integración con bus real, colas, SIEM
        time.sleep(1)
