------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
Notifier (Notificaciones a Telegram)

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
Enviar alertas automáticas de hallazgos críticos o eventos relevantes a canales de comunicación instantánea como Telegram, permitiendo una respuesta inmediata del auditor.

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
- Componente principal: notify_telegram(message, bot_token, chat_id)
- Flujo de datos: Recibe mensaje, envía POST a API de Telegram
- Entradas: Mensaje, token de bot, chat_id
- Salidas: Notificación en Telegram
- Dependencias: requests, API Telegram
- Estándares: Notificación instantánea, integración con mensajería

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
- Parámetros: message (str), bot_token (str), chat_id (str/int)
- Entrada esperada: Texto de alerta
- Salida: Mensaje en canal/chat
- Comportamiento: Envía POST a Telegram
- Limitaciones: Requiere bot y chat_id válidos

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.notifier import notify_telegram
notify_telegram('Alerta crítica', 'BOT_TOKEN', 'CHAT_ID')

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
- Se conecta al pipeline de alertas y eventos críticos
- Puede ser invocado por el orquestador o el live monitor

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
Descubrimiento → Evaluación → Correlación → Alerta → Recomendación → Visualización

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
- CIS Controls: 16
- NIST 800‑53: IR-5
- MITRE ATT&CK: T1071 (defensivo)
- SABSA: Capa de Comunicación y Respuesta

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: notify_critical
  when: critical_finding_detected
  action: notify_telegram(message, bot_token, chat_id)

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
- Usar para alertar sobre hallazgos críticos o actividad sospechosa
- Proteger tokens y credenciales

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
- Mide: Número de alertas enviadas
- Indicadores: Tiempo de reacción, criticidad de eventos

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
Notifier permite a los equipos de auditoría recibir alertas críticas en tiempo real, mejorando la capacidad de respuesta y la coordinación ante incidentes de seguridad.

------------------------------------------------------------
