# pipeline/stages/anomaly/high_speed_probe.py
"""
Escaneo táctico de red usando nmap. Formalizado para arquitectura enterprise.
"""
import nmap
import json
from core.utils import log_event
from core.contracts import AnomalyOutput

def industrial_scan(network_range: str) -> AnomalyOutput:
    nm = nmap.PortScanner()
    print(f"[*] Iniciando Barrido Táctico en {network_range}...")
    nm.scan(hosts=network_range, arguments='-sS -O -T4 --script vuln')
    results = []
    for host in nm.all_hosts():
        data = {
            "ip": host,
            "status": nm[host].state(),
            "os": nm[host].get('osmatch', [{}])[0].get('name', 'Unknown'),
            "ports": nm[host].get('tcp', {})
        }
        results.append(data)
    with open('logs/audit_live.json', 'w') as f:
        json.dump(results, f, indent=4)
    log_event("anomaly.scan.completed", {"network_range": network_range, "hosts": len(results)})
    return AnomalyOutput(anomaly_type="network_scan", score=1.0 if results else 0.0, details={"results": results})
