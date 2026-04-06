import time
from core.utils import log_event

def vlan_shift_asset(asset_id: str, vlan_id: str = "quarantine"):
    """
    Aísla físicamente un activo cambiando su VLAN a una de cuarentena.
    Lanza excepción si el switch no responde.
    """
    log_event("infra.vlan_shift.start", {"asset": asset_id, "vlan": vlan_id})
    # Simulación de llamada a API de switch/SDN
    try:
        # Aquí iría la integración real (Netmiko, REST, SNMP, etc)
        if asset_id == "fail":
            raise ConnectionError("Switch no responde")
        time.sleep(0.2)  # Simula latencia
        log_event("infra.vlan_shift.success", {"asset": asset_id, "vlan": vlan_id})
        return True
    except Exception as e:
        log_event("infra.vlan_shift.error", {"asset": asset_id, "error": str(e)})
        raise
