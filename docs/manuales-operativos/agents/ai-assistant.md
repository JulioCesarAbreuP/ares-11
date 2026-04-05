# Sección “AI Assistant” — Agentes Distribuidos

## 1. Propósito de la integración
El AI Assistant ayuda a interpretar señales y eventos detectados por los agentes, sugiriendo explicaciones y acciones recomendadas, sin ejecutar ni modificar acciones locales.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.recommendAction` sobre señales/eventos relevantes.
- Flujo: Señal/evento → AI Assistant → Explicación/sugerencia → Operador/log.
- Señales: señales, eventos, logs de agente.
- Genera: explicaciones, sugerencias, narrativa técnica.

## 3. Comportamiento
- Respuestas: explicaciones, sugerencias, narrativa técnica.
- Estilo: claro, técnico, alineado a doctrina ARES‑11.
- Restricciones: nunca ejecuta acciones en el host.

## 4. Ejemplo de uso
- Caso normal: “Señal recibida: actividad normal.”
- Caso de riesgo: “Actividad sospechosa. Sugerencia: escalar a Core.”
- Caso de anomalía: “Error de comunicación. Explicación IA: posible pérdida de red.”
- Caso de remediación: “Acción ejecutada. Sugerencia IA: validar integridad.”

## 5. Integración con Dashboard
- Visualización de explicaciones IA junto a señales y logs de agentes.

## 6. Integración doctrinal
- Rol: asistente de interpretación, nunca ejecutor.
- Ejemplo: “El AI Assistant interpreta, el agente ejecuta.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](../index.md)
- [Manual Agentes](manual_agents.md)
- [Integración AI Assistant](../integracion-ai-assistant.md)
