def analyze_ecosystem_health(scan_data):
    for ip, details in scan_data.items():
        print(f"\n--- Auditoría para: {ip} ({details['os']}) ---")
        
        # 1. Puertos Abiertos Innecesarios (CIS 4.1 / AZ-104)
        critical_ports = [21, 23, 445, 3389] # FTP, Telnet, SMB, RDP
        for p in details['open_ports']:
            if p['port'] in critical_ports:
                print(f"[!] RIESGO ALTO: Puerto {p['port']} ({p['service']}) abierto.")
        
        # 2. Software Desactualizado
        for p in details['open_ports']:
            if p['version'] == "":
                print(f"[?] ADVERTENCIA: No se pudo verificar versión en puerto {p['port']}. Posible Shadow IT.")
        
        # 3. Contraseñas Débiles (SC-300 / Hacking Tradicional)
        for vuln in details['vulnerabilities']:
            if "password" in str(vuln).lower():
                print(f"[!!!] CRÍTICO: Se detectó contraseña débil o por defecto.")
