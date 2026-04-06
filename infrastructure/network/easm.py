from core.utils import log_event

def notify_easm(incident_id: str, assets: list):
    """
    Notifica a la plataforma EASM para gestión de superficie externa.
    """
    log_event("infra.easm_notify.start", {"incident_id": incident_id, "assets": assets})
    # Simulación de integración con EASM (API REST, etc)
    if not assets:
        raise ValueError("No assets to notify")
    # Aquí iría la llamada real
    log_event("infra.easm_notify.success", {"incident_id": incident_id, "assets": assets})
    return True
