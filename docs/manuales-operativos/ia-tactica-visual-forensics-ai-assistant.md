# Sección “AI Assistant” — IA Táctica / Visual Forensics

## 1. Propósito de la integración
El AI Assistant complementa el análisis visual y forense, explicando hallazgos, generando narrativa y sugiriendo acciones, sin ejecutar ni modificar scripts de análisis.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre hallazgos visuales, OCR o acciones forenses.
- Flujo: Hallazgo/acción → AI Assistant → Explicación/narrativa → Operador/log.
- Señales: hallazgos visuales, OCR, acciones forenses.
- Genera: explicaciones, narrativa, sugerencias.

## 3. Comportamiento
- Respuestas: explicaciones, narrativa, sugerencias.
- Estilo: alineado a doctrina forense y visual.
- Restricciones: nunca ejecuta ni modifica scripts.

## 4. Ejemplo de uso
- Caso normal: “Hallazgo visual procesado. Explicación IA: sin riesgo.”
- Caso de riesgo: “OCR detecta texto sospechoso. Sugerencia IA: escalar a forense.”
- Caso de anomalía: “Sin señales IA. Explicación IA: posible error de modelo.”
- Caso de remediación: “Vacuna generada. Narrativa IA: acción preventiva.”

## 5. Integración con Dashboard
- Visualización de explicaciones IA junto a hallazgos y acciones visuales.

## 6. Integración doctrinal
- Rol: asistente de narrativa y explicación, nunca ejecutor.
- Ejemplo: “El AI Assistant narra, el operador decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](docs/manuales-operativos/index.md)
- [Integración AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)
