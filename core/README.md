# CORE

## Descripción Técnica
Núcleo de contratos, eventos, utilidades, resiliencia, logs y seguridad. Centraliza validación, observabilidad y patrones enterprise.

## Responsabilidad
- Definir contratos y eventos
- Proveer utilidades de logging, trazas, retries, circuit breakers, sanitización, DLP/WORM

## Entradas/Salidas
- Entradas: Datos de módulos, eventos, contratos
- Salidas: Logs, eventos, contratos validados

## Contratos
- /core/contracts.py: Todos los modelos de datos
- /core/events.py: Definición de eventos

## Eventos
- Emite y consume eventos de arquitectura

## Dependencias
- Pydantic, logging, typing

## Requisitos
- Python 3.10+, dependencias en requirements.txt

## Instalación
- Incluido en el repositorio principal

## Configuración
- No requiere configuración adicional

## Ejecución
- Importar utilidades y contratos desde otros módulos

## Integración
- Usar contratos y eventos en todos los módulos

## Errores Comunes
- Importaciones cruzadas, validación fallida

## Logs Esperados
- Logs estructurados en /logs/

## Ejemplo de Uso
```python
from core.contracts import SomeContract
from core.utils import log_event
```

## Diagrama de Flujo
[![](../docs/diagrams/core_flow.png)](../docs/diagrams/core_flow.png)

## Checklist de Seguridad
- [x] Validación estricta de contratos
- [x] Sanitización de entradas
- [x] Logs estructurados
- [x] Observabilidad
- [x] DLP/WORM hooks

---

# Núcleo de ARES-11

Contiene el orquestador explícito, contratos estrictos y event bus para desacoplar etapas del pipeline.

- `orchestrator.py`: define el pipeline y la secuencia de stages.
- `contracts.py`: contratos de datos (Pydantic).
- `events.py`: event bus mínimo para comunicación interna.
