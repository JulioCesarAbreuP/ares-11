------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
Shodan Check (Verificación de Exposición Pública)

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
Consultar la base de datos de Shodan para determinar si un dispositivo interno es visible desde Internet, alertando sobre exposición pública inadvertida.

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
- Componente principal: check_shodan(ip, api_key)
- Flujo de datos: Consulta API de Shodan, interpreta respuesta
- Entradas: IP, API Key
- Salidas: Booleano y alerta
- Dependencias: requests, API Shodan
- Estándares: Threat Intelligence, exposición externa

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
- Parámetros: ip (str), api_key (str)
- Entrada esperada: IP válida y API Key
- Salida: True/False y mensaje
- Comportamiento: Consulta Shodan y alerta si expuesto
- Limitaciones: Requiere API Key válida

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.shodan_check import check_shodan
is_exposed = check_shodan('8.8.8.8', 'API_KEY')

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
- Se conecta al pipeline de evaluación de exposición
- Puede ser invocado por el orquestador o dashboard

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
Descubrimiento → Evaluación → Shodan Check → Correlación → Recomendación → Visualización

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
- CIS Controls: 1, 14
- NIST 800‑53: CA-3, CA-7
- MITRE ATT&CK: T1595 (defensivo)
- SABSA: Capa de Exposición y Perímetro

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: shodan_exposure_alert
  when: new_device_detected
  action: check_shodan(ip, api_key)

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
- Usar para validar que activos internos no sean públicos
- Proteger la API Key

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
- Mide: Número de dispositivos expuestos
- Indicadores: Alertas de exposición pública

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
Shodan Check permite a ARES‑11 identificar activos internos expuestos en Internet, fortaleciendo la postura de seguridad y previniendo brechas por mala configuración.

------------------------------------------------------------
