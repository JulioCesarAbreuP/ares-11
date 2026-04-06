# Guía de Integración Externa para Empresas

Esta guía describe cómo integrar sistemas externos, SIEM, EDR, APIs y plataformas empresariales con ARES-11.

## 1. Contratos y APIs
- Todos los datos se intercambian mediante contratos Pydantic definidos en `/core/contracts.py`.
- Los eventos se publican y consumen vía `/core/events.py` (event bus).
- API REST y agentes disponibles en `/interfaces/`.

## 2. Requisitos de Integración
- Python 3.10+, dependencias en `requirements.txt`.
- Acceso a endpoints de integración (REST, colas, storage).
- Cumplimiento de contratos y eventos.

## 3. Seguridad y Auditoría
- Todos los inputs pasan por AI Gateway (sanitización, DLP, validación, hooks Zero Trust).
- Logs estructurados y forenses en WORM.
- Auditoría completa de cada interacción.

## 4. Ejemplo de Integración
```python
from core.contracts import AnomalyInput
from core.events import EventBus

input = AnomalyInput(ip="192.168.1.10", ...)
EventBus().publish("anomaly.detected", input.dict())
```

## 5. Extensión y Personalización
- Añade stages en `/pipeline/stages/` siguiendo los contratos y eventos.
- Usa hooks de AI Gateway para políticas personalizadas.

## 6. Soporte y Contacto
- Consulta `/docs/TECHNICAL_GUIDE.md` y los README de cada módulo.
- Contacta al equipo de desarrollo para soporte empresarial.

---

**Checklist de Integración**
- [ ] Cumplimiento de contratos
- [ ] Validación de eventos
- [ ] Seguridad y DLP activos
- [ ] Logs y auditoría habilitados
- [ ] Pruebas de integración superadas
