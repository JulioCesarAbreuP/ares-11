import time
from contracts.events import IngestEvent
from event_bus.event_bus import bus

def check_health():
    return True

def sniffer_loop():
    while True:
        # Simulación de ingesta de datos
        event = IngestEvent(
            timestamp=time.time(),
            src_ip="192.168.1.100",
            device="router01",
            raw_data={"banner": "Welcome admin!", "port": 8080}
        )
        bus.publish("IngestEvent", event.dict())
        time.sleep(2)

if __name__ == "__main__":
    sniffer_loop()
