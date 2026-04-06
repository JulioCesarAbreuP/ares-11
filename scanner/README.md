# SCANNER

## Descripción Técnica
Módulos de escaneo de red, hardware, firmware, VLAN, SNMP, ARP, LLDP y passive intel. Cada archivo implementa una función de escaneo autocontenida.

## Responsabilidad
- Proveer funciones de escaneo y recolección de datos de red y hardware

## Entradas/Salidas
- Entradas: Parámetros de red, contratos
- Salidas: Resultados de escaneo, logs, eventos

## Contratos
- Consume contratos de /core/contracts.py

## Eventos
- Emite eventos de escaneo

## Dependencias
- scapy, core

## Requisitos
- Python 3.10+, dependencias en requirements.txt

## Instalación
- Incluido en el repositorio principal

## Configuración
- Variables en /src/config/

## Ejecución
- Importar funciones desde pipeline, domain o interfaces

## Integración
- Usar desde pipeline, domain o interfaces

## Errores Comunes
- Permisos insuficientes, dependencias faltantes

## Logs Esperados
- Logs de escaneo en /logs/

## Ejemplo de Uso
```python
from scanner.arp_inspection import test_arp_spoofing
```

## Diagrama de Flujo
[![](../docs/diagrams/scanner_flow.png)](../docs/diagrams/scanner_flow.png)

## Checklist de Seguridad
- [x] Validación de entradas
- [x] Logs estructurados
- [x] Observabilidad
- [x] Contratos estrictos
