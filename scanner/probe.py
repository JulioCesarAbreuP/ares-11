from scapy.all import IP, TCP, sr1
import json

def tactical_scan(target_ip, port):
    # Enviamos un paquete SYN (Hacking Tradicional)
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    
    result = {"ip": target_ip, "port": port, "status": "Closed", "risk": "Low"}
    
    if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        result["status"] = "Open"
        # Determinismo: Si el TTL es 128, es probable que sea Windows (Contexto AZ-104)
        result["os_guess"] = "Windows" if response.ttl == 128 else "Linux"
        result["risk"] = "High" if port in [445, 3389] else "Medium"
        
    return result

# Guardamos el hallazgo para el motor de correlación
with open('data_scan.json', 'w') as f:
    json.dump(tactical_scan("192.168.1.1", 445), f)
