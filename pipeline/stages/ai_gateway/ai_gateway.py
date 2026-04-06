import re
from core.events import EventBus
from core.contracts import GatewayOutput

class ARES11Gateway:
    def __init__(self):
        self.injection_patterns = [
            r"ignore all previous instructions",
            r"system override",
            r"new instructions:",
            r"forget what I told you",
            r"reprogram"
        ]
        self.pii_patterns = {
            "DNI": r"\d{8}[A-Z]",
            "CreditCard": r"\b(?:\d[ -]*?){13,16}\b"
        }

    def sanitize_input(self, raw_data) -> GatewayOutput:
        clean_data = raw_data
        blocked = False
        reason = None
        for pattern in self.injection_patterns:
            if re.search(pattern, clean_data, re.IGNORECASE):
                blocked = True
                reason = "Prompt Injection detected"
                print("[!!!] ALERTA DE SEGURIDAD: Intento de Prompt Injection detectado.")
                EventBus().publish("gateway.blocked", {"reason": reason})
                return GatewayOutput(sanitized_input=None, blocked=True, reason=reason)
        for label, pattern in self.pii_patterns.items():
            clean_data = re.sub(pattern, f"[REDACTED_{label}]", clean_data)
        EventBus().publish("gateway.sanitized", {"input": clean_data})
        return GatewayOutput(sanitized_input=clean_data, blocked=False)

def ask_ares_brain(raw_network_data):
    gateway = ARES11Gateway()
    output = gateway.sanitize_input(raw_network_data)
    if output.sanitized_input:
        print("[+] Datos sanitizados enviados a Llama 3.")
        return output.sanitized_input
    else:
        return "ERROR: Intento de manipulación de IA bloqueado."