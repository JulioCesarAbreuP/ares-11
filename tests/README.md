# Pruebas Automáticas de ARES-11

Estructura de carpetas:
- /tests/core
- /tests/domain
- /tests/pipeline/stages
- /tests/infrastructure
- /tests/interfaces

Cada carpeta contiene:
- test_unit.py: pruebas unitarias
- test_integration.py: pruebas de integración
- test_resilience.py: pruebas de resiliencia (retries, fallbacks)
- test_sanitization.py: pruebas de sanitización
- test_contracts.py: validación de contratos
- test_logs.py: logs estructurados
- test_e2e.py: flujo end-to-end

Ejecuta todas las pruebas con:
```bash
pytest tests/
```

---

# TESTS

## Descripción Técnica
Suite de pruebas automáticas por capa: core, domain, pipeline, infrastructure, interfaces, integración y UI. Incluye unitarias, integración, resiliencia, sanitización, validación de contratos, logs y end-to-end.

## Estructura
- /core: Pruebas de contratos, eventos, utilidades
- /domain: Motores de decisión y riesgo
- /pipeline: Stages y orquestación
- /infrastructure: Almacenamiento, notificaciones, forensics
- /interfaces: CLI, API, agents
- /integration: Pruebas de integración entre capas
- /ui: Pruebas de interfaces web

## Tipos de Pruebas
- Unitarias
- Integración
- Resiliencia y fallos
- Sanitización y validación
- Logs y observabilidad
- End-to-end

## Ejecución
- `pytest tests/` o `python -m unittest discover tests/`

## Ejemplo de Prueba
```python
from core.contracts import SomeContract

def test_contract_validation():
    obj = SomeContract(field="valor")
    assert obj.field == "valor"
```

## Checklist de Calidad
- [x] Cobertura mínima 80%
- [x] Pruebas de contratos y eventos
- [x] Pruebas de resiliencia y sanitización
- [x] Pruebas de logs y observabilidad