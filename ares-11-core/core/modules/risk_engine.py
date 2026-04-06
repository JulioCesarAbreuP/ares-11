from ..events import Event, RiskAnalysisRequested
from ..utils import log
from ..orchestrator import Orchestrator

class RiskEngine:
    def register(self, core: Orchestrator) -> None:
        core.on("risk.analysis.requested", self.handle_risk_analysis)

    def handle_risk_analysis(self, event: Event) -> None:
        target = (event.payload or {}).get("target", "desconocido")
        log(f"[RiskEngine] Analizando riesgo para: {target}")
