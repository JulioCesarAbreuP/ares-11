# GUÍA DE INTEGRACIÓN EXTERNA ARES-11

## 1. Visión General
ARES-11 permite integración segura con SIEM, EDR, API REST, colas y plataformas de orquestación.

## 2. Puntos de Integración
- API REST (en /interfaces/rest)
- Event Bus (contratos en /core/events.py)
- Webhooks y notificaciones
- Adaptadores para EASM, microsegmentación, DLP

## 3. Contratos y Seguridad
- Todos los datos deben cumplir contratos tipados (ver /core/contracts.py)
- El AI Gateway bloquea y audita cualquier intento de fuga o prompt injection
- Logs y auditoría disponibles en /logs y WORM

## 4. Ejemplo de Integración
```python
from core.contracts import SignalIngest
from interfaces.rest.api import send_signal
signal = SignalIngest(source="SIEM", data="alerta crítica")
send_signal(signal)
```

## 5. Requisitos
- Python 3.10+, dependencias en requirements.txt
- Acceso a endpoints y contratos validados

## 6. Soporte
- Contacto: equipo de arquitectura
- Documentación técnica: /docs/TECHNICAL_GUIDE.md
