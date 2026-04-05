====================================================================
1. Shodan Check
====================================================================
Verificador de exposición pública: visualiza dispositivos internos expuestos en Internet y alerta sobre riesgos de visibilidad.

====================================================================
2. Propósito de la Interfaz
====================================================================
- Visualizar señales de exposición pública y alertas de riesgo.
- Mostrar controles evaluados y dispositivos expuestos.
- Indicadores de criticidad y visibilidad externa.
- Estado del módulo y su integración con el dashboard táctico.

====================================================================
3. Diseño General de la UI
====================================================================
- Layout principal: panel de dispositivos expuestos, sección de alertas, panel de criticidad.
- Secciones: lista de dispositivos, alertas recientes, criticidad de exposición.
- Componentes clave: cards de dispositivos, badges de exposición, tabla de alertas, panel de criticidad.
- Jerarquía visual: primero dispositivos expuestos, luego alertas y criticidad.
- Estilo: minimalista, táctico, empresarial.

====================================================================
4. Componentes Visuales
====================================================================
- Tarjetas de dispositivos (cards)
- Badges de exposición
- Tabla de alertas
- Panel lateral de criticidad
- Alertas de visibilidad

====================================================================
5. Flujo de Interacción
====================================================================
- Entrada: análisis automático de dispositivos
- Visualización: lista de dispositivos expuestos, detalles al hacer clic
- Recomendación: panel lateral muestra criticidad y alertas
- Estados: expuesto, no expuesto, alerta crítica
- Integración: datos se actualizan en tiempo real desde el motor

====================================================================
6. Integración con el Dashboard Táctico
====================================================================
- Señales de exposición y criticidad se envían al dashboard
- Representación en MITRE defensivo: exposición mapeada a técnicas
- Contribuye al mapa táctico de visibilidad y riesgo

====================================================================
7. Indicadores Clave (KPIs)
====================================================================
- Número de dispositivos expuestos
- Severidad de exposición
- Tasa de remediación
- Visualización: gráficos, badges, tablas

====================================================================
8. Ejemplo de Pantalla
====================================================================
- Sección superior: lista de dispositivos expuestos y gráfico de criticidad
- Panel central: alertas y criticidad
- Panel lateral: visibilidad y alertas
- Datos simulados: 2 dispositivos expuestos, 1 alerta crítica
- Estados: rojo (expuesto), verde (no expuesto), amarillo (alerta)

====================================================================
9. Estándares y Doctrina
====================================================================
- SABSA: alineación de visibilidad a objetivos de negocio
- CIS Controls: control de exposición
- NIST 800-53: mapeo de visibilidad
- MITRE ATT&CK (defensivo): correlación de exposición
- Doctrina ARES-11: “No es un escáner. Es un motor de razonamiento de seguridad.”

====================================================================
10. Resumen Ejecutivo
====================================================================
La interfaz de Shodan Check permite identificar dispositivos expuestos, alertar sobre riesgos de visibilidad y mejorar la postura defensiva táctica.