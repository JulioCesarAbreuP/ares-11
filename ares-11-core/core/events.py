from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class Event:
    name: str
    payload: Dict[str, Any] | None = None

@dataclass
class SystemStartEvent(Event):
    name: str = "system.start"

@dataclass
class TickEvent(Event):
    name: str = "system.tick"

@dataclass
class RiskAnalysisRequested(Event):
    name: str = "risk.analysis.requested"

@dataclass
class TaxiiPullRequested(Event):
    name: str = "taxii.pull.requested"
