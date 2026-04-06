from core_engine.domain.interfaces import IExecutionOrchestrator
from core_engine.domain.models import TacticalInference

class ExecutionOrchestrator(IExecutionOrchestrator):
    """Orquestador de ejecución con microsegmentación y circuit breaker."""
    def __init__(self, vlan_adapter, worm_storage, risk_threshold=0.7):
        self.vlan_adapter = vlan_adapter
        self.worm_storage = worm_storage
        self.risk_threshold = risk_threshold

    async def execute(self, analysis_result: dict) -> None:
        inference = TacticalInference(**analysis_result)
        if inference.risk_score > self.risk_threshold:
            try:
                await self.vlan_adapter.vlan_shift_asset()
            except Exception:
                await self.worm_storage.persist_event({"event": "CRITICAL_ALERT", "data": analysis_result})
        await self.worm_storage.persist_event({"event": "MISSION_COMPLETE", "data": analysis_result})
