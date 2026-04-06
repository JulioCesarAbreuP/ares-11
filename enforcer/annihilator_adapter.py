# Integración de Annihilator como microservicio
from enforcer.annihilator import execute_annihilation

def check_health():
    try:
        execute_annihilation({"switch_ip": "127.0.0.1", "port": "test", "ip": "127.0.0.1", "user_real_name": "test"})
        return True
    except Exception:
        return False

def annihilate(target_data):
    return execute_annihilation(target_data)
