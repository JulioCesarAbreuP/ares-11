# Sección “AI Assistant” — Core (Orquestador Principal)

## 1. Propósito de la integración
El AI Assistant en el Core asiste en la interpretación de señales globales, explica decisiones de orquestación y ayuda en el onboarding doctrinal, sin tomar decisiones ni modificar el ciclo de vida de los módulos.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre señales, eventos críticos o logs de orquestación.
- Flujo: Señal/evento → AI Assistant → Explicación/sugerencia → Operador/log.
- Señales: señales globales, eventos críticos, logs.
- Genera: explicaciones, sugerencias, narrativa de orquestación.

## 3. Comportamiento
- Respuestas: explicaciones, sugerencias, narrativa doctrinal.
- Estilo: alineado a doctrina ARES‑11.
- Restricciones: nunca modifica el ciclo de vida ni ejecuta acciones.

## 4. Ejemplo de uso
- Caso normal: “Todos los módulos OK. Explicación IA: operación estable.”
- Caso de riesgo: “Módulo degradado. Sugerencia IA: revisar dependencias.”
- Caso de anomalía: “Reinicio automático. Explicación IA: política de resiliencia.”
- Caso de remediación: “Aislamiento ejecutado. Narrativa IA: riesgo mitigado.”

## 5. Integración con Dashboard
- Visualización de explicaciones IA junto a señales y logs globales.

## 6. Integración doctrinal
- Rol: asistente de interpretación, nunca decisor.
- Ejemplo: “El AI Assistant interpreta, el Core ejecuta.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](../index.md)
- [Manual Core](manual_core.md)
- [Integración AI Assistant](../integracion-ai-assistant.md)
