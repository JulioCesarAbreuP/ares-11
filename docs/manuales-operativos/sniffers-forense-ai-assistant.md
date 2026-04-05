# Sección “AI Assistant” — Sniffers / Forense Defensivo

## 1. Propósito de la integración
El AI Assistant genera narrativa defensiva, explica hallazgos forenses y sugiere acciones, sin ejecutar ni modificar evidencia.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre hallazgos o reportes forenses.
- Flujo: Hallazgo/reporte → AI Assistant → Narrativa/sugerencia → Operador/log.
- Señales: hallazgos, reportes, evidencia.
- Genera: narrativa, explicaciones, sugerencias.

## 3. Comportamiento
- Respuestas: narrativa defensiva, explicaciones, sugerencias.
- Estilo: técnico, alineado a doctrina forense.
- Restricciones: nunca modifica evidencia ni ejecuta acciones.

## 4. Ejemplo de uso
- Caso normal: “Captura pasiva sin alertas. Narrativa IA: operación normal.”
- Caso de riesgo: “MAC spoofing detectado. Sugerencia IA: aislar host.”
- Caso de anomalía: “Sensor sin datos. Explicación IA: posible desconexión.”
- Caso de remediación: “Vacuna ejecutada. Narrativa IA: host protegido.”

## 5. Integración con Dashboard
- Visualización de narrativa IA junto a hallazgos y reportes.

## 6. Integración doctrinal
- Rol: asistente de narrativa, nunca ejecutor.
- Ejemplo: “El AI Assistant narra, el operador decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](docs/manuales-operativos/index.md)
- [Integración AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)
