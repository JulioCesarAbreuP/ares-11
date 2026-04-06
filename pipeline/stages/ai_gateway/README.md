# AI Gateway Stage

## Descripción
Stage formal del pipeline para validación, DLP, sanitización, redacción y auditoría avanzada de señales antes de correlación.

## Responsabilidad
- Sanitización profunda de inputs
- Validación estricta de contratos
- Detección de prompt injection
- Detección y bloqueo de fuga de datos (DLP)
- Redacción automática de datos sensibles
- Políticas de seguridad configurables
- Hooks para Zero Trust
- Integración con WORM Logger y Forensics Packager
- Reglas de bloqueo y cuarentena
- Auditoría completa de cada interacción

## Entradas/Salidas
- Entrada: `SignalIngest` (contrato tipado)
- Salida: `SignalValidated` (contrato tipado)

## Logs y Trazabilidad
- Logs estructurados en cada paso
- Trazabilidad completa de decisiones y bloqueos

## Extensión
- Punto de extensión para modelos de validación futuros

## Ejemplo de Uso
```python
from pipeline.stages.ai_gateway.gateway import ai_gateway_stage
from core.contracts import SignalIngest

signal = SignalIngest(source="sensor1", data="user: john.doe@example.com")
validated = ai_gateway_stage(signal)
```
