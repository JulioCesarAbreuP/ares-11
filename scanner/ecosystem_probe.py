import nmap
import json

def audit_ecosystem(target_network):
    # -sV: Detección de versiones (Software desactualizado)
    # -sC: Ejecuta scripts por defecto (Contraseñas débiles, vulnerabilidades comunes)
    # --script ssl-cert: Revisa si los certificados están vencidos (Políticas)
    nm = nmap.PortScanner()
    print(f"[*] Escaneando ecosistema en {target_network}...")
    
    # Escaneo profundo: Puertos comunes + Vulnerabilidades + Versiones
    nm.scan(hosts=target_network, arguments='-sV -sC --script=auth,vuln,default')
    
    results = {}
    for host in nm.all_hosts():
        results[host] = {
            "status": nm[host].state(),
            "os": nm[host].get('osmatch', [{"name": "Desconocido"}])[0]['name'],
            "vulnerabilities": [],
            "open_ports": []
        }
        
        # Analizar puertos y scripts (Contraseñas y Versiones)
        if 'tcp' in nm[host]:
            for port, info in nm[host]['tcp'].items():
                port_data = {
                    "port": port,
                    "service": info['name'],
                    "version": info['version'],
                    "state": info['state']
                }
                results[host]["open_ports"].append(port_data)
                
                # Si el script detecta algo (ej: "password: admin")
                if 'script' in info:
                    results[host]["vulnerabilities"].append(info['script'])

    with open('reports/ecosystem_scan.json', 'w') as f:
        json.dump(results, f, indent=4)
    return results
