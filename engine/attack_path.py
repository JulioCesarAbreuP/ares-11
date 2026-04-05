# engine/attack_path.py

def trace_attack_path(scan_results):
    paths = []
    # Buscamos dispositivos con criticidad ALTA (Passwords por defecto)
    entry_points = [h for h in scan_results if h.get('risk_level') == 'CRITICAL']
    
    for entry in entry_points:
        path = f"START: {entry['ip']} ({entry.get('device_type','Unknown')})"
        # Si el dispositivo está en la VLAN 1 (Administración)
        if entry.get('vlan') == 1 or entry.get('vlan') == 'admin':
            path += " --> [PIVOT] Router Mgmt Interface"
            path += " --> [TARGET] Active Directory / Azure Gateway"
            paths.append({"path": path, "severity": "EMERGENCY"})
        else:
            # Ruta genérica: IoT -> Router -> PC Admin -> AD
            path += " --> [PIVOT] Office Router"
            path += " --> [PIVOT] Admin PC"
            path += " --> [TARGET] Active Directory / Azure Gateway"
            paths.append({"path": path, "severity": "HIGH"})
    return paths
