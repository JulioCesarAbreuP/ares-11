from pydantic import BaseModel
from typing import Any, Dict, Optional

class AnomalyOutput(BaseModel):
    anomaly_type: str
    score: float
    details: Dict[str, Any]

class CorrelationOutput(BaseModel):
    correlation_id: str
    risk_level: str
    related_events: list
    details: Dict[str, Any]

class GatewayOutput(BaseModel):
    sanitized_input: str
    blocked: bool
    reason: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class DecisionOutput(BaseModel):
    action: str
    confidence: float
    justification: str
    metadata: Optional[Dict[str, Any]] = None

class ExecutionRequest(BaseModel):
    target: str
    action: str
    parameters: Dict[str, Any]
    request_id: Optional[str] = None
