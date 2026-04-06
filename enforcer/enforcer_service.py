import time
from contracts.events import DecisionEvent, EnforcementEvent
from event_bus.event_bus import bus

def check_health():
    return True

def handle_decision(payload):
    try:
        event = DecisionEvent(**payload)
        # Simulación de acción de enforcement
        enforcement_action = event.action
        status = "executed"
        enforcement = EnforcementEvent(
            timestamp=time.time(),
            src_ip=event.src_ip,
            enforcement_action=enforcement_action,
            status=status,
            details=event.details
        )
        bus.publish("EnforcementEvent", enforcement.dict())
    except Exception as e:
        print(f"[EnforcerService] Error: {e}")

if __name__ == "__main__":
    bus.consume("DecisionEvent", handle_decision)
    while True:
        time.sleep(1)
