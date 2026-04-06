from brain.tactical_memory import TacticalMemory
from enforcer.vlan_shifter import isolate_port

class DeviceReputation:
    def __init__(self, vector_db=None):
        self.db = vector_db or TacticalMemory()
        self.threshold = 0.7  # Umbral de desconfianza

    def calculate_risk(self, device_id, current_activity, port_id=None, switch_ip=None):
        # 1. Buscamos en la Memoria Táctica si este patrón es conocido
        past_match = self.db.compare_with_past(current_activity)
        score = 1.0  # Empezamos con confianza plena
        if past_match['match']:
            score -= past_match['confidence']
        print(f"[*] Reputación para {device_id}: {score:.2f}")
        # 2. Si el score cae, disparamos el Sentinel Bridge
        if score < self.threshold:
            self.trigger_sentinel_bridge(device_id, port_id, switch_ip)
        return score

    def trigger_sentinel_bridge(self, device_id, port_id=None, switch_ip=None):
        print(f"[!!!] SENTINEL BRIDGE: Iniciando aislamiento preventivo para {device_id}")
        if port_id and switch_ip:
            isolate_port(switch_ip, port_id, vlan_quarantine=999)
        # Aquí se podría integrar con Azure Sentinel vía API en el futuro
