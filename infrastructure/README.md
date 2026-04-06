# INFRASTRUCTURE

## Descripción Técnica
Adaptadores para APIs externas, almacenamiento, WORM, forensics, notificaciones y seguridad. Sin lógica de negocio.

## Responsabilidad
- Persistencia, almacenamiento, notificaciones, integración externa

## Entradas/Salidas
- Entradas: Datos de pipeline/domain, contratos
- Salidas: Persistencia, notificaciones, logs

## Contratos
- Consume contratos de /core/contracts.py

## Eventos
- Emite eventos de almacenamiento, notificación, forensics

## Dependencias
- requests, fpdf, chromadb, core

## Requisitos
- Python 3.10+, dependencias en requirements.txt

## Instalación
- Incluido en el repositorio principal

## Configuración
- Variables en /src/config/

## Ejecución
- Usar desde domain, pipeline o interfaces

## Integración
- API REST, SIEM, colas, almacenamiento externo

## Errores Comunes
- Fallos de red, permisos de escritura

## Logs Esperados
- Logs de almacenamiento y notificaciones en /logs/

## Ejemplo de Uso
```python
from infrastructure.storage.forensics_packager import package_forensics
```

## Diagrama de Flujo
[![](../docs/diagrams/infrastructure_flow.png)](../docs/diagrams/infrastructure_flow.png)

## Checklist de Seguridad
- [x] Validación de entradas
- [x] Logs estructurados
- [x] DLP/WORM hooks
- [x] Observabilidad

---

# Infraestructura de ARES-11

Adaptadores para APIs externas, base de datos, colas, almacenamiento y seguridad. No debe contener lógica de negocio.