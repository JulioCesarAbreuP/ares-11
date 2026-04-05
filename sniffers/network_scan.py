# network_scan.py
# Simulador de escaneo de red para ARES-11 OMNI
# Genera un JSON de dispositivos y vulnerabilidades para pruebas de IA táctica

import json
from datetime import datetime

def main():
    data = {
        "dispositivos": [
            {
                "nombre": "Cafetera",
                "ip": "192.168.1.50",
                "vulnerabilidades": ["SMB abierto", "Sin autenticación"],
                "riesgo": 9
            },
            {
                "nombre": "PC-04",
                "ip": "192.168.1.101",
                "vulnerabilidades": ["RDP sin MFA"],
                "riesgo": 7
            },
            {
                "nombre": "Router",
                "ip": "192.168.1.1",
                "vulnerabilidades": ["Firmware desactualizado"],
                "riesgo": 6
            }
        ],
        "domain_controller": {
            "nombre": "DC-01",
            "ip": "192.168.1.10"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    with open("scan_result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Escaneo simulado guardado en scan_result.json")

if __name__ == "__main__":
    main()
