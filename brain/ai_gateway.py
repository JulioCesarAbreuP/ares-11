import re

class ARES11_Gateway:
    def __init__(self):
        # Patrones de Inyección (Heurística de ataque)
        self.injection_patterns = [
            r"ignore all previous instructions",
            r"system override",
            r"new instructions:",
            r"forget what I told you",
            r"reprogram"
        ]
        # Patrones PII (DNI, Tarjetas, IPs sensibles)
        self.pii_patterns = {
            "DNI": r"\d{8}[A-Z]",
            "CreditCard": r"\b(?:\d[ -]*?){13,16}\b"
        }

    def sanitize_input(self, raw_data):
        clean_data = raw_data
        # 1. Filtro de Inyección (Defensa Activa)
        for pattern in self.injection_patterns:
            if re.search(pattern, clean_data, re.IGNORECASE):
                print("[!!!] ALERTA DE SEGURIDAD: Intento de Prompt Injection detectado.")
                return None # Bloqueo total del flujo
        # 2. Filtro PII (Privacidad - SC-300 Compliant)
        for label, pattern in self.pii_patterns.items():
            clean_data = re.sub(pattern, f"[REDACTED_{label}]", clean_data)
        return clean_data

# --- Integración con el Cerebro (Ollama) ---
def ask_ares_brain(raw_network_data):
    gateway = ARES11_Gateway()
    safe_data = gateway.sanitize_input(raw_network_data)
    if safe_data:
        # Aquí llamarías a tu script de Ollama que ya tenemos
        print("[+] Datos sanitizados enviados a Llama 3.")
        return safe_data
    else:
        return "ERROR: Intento de manipulación de IA bloqueado."
