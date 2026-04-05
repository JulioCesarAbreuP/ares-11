import nmap

def get_deep_infrastructure_details(target_ip):
    nm = nmap.PortScanner()
    # -O: OS Detection (Usa el stack TCP/IP para saber si es Win 10, 11 o Server)
    # -sV: Version Detection (Saca la versión del firmware del router/switch)
    # --osscan-guess: Agresivo para identificar sistemas difíciles
    print(f"[*] Interrogando infraestructura en {target_ip}...")
    nm.scan(hosts=target_ip, arguments='-O -sV --osscan-guess')

    if target_ip in nm.all_hosts():
        os_info = nm[target_ip].get('osmatch', [])
        firmware_info = nm[target_ip].get('tcp', {})
        print(f"--- RESULTADO TÁCTICO: {target_ip} ---")
        if os_info:
            print(f"[+] OS Detectado: {os_info[0]['name']} (Precisión: {os_info[0]['accuracy']}%)")
        for port, data in firmware_info.items():
            if data['version']:
                print(f"[+] Servicio en Puerto {port}: {data['product']} v{data['version']}")
