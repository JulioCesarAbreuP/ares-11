# Sección “AI Assistant” — Vacunas / Enforcer

## 1. Propósito de la integración
El AI Assistant explica acciones de hardening, justifica recomendaciones y sugiere mejoras, sin ejecutar ni modificar scripts.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre acciones de hardening o alertas.
- Flujo: Acción/alerta → AI Assistant → Explicación/sugerencia → Operador/log.
- Señales: acciones, alertas, logs.
- Genera: explicaciones, sugerencias, narrativa de hardening.

## 3. Comportamiento
- Respuestas: explicaciones, sugerencias, narrativa técnica.
- Estilo: alineado a CIS/NIST/MITRE.
- Restricciones: nunca ejecuta ni modifica scripts.

## 4. Ejemplo de uso
- Caso normal: “Acción ejecutada. Explicación IA: host endurecido.”
- Caso de riesgo: “Compromiso detectado. Sugerencia IA: reforzar controles.”
- Caso de anomalía: “Acción fallida. Explicación IA: posible falta de permisos.”
- Caso de remediación: “Vacuna aplicada. Sugerencia IA: monitorear logs.”

## 5. Integración con Dashboard
- Visualización de explicaciones IA junto a acciones y alertas.

## 6. Integración doctrinal
- Rol: asistente de explicación, nunca ejecutor.
- Ejemplo: “El AI Assistant explica, el operador decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](docs/manuales-operativos/index.md)
- [Integración AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)
