from abc import ABC, abstractmethod
from typing import Any

class ISurveillanceEngine(ABC):
    """Contrato para motores de reconocimiento."""
    @abstractmethod
    async def scan(self, target: str) -> Any:
        pass

class IExecutionOrchestrator(ABC):
    """Contrato para la toma de acciones."""
    @abstractmethod
    async def execute(self, analysis_result: dict) -> None:
        pass
