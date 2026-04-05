====================================================================
1. Exporter
====================================================================
Exportador de hallazgos: permite exportar resultados y rutas de ataque a CSV/Excel para análisis y reporte externo.

====================================================================
2. Propósito de la Interfaz
====================================================================
- Visualizar señales de exportación y estado de los reportes.
- Mostrar controles evaluados y hallazgos exportados.
- Indicadores de éxito de exportación y cobertura.
- Estado del módulo y su integración con el dashboard táctico.

====================================================================
3. Diseño General de la UI
====================================================================
- Layout principal: panel de exportación, sección de hallazgos, panel de estado.
- Secciones: lista de hallazgos, exportaciones recientes, estado de exportación.
- Componentes clave: cards de hallazgos, badges de exportación, tabla de reportes, panel de estado.
- Jerarquía visual: primero el estado de exportación, luego detalles de hallazgos.
- Estilo: minimalista, táctico, empresarial.

====================================================================
4. Componentes Visuales
====================================================================
- Tarjetas de hallazgos (cards)
- Badges de exportación
- Tabla de reportes exportados
- Panel lateral de estado
- Alertas de éxito/error

====================================================================
5. Flujo de Interacción
====================================================================
- Entrada: selección de hallazgos → exportación automática
- Visualización: lista de reportes exportados, detalles al hacer clic
- Recomendación: panel lateral muestra estado y alertas
- Estados: exportado, pendiente, error
- Integración: datos se actualizan en tiempo real desde el motor

====================================================================
6. Integración con el Dashboard Táctico
====================================================================
- Señales de exportación y cobertura se envían al dashboard
- Representación en MITRE defensivo: cobertura de hallazgos exportados
- Contribuye al mapa táctico de reporte y cobertura

====================================================================
7. Indicadores Clave (KPIs)
====================================================================
- Número de hallazgos exportados
- Número de reportes generados
- Tasa de éxito de exportación
- Visualización: gráficos, badges, tablas

====================================================================
8. Ejemplo de Pantalla
====================================================================
- Sección superior: estado de exportación y gráfico de cobertura
- Panel central: lista de hallazgos y reportes
- Panel lateral: estado y alertas
- Datos simulados: 10 hallazgos exportados, 2 errores
- Estados: verde (exportado), amarillo (pendiente), rojo (error)

====================================================================
9. Estándares y Doctrina
====================================================================
- SABSA: alineación de exportación a objetivos de negocio
- CIS Controls: reporte de hallazgos
- NIST 800-53: mapeo de cobertura
- MITRE ATT&CK (defensivo): correlación de hallazgos
- Doctrina ARES-11: “No es un escáner. Es un motor de razonamiento de seguridad.”

====================================================================
10. Resumen Ejecutivo
====================================================================
La interfaz de Exporter permite exportar hallazgos y rutas de ataque, facilitando el análisis externo y la colaboración en la auditoría táctica.