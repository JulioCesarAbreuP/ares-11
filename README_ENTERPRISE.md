# ARES-11 Enterprise Architecture

Esta versión reestructura el proyecto hacia una arquitectura enterprise real, desacoplando dominio, pipeline, infraestructura e interfaces. Consulta `/core/orchestrator.py` y `/core/contracts.py` para el nuevo pipeline y contratos estrictos.

## Estructura base
- `/core`: orquestador, contratos, event bus
- `/domain`: modelos, reglas, lógica de decisión y riesgo
- `/pipeline/stages`: stages desacoplados (anomaly, correlation, ai_gateway, tactical_ai, execution)
- `/infrastructure`: adaptadores externos (API, DB, colas, storage, seguridad)
- `/interfaces`: CLI, REST, agentes
- `/docs`: frontend (sin cambios)

**Siguiente paso:** migrar y refactorizar código existente a las nuevas capas según responsabilidad.
