------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
Whitelist (Lista Blanca de Dispositivos)

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
Permitir marcar dispositivos confiables para evitar falsos positivos y reducir el ruido en los hallazgos, adaptando la auditoría al contexto real del cliente.

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
- Componentes: add_to_whitelist(ip), is_whitelisted(ip)
- Flujo de datos: Lee y escribe en un archivo JSON de whitelist
- Entradas: IP de dispositivo
- Salidas: Confirmación de whitelist o validación
- Dependencias: JSON, almacenamiento local
- Estándares: Personalización, reducción de alertas

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
- Parámetros: ip (str)
- Entrada esperada: IP válida
- Salida: Confirmación o booleano
- Comportamiento: Añade o verifica IP en la whitelist
- Limitaciones: Solo IPs, no atributos avanzados

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.whitelist import add_to_whitelist, is_whitelisted
add_to_whitelist('192.168.1.10')
if is_whitelisted('192.168.1.10'):
    print('Dispositivo confiable')

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
- Se conecta al pipeline de hallazgos y filtrado
- Permite personalizar la auditoría según el entorno

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
Descubrimiento → Evaluación → Whitelist → Correlación → Recomendación → Visualización

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
- CIS Controls: 8, 16
- NIST 800‑53: SI-4
- MITRE ATT&CK: T1078 (defensivo)
- SABSA: Capa de Personalización y Contexto

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: filter_whitelisted
  when: finding_detected
  action: if not is_whitelisted(ip): process_finding()

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
- Mantener la whitelist actualizada
- Revisar periódicamente para evitar omisiones

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
- Mide: Número de dispositivos en whitelist
- Indicadores: Reducción de falsos positivos

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
El módulo Whitelist de ARES‑11 permite adaptar la auditoría a la realidad del cliente, reduciendo alertas innecesarias y enfocando los esfuerzos en riesgos reales.

------------------------------------------------------------
