------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
Live Monitor (Monitoreo en Tiempo Real)

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
Monitorear la red en tiempo real para detectar la aparición de nuevos dispositivos o intentos de escaneo, generando alertas inmediatas y mejorando la visibilidad táctica.

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
- Componente principal: live_monitor(network_range, bot_token, chat_id, interval)
- Flujo de datos: Escanea la red periódicamente, compara hosts, alerta por cambios
- Entradas: Rango de red, credenciales de notificación, intervalo
- Salidas: Alertas en consola y Telegram
- Dependencias: audit_ecosystem, notifier
- Estándares: Detección continua, respuesta inmediata

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
- Parámetros: network_range (str), bot_token (str), chat_id (str/int), interval (int)
- Entrada esperada: Rango de red válido
- Salida: Alertas en tiempo real
- Comportamiento: Loop de escaneo y alerta
- Limitaciones: Requiere permisos de escaneo y conectividad

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.live_monitor import live_monitor
live_monitor('192.168.1.0/24', 'BOT_TOKEN', 'CHAT_ID', 60)

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
- Se conecta al pipeline de escaneo y alertas
- Puede ser invocado como servicio o daemon

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
Descubrimiento → Live Monitor → Correlación → Alerta → Recomendación → Visualización

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
- CIS Controls: 1, 16
- NIST 800‑53: CA-7, IR-5
- MITRE ATT&CK: T1046 (defensivo)
- SABSA: Capa de Monitoreo y Respuesta

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: live_monitor_alert
  when: new_device_detected
  action: notify_telegram(msg, bot_token, chat_id)

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
- Usar en auditorías prolongadas o entornos críticos
- Ajustar el intervalo según la sensibilidad requerida

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
- Mide: Nuevos dispositivos detectados, frecuencia de cambios
- Indicadores: Tiempo de detección, volumen de alertas

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
Live Monitor dota a ARES‑11 de capacidades de vigilancia continua, permitiendo detectar y responder a cambios en la red en tiempo real, clave para la defensa proactiva.

------------------------------------------------------------
