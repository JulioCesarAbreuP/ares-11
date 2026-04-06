# CLI de ARES-11

Responsabilidad: Orquestar el pipeline desde línea de comandos, permitiendo ejecución completa o por etapas.

- `ares11.py`: CLI principal, integra con el orquestador y publica eventos estructurados.
- Entrada: argumentos de línea de comandos (input, stage)
- Salida: resultado del pipeline o etapa
- Relación: Invoca `/core/orchestrator.py` y publica eventos vía `/core/utils.py`
