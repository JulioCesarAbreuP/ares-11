import time
from contracts.events import AnomalyEvent, CorrelationEvent
from event_bus.event_bus import bus

def check_health():
    return True

def handle_anomaly(payload):
    try:
        event = AnomalyEvent(**payload)
        # Simulación de correlación
        correlated = event.anomaly_score > 0.7
        correlation = CorrelationEvent(
            timestamp=time.time(),
            src_ip=event.src_ip,
            correlated=correlated,
            risk_level="high" if correlated else "low",
            details={"anomaly_score": event.anomaly_score}
        )
        bus.publish("CorrelationEvent", correlation.dict())
    except Exception as e:
        print(f"[CorrelationService] Error: {e}")

if __name__ == "__main__":
    bus.consume("AnomalyEvent", handle_anomaly)
    while True:
        time.sleep(1)
