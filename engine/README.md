# ENGINE

## Descripción Técnica
Módulos de análisis, correlación, forensics, remediación, inteligencia, visualización y utilidades avanzadas. Cada archivo implementa una función o clase autocontenida.

## Responsabilidad
- Proveer funciones de análisis, correlación, forensics, remediación, inteligencia, visualización y utilidades

## Entradas/Salidas
- Entradas: Datos de pipeline/domain, contratos
- Salidas: Resultados, logs, eventos

## Contratos
- Consume contratos de /core/contracts.py

## Eventos
- Emite eventos de análisis, forensics, remediación

## Dependencias
- requests, fpdf, chromadb, core

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
- Fallos de red, permisos de escritura, dependencias faltantes

## Logs Esperados
- Logs de análisis y forensics en /logs/

## Ejemplo de Uso
```python
from engine.visual_forensics import capture_remote_screen
```

## Diagrama de Flujo
[![](../docs/diagrams/engine_flow.png)](../docs/diagrams/engine_flow.png)

## Checklist de Seguridad
- [x] Validación de entradas
- [x] Logs estructurados
- [x] Observabilidad
- [x] Contratos estrictos
