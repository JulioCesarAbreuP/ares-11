import re
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

PII_PATTERNS = [
    re.compile(r'\b\d{8,10}[A-Z]?\b'),  # DNI
    re.compile(r'\b(?:\d[ -]*?){13,16}\b'),  # Tarjeta
    re.compile(r'\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'),  # IP interna
]

class DLPInterceptor(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == 'POST':
            body = await request.body()
            for pattern in PII_PATTERNS:
                body = pattern.sub(b'[REDACTED]', body)
            request._body = body
        response = await call_next(request)
        return response

def anti_prompt_injection(banner: str) -> str:
    # Filtra secuencias peligrosas
    return re.sub(r'[\x1b\x00\x1f\x7f]|system\s*prompt', '[FILTERED]', banner, flags=re.IGNORECASE)
