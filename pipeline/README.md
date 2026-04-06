# PIPELINE

## Descripción Técnica
Pipeline multi-stage, desacoplado, con stages de anomaly, correlation, ai_gateway, tactical_ai y execution. Orquestado por core.

## Responsabilidad
- Procesar datos en stages secuenciales
- Invocar lógica de análisis, correlación, AI y ejecución

## Entradas/Salidas
- Entradas: Datos de escaneo, contratos, eventos
- Salidas: Resultados de análisis, eventos, decisiones

## Contratos
- Consume y publica contratos de /core/contracts.py

## Eventos
- Emite y consume eventos de pipeline

## Dependencias
- core, domain, infrastructure

## Requisitos
- Python 3.10+, dependencias en requirements.txt

## Instalación
- Incluido en el repositorio principal

## Configuración
- Configuración de stages en /src/config/

## Ejecución
- Orquestado por core/orchestrator.py

## Integración
- Usar desde CLI, agents o API

## Errores Comunes
- Fallos de orquestación, eventos no consumidos

## Logs Esperados
- Logs de stages y eventos en /logs/

## Ejemplo de Uso
```python
from pipeline.stages.anomaly import detect_anomalies
result = detect_anomalies(data)
```

## Diagrama de Flujo
[![](../docs/diagrams/pipeline_flow.png)](../docs/diagrams/pipeline_flow.png)

## Checklist de Seguridad
- [x] Validación de entradas
- [x] Logs estructurados
- [x] Observabilidad
- [x] Contratos estrictos

---

# Pipeline de ARES-11

Cada etapa del pipeline es un módulo desacoplado, invocado por el orquestador. Implementa lógica de análisis, correlación, AI Gateway, IA táctica y ejecución.

Ubica la lógica de cada stage en `/pipeline/stages/<stage>/`.