import re
from core.utils import log_event

PII_PATTERNS = [
    re.compile(r"\\b\d{3}-\d{2}-\d{4}\\b"),  # SSN
    re.compile(r"\\b\d{16}\\b"),              # Credit Card
    re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+"),  # Email
]

PROMPT_INJECTION_PATTERNS = [
    re.compile(r"\{\{.*?\}\}"),
    re.compile(r"system:", re.IGNORECASE),
]

def dlp_scan(data: str) -> bool:
    """
    Devuelve True si detecta PII o patrones prohibidos.
    """
    for pat in PII_PATTERNS + PROMPT_INJECTION_PATTERNS:
        if pat.search(data):
            log_event("dlp.detected", {"pattern": pat.pattern, "data": data[:40]})
            return True
    return False

def anonymize_pii(data: str) -> str:
    """
    Reemplaza PII por [REDACTED].
    """
    for pat in PII_PATTERNS:
        data = pat.sub("[REDACTED]", data)
    return data
