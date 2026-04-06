# Agentes de ARES-11

Responsabilidad: Consumir eventos y ejecutar lógica especializada (anomalía, correlación, automatización, etc). Publican eventos y usan contratos estrictos.

- `anomaly_agent.py`: agente de análisis de anomalías
- Entrada: eventos de ingestión
- Salida: eventos de anomalía
- Relación: Consume y publica eventos vía `/core/events.py`
