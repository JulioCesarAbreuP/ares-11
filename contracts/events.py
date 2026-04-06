from pydantic import BaseModel
from typing import Any, Dict, Optional

class IngestEvent(BaseModel):
    timestamp: float
    src_ip: str
    device: str
    raw_data: Dict[str, Any]

class AnomalyEvent(BaseModel):
    timestamp: float
    src_ip: str
    anomaly_score: float
    details: Dict[str, Any]

class CorrelationEvent(BaseModel):
    timestamp: float
    src_ip: str
    correlated: bool
    risk_level: str
    details: Dict[str, Any]

class GatewayEvent(BaseModel):
    timestamp: float
    src_ip: str
    sanitized_data: Dict[str, Any]
    signals: Dict[str, Any]

class DecisionEvent(BaseModel):
    timestamp: float
    src_ip: str
    action: str
    confidence: float
    details: Dict[str, Any]

class EnforcementEvent(BaseModel):
    timestamp: float
    src_ip: str
    enforcement_action: str
    status: str
    details: Dict[str, Any]
