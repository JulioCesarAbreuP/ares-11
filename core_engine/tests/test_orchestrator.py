import pytest
import asyncio
from core_engine.adapters.execution_orchestrator import ExecutionOrchestrator

class DummyVLAN:
    async def vlan_shift_asset(self):
        self.called = True
        return True

class DummyWORM:
    async def persist_event(self, event):
        self.persisted = event
        return True

@pytest.mark.asyncio
async def test_orchestrator_executes_vlan():
    vlan = DummyVLAN()
    worm = DummyWORM()
    orchestrator = ExecutionOrchestrator(vlan, worm, risk_threshold=0.5)
    analysis = {"risk_score": 0.9, "vector_signature": "sig", "mitigation_priority": "HIGH"}
    await orchestrator.execute(analysis)
    assert hasattr(vlan, "called")
    assert hasattr(worm, "persisted")
