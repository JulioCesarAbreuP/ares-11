import time
from contracts.events import IngestEvent, AnomalyEvent
from event_bus.event_bus import bus

def check_health():
    return True

def handle_ingest(payload):
    try:
        event = IngestEvent(**payload)
        # Simulación de análisis de anomalía
        anomaly_score = 0.8  # Dummy
        anomaly = AnomalyEvent(
            timestamp=time.time(),
            src_ip=event.src_ip,
            anomaly_score=anomaly_score,
            details={"detected": anomaly_score > 0.7}
        )
        bus.publish("AnomalyEvent", anomaly.dict())
    except Exception as e:
        print(f"[AnomalyService] Error: {e}")

if __name__ == "__main__":
    bus.consume("IngestEvent", handle_ingest)
    while True:
        time.sleep(1)
