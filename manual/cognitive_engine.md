# Manual de Cognitive Engine

**Propósito:** Motor de razonamiento, correlación, scoring y simulación ofensiva/defensiva.

## Uso
- Se inicializa con `NewEngine(config)` y se ejecuta con `Start()`.
- Procesa señales de agentes, core, API y RRSS.

## Funciones principales
- `ProcessSignal(signal)`: Analiza y correlaciona señales.
- `analyzeWithAI(signal)`: Scoring y correlación IA.
- `defensiveActions(signal)`: Respuesta defensiva.
- `offensiveSimulation(signal)`: Simulación ofensiva.
- `rrssCorrelation(signal)`: Correlación con señales de redes sociales.

## Integración
- Orquestador, agentes, dashboard, API, remediation.
