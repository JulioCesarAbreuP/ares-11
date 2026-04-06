# defense/behavioral_anomaly_engine.py
"""
Behavioral Anomaly Engine: Detecta patrones anómalos en banners, hostnames y puertos.
Integra señales de riesgo y eleva el nivel de alerta si detecta comportamientos fuera de lo normal.
"""
import re
from brain.tactical_memory import TacticalMemory

def detect_anomalies(event):
    signals = {
        "anomaly_detected": False,
        "anomaly_details": None
    }
    # Heurísticas simples (pueden ampliarse con ML en el futuro)
    banner = event.get("banner", "")
    hostname = event.get("hostname", "")
    port = str(event.get("port", ""))
    # Detectar comandos sospechosos en banners
    if re.search(r"ignore|override|reprogram|root|shell", banner, re.IGNORECASE):
        signals["anomaly_detected"] = True
        signals["anomaly_details"] = f"Banner sospechoso: {banner}"
    # Hostnames anómalos (nombres raros, patrones de botnet, etc)
    if re.search(r"^x[a-z0-9]{8,}$|bot|infected|malware", hostname, re.IGNORECASE):
        signals["anomaly_detected"] = True
        signals["anomaly_details"] = f"Hostname anómalo: {hostname}"
    # Puertos inusuales
    if port not in ["22", "80", "443", "3389", "445"] and int(port) > 1024:
        signals["anomaly_detected"] = True
        signals["anomaly_details"] = f"Puerto inusual: {port}"
    # Correlación con memoria táctica
    memory = TacticalMemory()
    match = memory.compare_with_past(str(event))
    if match["match"]:
        signals["anomaly_detected"] = True
        signals["anomaly_details"] = f"Patrón persistente detectado: {match}"
    return signals
