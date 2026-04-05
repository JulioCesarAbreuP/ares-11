from scapy.all import *
from scapy.layers.l2 import LLDPDU, Dot3

def packet_callback(pkt):
    # Detectar LLDP (Estándar universal: Switches, APs, VoIP)
    if pkt.haslayer(LLDPDU):
        print(f"\n[+] DISPOSITIVO DE RED DETECTADO (LLDP)")
        # Extraer Chasis ID (MAC) y Port ID
        print(f"    - Chassis ID: {pkt[LLDPDU].getlayer(1).value.hex(':')}")
        # Extraer System Name y Description (Aquí viene el MODELO y FIRMWARE)
        for tlv in pkt[LLDPDU].payload.arguments:
            if hasattr(tlv, 'type'):
                if tlv.type == 5: print(f"    - Nombre: {tlv.value.decode()}")
                if tlv.type == 6: print(f"    - Descripción/Firmware: {tlv.value.decode()}")

    # Detectar mDNS (Aquí caen las Cafeteras IoT, Impresoras, Apple TV)
    if pkt.haslayer(UDP) and pkt[UDP].dport == 5353:
        print(f"[+] DISPOSITIVO IoT DETECTADO (mDNS): {pkt[IP].src}")

print("[*] ARES-11 en modo Escucha Pasiva... (Presiona Ctrl+C para detener)")
sniff(prn=packet_callback, store=0, filter="ether proto 0x88cc or udp port 5353")
