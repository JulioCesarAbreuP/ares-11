# engine/whitelist.py
"""
Permite marcar dispositivos confiables para evitar falsos positivos.
"""
import json

WHITELIST_FILE = 'data/whitelist.json'

def add_to_whitelist(ip):
    try:
        with open(WHITELIST_FILE, 'r') as f:
            wl = json.load(f)
    except:
        wl = []
    if ip not in wl:
        wl.append(ip)
        with open(WHITELIST_FILE, 'w') as f:
            json.dump(wl, f)
        print(f"[WHITELIST] {ip} añadido a la whitelist.")
    else:
        print(f"[WHITELIST] {ip} ya está en la whitelist.")

def is_whitelisted(ip):
    try:
        with open(WHITELIST_FILE, 'r') as f:
            wl = json.load(f)
        return ip in wl
    except:
        return False
