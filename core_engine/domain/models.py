from enum import Enum
from pydantic import BaseModel

class MitigationPriority(str, Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

class TacticalInference(BaseModel):
    risk_score: float
    vector_signature: str
    mitigation_priority: MitigationPriority
