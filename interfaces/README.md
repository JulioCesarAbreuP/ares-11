# INTERFACES

## Descripción Técnica
CLI, API REST y agentes externos. Exponen servicios y puntos de integración, sin lógica de negocio.

## Responsabilidad
- Exponer CLI, API REST, agentes y automatizaciones

## Entradas/Salidas
- Entradas: Comandos, peticiones, eventos
- Salidas: Respuestas, logs, eventos

## Contratos
- Consume contratos de /core/contracts.py

## Eventos
- Emite eventos de integración y automatización

## Dependencias
- click, fastapi, core

## Requisitos
- Python 3.10+, dependencias en requirements.txt

## Instalación
- Incluido en el repositorio principal

## Configuración
- Variables en /src/config/

## Ejecución
- CLI: `python interfaces/cli/ares11.py`
- API: `uvicorn interfaces/rest/api:app`

## Integración
- Usar desde sistemas externos, SIEM, EDR, colas

## Errores Comunes
- Argumentos inválidos, errores de red

## Logs Esperados
- Logs de CLI y API en /logs/

## Ejemplo de Uso
```bash
python interfaces/cli/ares11.py scan --target 192.168.1.1
```

## Diagrama de Flujo
[![](../docs/diagrams/interfaces_flow.png)](../docs/diagrams/interfaces_flow.png)

## Checklist de Seguridad
- [x] Validación de entradas
- [x] Logs estructurados
- [x] Observabilidad
- [x] Contratos estrictos

---

# Interfaces de ARES-11

CLI, API REST y agentes externos. Solo exponen servicios, no contienen lógica de negocio.