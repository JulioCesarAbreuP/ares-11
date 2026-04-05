====================================================================
1. Live Monitor
====================================================================
Monitor en tiempo real: visualiza la aparición de nuevos dispositivos y eventos de escaneo en la red.

====================================================================
2. Propósito de la Interfaz
====================================================================
- Visualizar señales de monitoreo y eventos en tiempo real.
- Mostrar controles evaluados y alertas generadas.
- Indicadores de nuevos dispositivos y actividad sospechosa.
- Estado del módulo y su integración con el dashboard táctico.

====================================================================
3. Diseño General de la UI
====================================================================
- Layout principal: panel de eventos, sección de dispositivos, panel de alertas.
- Secciones: lista de eventos, dispositivos detectados, alertas recientes.
- Componentes clave: cards de eventos, badges de actividad, tabla de dispositivos, panel de alertas.
- Jerarquía visual: primero eventos críticos, luego dispositivos y alertas.
- Estilo: minimalista, táctico, empresarial.

====================================================================
4. Componentes Visuales
====================================================================
- Tarjetas de eventos (cards)
- Badges de actividad
- Tabla de dispositivos detectados
- Panel lateral de alertas
- Alertas de actividad sospechosa

====================================================================
5. Flujo de Interacción
====================================================================
- Entrada: monitoreo automático de la red
- Visualización: lista de eventos, detalles al hacer clic
- Recomendación: panel lateral muestra alertas y recomendaciones
- Estados: nuevo dispositivo, escaneo detectado, alerta crítica
- Integración: datos se actualizan en tiempo real desde el motor

====================================================================
6. Integración con el Dashboard Táctico
====================================================================
- Señales de eventos y dispositivos se envían al dashboard
- Representación en MITRE defensivo: eventos mapeados a técnicas
- Contribuye al mapa táctico de monitoreo y visibilidad

====================================================================
7. Indicadores Clave (KPIs)
====================================================================
- Número de eventos detectados
- Número de dispositivos nuevos
- Tiempo de detección
- Visualización: gráficos, badges, tablas

====================================================================
8. Ejemplo de Pantalla
====================================================================
- Sección superior: lista de eventos y gráfico de actividad
- Panel central: dispositivos detectados y alertas
- Panel lateral: recomendaciones y alertas
- Datos simulados: 3 eventos críticos, 2 dispositivos nuevos
- Estados: azul (nuevo), rojo (crítico), amarillo (alerta)

====================================================================
9. Estándares y Doctrina
====================================================================
- SABSA: alineación de monitoreo a objetivos de negocio
- CIS Controls: monitoreo continuo
- NIST 800-53: mapeo de eventos
- MITRE ATT&CK (defensivo): correlación de eventos
- Doctrina ARES-11: “No es un escáner. Es un motor de razonamiento de seguridad.”

====================================================================
10. Resumen Ejecutivo
====================================================================
La interfaz de Live Monitor permite monitorear la red en tiempo real, detectar eventos críticos y mejorar la visibilidad táctica.