# engine/shodan_check.py
"""
Consulta Shodan para saber si un dispositivo es visible desde Internet.
"""
import requests

def check_shodan(ip, api_key):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('data'):
                print(f"[SHODAN] {ip} está expuesto en Internet!")
                return True
            else:
                print(f"[SHODAN] {ip} no está expuesto.")
                return False
        else:
            print(f"[SHODAN] Error: {resp.text}")
            return False
    except Exception as e:
        print(f"[SHODAN] Excepción: {e}")
        return False
