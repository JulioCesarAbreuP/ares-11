from ..events import Event, TaxiiPullRequested
from ..utils import log
from ..orchestrator import Orchestrator

class TAXIIClient:
    def register(self, core: Orchestrator) -> None:
        core.on("taxii.pull.requested", self.handle_taxii_pull)

    def handle_taxii_pull(self, event: Event) -> None:
        collection = (event.payload or {}).get("collection", "default")
        log(f"[TAXIIClient] Realizando pull de colección: {collection}")
