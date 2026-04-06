import time
from contracts.events import GatewayEvent, DecisionEvent
from event_bus.event_bus import bus

def check_health():
    return True

def handle_gateway(payload):
    try:
        event = GatewayEvent(**payload)
        # Simulación de IA Táctica
        action = "isolate" if event.signals.get("ai_gateway_blocked") else "monitor"
        decision = DecisionEvent(
            timestamp=time.time(),
            src_ip=event.src_ip,
            action=action,
            confidence=0.95,
            details=event.sanitized_data
        )
        bus.publish("DecisionEvent", decision.dict())
    except Exception as e:
        print(f"[DecisionService] Error: {e}")

if __name__ == "__main__":
    bus.consume("GatewayEvent", handle_gateway)
    while True:
        time.sleep(1)
