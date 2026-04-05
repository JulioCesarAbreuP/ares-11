# Sección “AI Assistant” — Remediation Engine

## 1. Propósito de la integración
El AI Assistant en Remediation Engine sugiere recomendaciones defensivas y explica el razonamiento detrás de cada acción propuesta. No ejecuta acciones críticas ni reemplaza la lógica de decisión del motor de remediación.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.recommendAction(evento)` al recibir una alerta o señal de riesgo.
- Flujo: Evento → AI Assistant → Sugerencia/explicación → Operador/registro.
- Señales: alertas, eventos de riesgo, logs de acciones.
- Genera: recomendaciones, justificaciones, narrativa defensiva.

## 3. Comportamiento
- Respuestas: sugerencias defensivas, explicaciones técnicas, justificaciones doctrinales.
- Estilo: técnico, táctico, alineado a CIS/NIST/MITRE.
- Restricciones: nunca ejecuta acciones, solo recomienda.

## 4. Ejemplo de uso
- Caso normal: “Se recomienda bloquear el host por T1021. Justificación: lateral movement detectado.”
- Caso de riesgo: “Aislamiento sugerido por score alto. Revisar logs antes de ejecutar.”
- Caso de anomalía: “Acción fallida, sugerencia: reintentar y validar integridad.”
- Caso de remediación: “Aplicar hardening IG2. Explicación: exposición a CVE-2023-12345.”

## 5. Integración con Dashboard
- Visualización de sugerencias IA en panel de acciones.
- Tooltips explicativos en logs y alertas.

## 6. Integración doctrinal
- Rol: asistente de recomendaciones, nunca decisor.
- Ejemplo: “El AI Assistant sugiere, el motor de remediación decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](../index.md)
- [Manual Remediation](manual_remediation.md)
- [Integración AI Assistant](../integracion-ai-assistant.md)
