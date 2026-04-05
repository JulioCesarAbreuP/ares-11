# Integración del AI Assistant en el Ecosistema ARES‑11

---

## 1. Propósito de la integración
El AI Assistant aporta razonamiento explicativo, recomendaciones y narrativa técnica a cada flujo de ARES‑11, sin reemplazar la lógica decisoria ni la autoridad del motor cognitivo. Complementa la toma de decisiones con explicaciones, insights y sugerencias, pero no ejecuta acciones críticas sin validación humana o del motor doctrinal.

**NO debe:**
- Tomar decisiones finales de remediación o aislamiento
- Modificar controles sin validación
- Reemplazar la lógica de correlación o scoring

**Complementa:**
- Motor cognitivo: aporta explicaciones, resúmenes y justificaciones
- Operador: asiste en interpretación, onboarding y documentación

---

## 2. Arquitectura de integración
- **Punto de entrada:** Llamadas a `aiAssistant.recommendAction`, `analyzeWithLocalLLM` o `analyzeWithAzureOpenAI` desde cada módulo
- **Flujo de datos:**
  - Módulo genera evento/señal → AI Assistant analiza → Respuesta enriquecida → Visualización/registro
- **Señales que consume:** eventos, logs, alertas, controles, anomalías
- **Señales que genera:** recomendaciones, explicaciones, resúmenes, narrativa
- **Interacción:**
  - Remediation: sugiere acciones defensivas
  - Dashboard: explica KPIs y alertas
  - Cognitive Engine: justifica correlaciones
  - Agentes: interpreta señales
  - Compliance: explica controles
  - Telemetry: resume anomalías
  - Forense: narrativa defensiva
  - Vacunas: explica hardening
  - Portada: onboarding y ayuda

---

## 3. Comportamiento del AI Assistant
- **Respuestas permitidas:** explicaciones, recomendaciones, resúmenes, narrativa técnica
- **Estilo:** técnico, táctico, empresarial, alineado a doctrina ARES‑11
- **Restricciones:** no ejecutar acciones críticas, no modificar reglas, no tomar decisiones finales
- **Ejemplo:**
  - “Se recomienda aislar el host por lateral movement. Justificación: T1021 detectado, riesgo alto.”
  - “El control CIS 6.1 se cumple parcialmente. Sugerencia: reforzar autenticación.”

---

## 4. Ejemplo de uso dentro del módulo
- **Caso normal:**
  - Remediation llama a `aiAssistant.recommendAction(evento)` para sugerir respuesta
- **Caso de riesgo:**
  - Dashboard muestra explicación IA de alerta crítica
- **Caso de anomalía:**
  - Telemetry Engine solicita resumen IA de anomalías recientes
- **Caso de remediación:**
  - Compliance Engine pide explicación de control fallido

---

## 5. Integración con el Dashboard
- Visualización de respuestas IA en paneles de alertas, KPIs y explicaciones
- Respuestas IA se muestran como tooltips, banners o secciones explicativas
- Integración con estados: “Explicación IA disponible”

---

## 6. Integración con la Documentación Doctrinal
Cada manual operativo incluye sección “AI Assistant”:
- Rol del asistente en el módulo
- Ejemplos doctrinales de interacción
- Limitaciones y buenas prácticas

---

## 7. Requisitos previos
- Node.js >= 18
- Paquete `node-fetch`
- Ollama/LM Studio local (opcional: Azure OpenAI)
- Configuración de endpoints y claves API

---

## 8. Enlace al Index Maestro
- Entrada en menú hamburguesa: “AI Assistant (IA Local/Online)”
- Enlace desde `/docs/manuales-operativos/index.md`
- Enlace sugerido desde portada principal

---

> **Nota:** La integración es extensible a nuevos módulos y flujos siguiendo este patrón doctrinal.
