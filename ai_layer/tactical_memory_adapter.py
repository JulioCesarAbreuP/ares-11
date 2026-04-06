# Integración de TacticalMemory como microservicio
from brain.tactical_memory import TacticalMemory

def check_health():
    try:
        memory = TacticalMemory()
        memory.store_incident("test", "desc", {})
        return True
    except Exception:
        return False

def store_incident(incident_id, incident_desc, metadata):
    memory = TacticalMemory()
    memory.store_incident(incident_id, incident_desc, metadata)

def compare_with_past(incident_desc):
    memory = TacticalMemory()
    return memory.compare_with_past(incident_desc)
