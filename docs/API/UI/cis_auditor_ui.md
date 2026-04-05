====================================================================
1. CIS Auditor
====================================================================
Auditoría de controles CIS: visualiza el cumplimiento, brechas y recomendaciones en tiempo real.

====================================================================
2. Propósito de la Interfaz
====================================================================
- Visualizar señales de cumplimiento y brechas por control CIS (IG1/IG2/IG3).
- Mostrar controles evaluados, estado de cada uno y recomendaciones.
- Indicadores de riesgo asociados a cada brecha.
- Estado general del módulo y su integración con el dashboard táctico.

====================================================================
3. Diseño General de la UI
====================================================================
- Layout principal: panel central con resumen de cumplimiento, panel lateral con detalles por control.
- Secciones: resumen global, lista de controles, recomendaciones, alertas.
- Componentes clave: cards de controles, badges de estado, tabla de hallazgos, panel de recomendaciones.
- Jerarquía visual: primero el score global, luego detalles por control.
- Estilo: minimalista, táctico, empresarial.

====================================================================
4. Componentes Visuales
====================================================================
- Tarjetas de control (cards)
- Badges de cumplimiento/incumplimiento
- Gráficos de barras de cumplimiento
- Tabla de hallazgos por control
- Panel lateral de recomendaciones
- Alertas de criticidad

====================================================================
5. Flujo de Interacción
====================================================================
- Entrada: selección de activo o grupo → análisis automático
- Visualización: score global, lista de controles, detalles al hacer clic
- Recomendación: panel lateral muestra acciones sugeridas
- Estados: cumplimiento, brecha, criticidad
- Integración: datos se actualizan en tiempo real desde el motor

====================================================================
6. Integración con el Dashboard Táctico
====================================================================
- Señales de cumplimiento y brechas se envían al dashboard
- Representación en MITRE defensivo: controles mapeados a técnicas
- Contribuye al mapa táctico de riesgo y cumplimiento

====================================================================
7. Indicadores Clave (KPIs)
====================================================================
- % de controles cumplidos
- Número de brechas críticas
- Score global de cumplimiento
- Tendencia de cumplimiento (histórico)
- Visualización: gráficos, badges, tablas

====================================================================
8. Ejemplo de Pantalla
====================================================================
- Sección superior: score global y gráfico de barras
- Panel central: lista de controles con badges
- Panel lateral: recomendaciones y alertas
- Datos simulados: CIS-4.1 (No cumple), CIS-8.1 (Cumple)
- Estados: verde (cumple), rojo (no cumple), amarillo (parcial)

====================================================================
9. Estándares y Doctrina
====================================================================
- SABSA: alineación de controles a objetivos de negocio
- CIS Controls: IG1/IG2/IG3
- NIST 800-53: mapeo de controles
- MITRE ATT&CK (defensivo): correlación de técnicas
- Doctrina ARES-11: “No es un escáner. Es un motor de razonamiento de seguridad.”

====================================================================
10. Resumen Ejecutivo
====================================================================
La interfaz de CIS Auditor permite visualizar el estado de cumplimiento de controles críticos, identificar brechas y priorizar acciones, aportando transparencia y gobernanza a la auditoría táctica.