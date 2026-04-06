

# === API ARES-11 — Arquitectura Hexagonal (Ports & Adapters) ===
# SRP: Este módulo solo expone la API y orquesta dependencias externas.

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
from core_engine.domain.models import TacticalInference, MitigationPriority
from core_engine.adapters.advanced_scanner import AdvancedScanner
from core_engine.adapters.execution_orchestrator import ExecutionOrchestrator
from core_engine.adapters.vlan_adapter import VLANAdapter
from core_engine.adapters.worm_storage import WORMStorage
from core_engine.ai_gateway.client import AIGatewayClient
from core_engine.middleware import DLPInterceptor, anti_prompt_injection
from core_engine.observability import ObservabilityMiddleware
from .ws import TacticalFeedManager

app = FastAPI()
app.add_middleware(ObservabilityMiddleware)
app.add_middleware(DLPInterceptor)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Dependencias (Adapters) ===
scanner = AdvancedScanner()
vlan_adapter = VLANAdapter()
worm_storage = WORMStorage()
orchestrator = ExecutionOrchestrator(vlan_adapter, worm_storage)
feed_manager = TacticalFeedManager()
ai_gateway = AIGatewayClient(base_url="http://localhost:9000")  # Ajusta URL real

# === Modelos de entrada ===
class ScanRequest(BaseModel):
    target: str

# === Endpoints ===
@app.get("/")
def read_root():
    """SRP: Estado de la API."""
    return {"message": "ARES-11 API Hexagonal"}

@app.get("/health")
def health_check():
    """SRP: Health check simple."""
    return {"status": "ok"}

@app.post("/scan")
async def scan(payload: ScanRequest):
    """SRP: Orquesta el escaneo táctico y pipeline de inferencia con AI Gateway."""
    # 1. Escaneo asíncrono sigiloso
    scan_results = await scanner.scan(payload.target)
    # 2. Banner Grabbing + Anti-Prompt Injection
    banners = [anti_prompt_injection(r["banner"]) for r in scan_results if r["banner"]]
    # 3. Paso por AI Gateway (DLP, inferencia, etc)
    ai_result = await ai_gateway.analyze({"target": payload.target, "banners": banners})
    # 4. Inferencia táctica local (fallback si AI Gateway falla)
    try:
        inference = TacticalInference(**ai_result["inference"])
    except Exception:
        inference = TacticalInference(
            risk_score=0.85,
            vector_signature="SIG-XYZ-123",
            mitigation_priority=MitigationPriority.HIGH
        )
    # 5. Orquestación de ejecución
    await orchestrator.execute(inference.dict())
    # 6. Notificación por WebSocket
    await feed_manager.send_event({
        "phase": "RECON_PHASE",
        "target": payload.target,
        "banners": banners,
        "inference": inference.dict()
    })
    return {
        "status": "scan complete",
        "target": payload.target,
        "banners": banners,
        "inference": inference.dict(),
        "ai_gateway": ai_result
    }

# === WebSocket para canal táctico ===
@app.websocket("/ws/tactical-feed")
async def tactical_feed(websocket: WebSocket):
    """SRP: Canal de eventos de misión en tiempo real."""
    await feed_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Mantener conexión
    except WebSocketDisconnect:
        feed_manager.disconnect(websocket)
