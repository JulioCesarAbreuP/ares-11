import time
from contracts.events import CorrelationEvent, GatewayEvent
from event_bus.event_bus import bus

def check_health():
    return True

def handle_correlation(payload):
    try:
        event = CorrelationEvent(**payload)
        # Simulación de AI Gateway
        sanitized_data = event.details
        signals = {"ai_gateway_blocked": False}
        gateway_event = GatewayEvent(
            timestamp=time.time(),
            src_ip=event.src_ip,
            sanitized_data=sanitized_data,
            signals=signals
        )
        bus.publish("GatewayEvent", gateway_event.dict())
    except Exception as e:
        print(f"[GatewayService] Error: {e}")

if __name__ == "__main__":
    bus.consume("CorrelationEvent", handle_correlation)
    while True:
        time.sleep(1)
