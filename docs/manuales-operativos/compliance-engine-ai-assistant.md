# Sección “AI Assistant” — Compliance Engine

## 1. Propósito de la integración
El AI Assistant explica controles, hallazgos y recomendaciones de cumplimiento, ayudando al operador a entender el estado y sugerir mejoras, sin modificar controles ni ejecutar acciones.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre hallazgos o controles fallidos.
- Flujo: Hallazgo/control → AI Assistant → Explicación/sugerencia → Operador/log.
- Señales: hallazgos, controles, reportes.
- Genera: explicaciones, sugerencias, narrativa de cumplimiento.

## 3. Comportamiento
- Respuestas: explicaciones, sugerencias, narrativa doctrinal.
- Estilo: alineado a CIS/NIST/MITRE.
- Restricciones: nunca modifica controles ni ejecuta acciones.

## 4. Ejemplo de uso
- Caso normal: “Control CIS 6.1 cumplido. Explicación IA: autenticación robusta.”
- Caso de riesgo: “Incumplimiento crítico. Sugerencia IA: reforzar monitoreo.”
- Caso de anomalía: “Evidencia insuficiente. Explicación IA: revisar fuentes.”
- Caso de remediación: “Control corregido. Sugerencia IA: documentar cambio.”

## 5. Integración con Dashboard
- Visualización de explicaciones IA junto a hallazgos y controles.

## 6. Integración doctrinal
- Rol: asistente de explicación, nunca decisor.
- Ejemplo: “El AI Assistant explica, el operador decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](docs/manuales-operativos/index.md)
- [Integración AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)
