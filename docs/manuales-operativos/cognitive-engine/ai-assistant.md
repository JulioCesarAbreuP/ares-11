# Sección “AI Assistant” — Cognitive Engine

## 1. Propósito de la integración
El AI Assistant en Cognitive Engine aporta razonamiento explicativo y justificaciones doctrinales para correlaciones y alertas, sin tomar decisiones ni modificar reglas.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.analyzeWithLocalLLM` sobre correlaciones, scores o simulaciones.
- Flujo: Correlación/score → AI Assistant → Justificación/explicación → Registro o panel.
- Señales: correlaciones, scores, simulaciones, alertas.
- Genera: explicaciones, justificaciones, narrativa doctrinal.

## 3. Comportamiento
- Respuestas: justificaciones, explicaciones, narrativa técnica.
- Estilo: doctrinal, técnico, alineado a MITRE/NIST.
- Restricciones: nunca modifica reglas ni toma decisiones.

## 4. Ejemplo de uso
- Caso normal: “Score bajo, correlación válida. Explicación: actividad normal.”
- Caso de riesgo: “Score alto, justificación: múltiples técnicas T1059 detectadas.”
- Caso de anomalía: “Simulación sin resultado. Sugerencia: revisar entradas.”
- Caso de remediación: “Alerta generada. Explicación IA: riesgo crítico.”

## 5. Integración con Dashboard
- Visualización de justificaciones IA junto a correlaciones y scores.

## 6. Integración doctrinal
- Rol: asistente de explicación, nunca decisor.
- Ejemplo: “El AI Assistant justifica, el motor decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](../index.md)
- [Manual Cognitive Engine](manual_cognitive_engine.md)
- [Integración AI Assistant](../integracion-ai-assistant.md)
