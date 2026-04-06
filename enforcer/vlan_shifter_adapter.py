# Integración de VLAN Shifter como microservicio
from enforcer.vlan_shifter import isolate_port

def check_health():
    try:
        isolate_port("127.0.0.1", "test_port", vlan_quarantine=999)
        return True
    except Exception:
        return False

def isolate(switch_ip, port, vlan_quarantine):
    return isolate_port(switch_ip, port, vlan_quarantine)
