# Sección “AI Assistant” — Telemetry Engine

## 1. Propósito de la integración
El AI Assistant resume anomalías, explica métricas y ayuda a interpretar eventos de telemetría, sin modificar datos ni ejecutar acciones.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre anomalías o métricas destacadas.
- Flujo: Anomalía/métrica → AI Assistant → Resumen/explicación → Operador/log.
- Señales: anomalías, métricas, eventos de salud.
- Genera: resúmenes, explicaciones, narrativa técnica.

## 3. Comportamiento
- Respuestas: resúmenes, explicaciones, narrativa técnica.
- Estilo: claro, técnico, alineado a doctrina ARES‑11.
- Restricciones: nunca modifica datos ni ejecuta acciones.

## 4. Ejemplo de uso
- Caso normal: “Latencia dentro de umbral. Explicación IA: operación normal.”
- Caso de riesgo: “Error crítico. Sugerencia IA: escalar a soporte.”
- Caso de anomalía: “Múltiples alertas. Resumen IA: posible ataque DDoS.”
- Caso de remediación: “Métrica corregida. Explicación IA: recurso restaurado.”

## 5. Integración con Dashboard
- Visualización de resúmenes IA junto a métricas y anomalías.

## 6. Integración doctrinal
- Rol: asistente de interpretación, nunca decisor.
- Ejemplo: “El AI Assistant resume, el operador decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](docs/manuales-operativos/index.md)
- [Integración AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)
