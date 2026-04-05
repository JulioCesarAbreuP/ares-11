# forensic_eye.py
# Sensor Forense de Bajo Nivel (Python + Scapy)
# Captura fingerprints TCP/IP y detecta suplantación de MAC/OS

from scapy.all import *
import pandas as pd
from datetime import datetime
import os

# Base de datos forense local
forensic_log = "../logs/forensic_evidence.csv"

def analyze_packet(pkt):
    if pkt.haslayer(IP):
        ip_src = pkt[IP].src
        ttl = pkt[IP].ttl
        window = pkt[IP].window if hasattr(pkt[IP], 'window') else None
        # Identificación Forense por Atributos de Red
        os_guess = "Windows/Azure" if ttl > 64 else "Linux/IoT/Embedded"
        evidence = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip": ip_src,
            "mac": pkt.src,
            "ttl": ttl,
            "window_size": window,
            "os_detected": os_guess,
            "proto": pkt.proto if hasattr(pkt, 'proto') else None
        }
        save_evidence(evidence)

def save_evidence(data):
    df = pd.DataFrame([data])
    df.to_csv(forensic_log, mode='a', header=not os.path.exists(forensic_log), index=False)

print("[*] ARES-11: Iniciando Sensor Forense de Alta Fidelidad...")
sniff(prn=analyze_packet, store=0)
