# Manual de Core

**Propósito:** Orquestador principal, inicializa y coordina todos los módulos.

## Uso
- El core se ejecuta automáticamente al iniciar ARES-11 (`main.go`).
- Gestiona el ciclo de vida de los módulos y la comunicación entre ellos.

## Comandos principales
- `core.Start()`: Inicializa el sistema.

## Integración
- Todos los módulos dependen del core para su ciclo de vida y señales.
