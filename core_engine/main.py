from time import sleep

from core.orchestrator import Orchestrator
from core.events import SystemStartEvent, TickEvent, RiskAnalysisRequested, TaxiiPullRequested
from core.modules import RiskEngine, TAXIIClient
from core.utils import log

def main() -> None:
    log("Iniciando ARES-11 Core (Orquestador)...")

    core = Orchestrator()

    core.register_module(RiskEngine())
    core.register_module(TAXIIClient())

    core.emit(SystemStartEvent())
    core.emit(RiskAnalysisRequested(payload={"target": "host-01.internal"}))
    core.emit(TaxiiPullRequested(payload={"collection": "enterprise-threats"}))

    for i in range(3):
        core.emit(TickEvent(payload={"tick": i}))
        core.process_events()
        sleep(1)

    log("Finalizando demo del Core ARES-11.")

if __name__ == "__main__":
    main()
