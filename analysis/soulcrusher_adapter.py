# Integración de SoulCrusher como microservicio
from engine.soul_crusher import SoulCrusher
import os

def check_health():
    try:
        crusher = SoulCrusher(os.getenv("SHODAN_API_KEY", "demo"))
        crusher.annihilate_target("127.0.0.1")
        return True
    except Exception:
        return False

def run_osint(ip):
    crusher = SoulCrusher(os.getenv("SHODAN_API_KEY", "demo"))
    return crusher.annihilate_target(ip)
