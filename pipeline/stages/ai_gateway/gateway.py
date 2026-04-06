from core.contracts import SignalIngest, SignalValidated
from infrastructure.dlp.dlp_engine import dlp_scan, anonymize_pii
from core.utils import log_event, sanitize_input, trace
from infrastructure.storage.worm_logger import upload_worm_log
from infrastructure.storage.forensics_packager import package_forensics
import os

SECURITY_POLICIES = {
    "block_on_dlp": True,
    "block_on_prompt_injection": True,
    "quarantine_on_violation": True,
    "worm_log": True,
    "forensics_pack": True,
}

@trace(stage="ai_gateway")
def ai_gateway_stage(signal: SignalIngest) -> SignalValidated:
    log_event("ai_gateway.input", {"source": signal.source, "size": len(str(signal.data))})
    # Sanitización profunda
    clean_data = sanitize_input(signal.data)
    # Validación estricta de contrato
    try:
        SignalIngest(**signal.dict())
    except Exception as e:
        log_event("ai_gateway.contract_error", {"error": str(e)})
        raise
    # DLP y Prompt Injection
    dlp_violation = dlp_scan(clean_data)
    if dlp_violation and SECURITY_POLICIES["block_on_dlp"]:
        log_event("ai_gateway.dlp_block", {"reason": "DLP violation"})
        if SECURITY_POLICIES["worm_log"]:
            upload_worm_log(str(clean_data))
        if SECURITY_POLICIES["forensics_pack"]:
            package_forensics(type("Req", (), {"evidence_paths": [str(clean_data)], "output_zip": "DLP-violation.zip"}))
        if SECURITY_POLICIES["quarantine_on_violation"]:
            # Aquí se podría aislar el origen
            log_event("ai_gateway.quarantine", {"source": signal.source})
        raise ValueError("DLP violation: sensitive data detected")
    # Redacción automática
    redacted_data = anonymize_pii(clean_data)
    # Prompt Injection
    if ("{" in redacted_data or "}}}" in redacted_data or "system:" in redacted_data.lower()) and SECURITY_POLICIES["block_on_prompt_injection"]:
        log_event("ai_gateway.prompt_injection", {"payload": redacted_data})
        if SECURITY_POLICIES["worm_log"]:
            upload_worm_log(str(redacted_data))
        if SECURITY_POLICIES["forensics_pack"]:
            package_forensics(type("Req", (), {"evidence_paths": [str(redacted_data)], "output_zip": "PromptInjection.zip"}))
        if SECURITY_POLICIES["quarantine_on_violation"]:
            log_event("ai_gateway.quarantine", {"source": signal.source})
        raise ValueError("Prompt injection detected")
    # Auditoría completa
    log_event("ai_gateway.passed", {"source": signal.source, "data": redacted_data[:40]})
    if SECURITY_POLICIES["worm_log"]:
        upload_worm_log(str(redacted_data))
    # Salida tipada
    return SignalValidated(**{**signal.dict(), "data": redacted_data})

# Punto de extensión para modelos futuros
# def ai_gateway_custom_model(signal: SignalIngest) -> SignalValidated:
#     ...