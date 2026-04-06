# DOMAIN

## Descripción Técnica
Lógica de negocio, motores de decisión, reglas, memoria táctica y reputación de dispositivos. Implementa lógica desacoplada y patrones enterprise.

## Responsabilidad
- Motores de decisión y riesgo
- Reglas y lógica de negocio
- Memoria táctica y reputación

## Entradas/Salidas
- Entradas: Datos de pipeline, contratos, eventos
- Salidas: Decisiones, riesgos, eventos

## Contratos
- Consume y publica contratos de /core/contracts.py

## Eventos
- Emite y consume eventos de decisión y riesgo

## Dependencias
- chromadb, Pydantic, core.events

## Requisitos
- Python 3.10+, dependencias en requirements.txt

## Instalación
- Incluido en el repositorio principal

## Configuración
- No requiere configuración adicional

## Ejecución
- Importar motores y lógica desde pipeline o interfaces

## Integración
- Usar desde pipeline, agents o CLI

## Errores Comunes
- Fallos de validación, memoria táctica no inicializada

## Logs Esperados
- Logs de decisiones y riesgos en /logs/

## Ejemplo de Uso
```python
from domain.risk_engine.device_reputation import DeviceReputation
score = DeviceReputation().calculate_risk(device_id, activity)
```

## Diagrama de Flujo
[![](../docs/diagrams/domain_flow.png)](../docs/diagrams/domain_flow.png)

## Checklist de Seguridad
- [x] Validación de entradas
- [x] Logs estructurados
- [x] Observabilidad
- [x] Contratos estrictos

---

# Dominio de ARES-11

Contiene modelos, reglas, lógica de decisión y motores de riesgo. Todo el core de negocio debe residir aquí, desacoplado de infraestructura.