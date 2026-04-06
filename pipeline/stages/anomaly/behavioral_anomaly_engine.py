# pipeline/stages/anomaly/behavioral_anomaly_engine.py
"""
Behavioral Anomaly Engine: Detecta patrones anómalos en banners, hostnames y puertos.
Formalizado para arquitectura enterprise.
"""
import re
from domain.decision_engine.tactical_memory import TacticalMemory
from core.contracts import AnomalyOutput
from core.events import EventBus

def detect_anomalies(event: dict) -> AnomalyOutput:
    details = {}
    anomaly_detected = False
    banner = event.get("banner", "")
    hostname = event.get("hostname", "")
    port = str(event.get("port", ""))
    if re.search(r"ignore|override|reprogram|root|shell", banner, re.IGNORECASE):
        anomaly_detected = True
        details["banner"] = banner
    if re.search(r"^x[a-z0-9]{8,}$|bot|infected|malware", hostname, re.IGNORECASE):
        anomaly_detected = True
        details["hostname"] = hostname
    if port not in ["22", "80", "443", "3389", "445"] and port.isdigit() and int(port) > 1024:
        anomaly_detected = True
        details["port"] = port
    memory = TacticalMemory()
    match = memory.compare_with_past(str(event))
    if match["match"]:
        anomaly_detected = True
        details["memory_match"] = match
    EventBus().publish("anomaly.detected", details)
    return AnomalyOutput(anomaly_type="behavioral", score=1.0 if anomaly_detected else 0.0, details=details)
