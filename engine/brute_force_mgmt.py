import requests
from requests.auth import HTTPBasicAuth

# Lista optimizada de credenciales comunes en entornos industriales y de oficina
COMMON_CREDS = [
    ("admin", "admin"), ("admin", "password"), ("root", "root"), ("admin", "1234"), ("ubnt", "ubnt"),
    ("cisco", "cisco"), ("support", "support"), ("user", "user"), ("admin", ""), ("root", "password"),
    ("administrator", "admin"), ("admin", "12345"), ("admin", "pass"), ("admin", "123456"), ("admin", "admin123"),
    ("admin", "changeme"), ("admin", "default"), ("admin", "superuser"), ("admin", "supervisor"), ("admin", "manager"),
    ("cisco", "default"), ("cisco", "password"), ("cisco", "1234"), ("cisco", "12345"), ("cisco", "123456"),
    ("hp", "hp"), ("hp", "admin"), ("hp", "password"), ("hp", "1234"), ("hp", "12345"),
    ("tplink", "tplink"), ("tplink", "admin"), ("tplink", "password"), ("tplink", "1234"),
    ("ubiquiti", "ubnt"), ("ubiquiti", "ubiquiti"), ("ubiquiti", "admin"), ("ubiquiti", "password"),
    ("guest", "guest"), ("guest", "password"), ("guest", "1234"), ("guest", "guest123"),
    ("operator", "operator"), ("operator", "password"), ("operator", "1234"),
    ("supervisor", "supervisor"), ("supervisor", "password"), ("supervisor", "1234"),
    ("manager", "manager"), ("manager", "password"), ("manager", "1234")
]

COMMON_PATHS = ["/admin", "/admin/login.php", "/config", "/setup", "/login", "/administrator", "/manage"]

def audit_web_management(target_ip, port=80):
    url_base = f"http://{target_ip}:{port}"
    print(f"[*] ARES-11: Iniciando auditoría de acceso en {url_base}...")
    
    # Barrido de rutas comunes de administración
    for path in COMMON_PATHS:
        url = url_base + path
        try:
            resp = requests.get(url, timeout=2)
            if resp.status_code == 200:
                print(f"[!] Panel de gestión expuesto: {url}")
        except requests.exceptions.RequestException:
            continue
    
    # Prueba de credenciales en la raíz
    for user, pwd in COMMON_CREDS:
        try:
            response = requests.get(url_base, auth=HTTPBasicAuth(user, pwd), timeout=2)
            if response.status_code == 200:
                print(f"[!!!] CRÍTICO: Acceso concedido en {target_ip} con {user}:{pwd}")
                return {
                    "status": "VULNERABLE",
                    "creds": f"{user}:{pwd}",
                    "mitre": "T1078 (Valid Accounts)",
                    "ms_defense": "SC-300: Falta de gobierno de identidades. Remediación: Rotación de claves y MFA."
                }
        except requests.exceptions.RequestException:
            continue
    return {"status": "SECURE", "detail": "Credenciales por defecto no encontradas"}
