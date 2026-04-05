# Sección “AI Assistant” — Dashboard Táctico

## 1. Propósito de la integración
El AI Assistant en el Dashboard explica alertas, KPIs y estados, generando insights y resúmenes ejecutivos para el operador. No toma decisiones ni modifica datos en tiempo real.

## 2. Arquitectura de integración
- Punto de entrada: Llamada a `aiAssistant.recommendAction` o `analyzeWithLocalLLM` sobre alertas, KPIs o logs destacados.
- Flujo: Alerta/KPI → AI Assistant → Explicación/insight → Visualización en panel.
- Señales: alertas, KPIs, logs, eventos críticos.
- Genera: explicaciones, resúmenes, banners informativos.

## 3. Comportamiento
- Respuestas: explicaciones técnicas, resúmenes ejecutivos, insights tácticos.
- Estilo: claro, técnico, alineado a doctrina ARES‑11.
- Restricciones: nunca modifica datos ni toma decisiones.

## 4. Ejemplo de uso
- Caso normal: “El score de riesgo es bajo. No se requieren acciones.”
- Caso de riesgo: “Alerta crítica: score > 80. Sugerencia: escalar a SOC.”
- Caso de anomalía: “Panel sin datos. Explicación: posible desconexión de fuente.”
- Caso de remediación: “Acción ejecutada. Resumen IA: host aislado exitosamente.”

## 5. Integración con Dashboard
- Visualización de respuestas IA como tooltips, banners o secciones explicativas.
- Estado: “Explicación IA disponible” junto a cada alerta/KPI.

## 6. Integración doctrinal
- Rol: asistente de interpretación y explicación, nunca decisor.
- Ejemplo: “El AI Assistant explica, el operador decide.”

## 7. Requisitos previos
- Node.js >= 18, node-fetch, AI Assistant configurado.

## 8. Enlace
- [Índice Maestro](docs/manuales-operativos/index.md)
- [Integración AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)
