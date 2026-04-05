import nmap # Wrapper para libnmap (necesitas nmap instalado en el sistema)
import json

def industrial_scan(network_range):
    # -sS: SYN Scan (Hacking Tradicional - Sigiloso)
    # -O: OS Detection (Para AZ-104/SC-300)
    # -T4: Velocidad agresiva para entornos de oficina
    # --script vuln: Busca vulnerabilidades críticas (CVE) automáticamente
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
    return results
