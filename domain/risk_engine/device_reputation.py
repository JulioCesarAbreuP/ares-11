# domain/risk_engine/device_reputation.py
from domain.decision_engine.tactical_memory import TacticalMemory
from pipeline.stages.execution.execution_engine import ExecutionEngine
from core.contracts import DecisionOutput
from core.events import EventBus
from core.utils import log_event, trace, retry, sanitize_input

class DeviceReputation:
    def __init__(self, vector_db=None):
        self.db = vector_db or TacticalMemory()
        self.threshold = 0.7  # Umbral de desconfianza

    @trace(stage="device_reputation")
    @retry(retries=2, delay=1.0)
    def calculate_risk(self, device_id: str, current_activity: str, port_id: str = None, switch_ip: str = None) -> float:
        device_id = sanitize_input(device_id)
        current_activity = sanitize_input(current_activity)
        port_id = sanitize_input(port_id) if port_id else None
        switch_ip = sanitize_input(switch_ip) if switch_ip else None
        past_match = self.db.compare_with_past(current_activity)
        score = 1.0
        if past_match['match']:
            score -= past_match['confidence']
        log_event("device_reputation.calculated", {"device_id": device_id, "score": score}, context={"stage": "device_reputation"})
        EventBus().publish("device_reputation.calculated", {"device_id": device_id, "score": score})
        if score < self.threshold:
            self.trigger_sentinel_bridge(device_id, port_id, switch_ip)
        return score

    @trace(stage="device_reputation")
    @retry(retries=2, delay=1.0)
    def trigger_sentinel_bridge(self, device_id: str, port_id: str = None, switch_ip: str = None):
        device_id = sanitize_input(device_id)
        port_id = sanitize_input(port_id) if port_id else None
        switch_ip = sanitize_input(switch_ip) if switch_ip else None
        print(f"[!!!] SENTINEL BRIDGE: Iniciando aislamiento preventivo para {device_id}")
        if port_id and switch_ip:
            ExecutionEngine().execute({
                "switch_ip": switch_ip,
                "port": port_id,
                "ip": device_id,
                "user_real_name": "Desconocido"
            })
        log_event("device_reputation.sentinel_triggered", {"device_id": device_id}, context={"stage": "device_reputation"})
        EventBus().publish("device_reputation.sentinel_triggered", {"device_id": device_id})
