# ONBOARDING PARA DESARROLLADORES ARES-11

## 1. Visión General
ARES-11 es una plataforma modular, enterprise y event-driven para defensa, auditoría y respuesta avanzada.

## 2. Estructura de Carpetas
- /core: contratos, eventos, utilidades
- /domain: lógica de negocio, motores, reglas
- /pipeline: stages desacoplados (AI Gateway, correlación, ejecución)
- /infrastructure: adaptadores externos, DLP, WORM, microsegmentación
- /interfaces: CLI, agentes, API REST
- /tests: pruebas unitarias, integración, resiliencia

## 3. Instalación Rápida
1. Clona el repo y crea un entorno virtual
2. Instala dependencias: `pip install -r requirements.txt`
3. Configura variables en /src/config/
4. Ejecuta pruebas: `pytest tests/`

## 4. Flujo de Desarrollo
- Cada módulo debe tener contrato tipado y pruebas
- Usa logs estructurados y sigue Clean Architecture
- Consulta /docs/TECHNICAL_GUIDE.md para detalles de cada módulo

## 5. Buenas Prácticas
- No acoples lógica de negocio a infraestructura
- Usa eventos y contratos para comunicación
- Añade pruebas y documentación a cada cambio

## 6. Recursos
- Manual técnico: /docs/TECHNICAL_GUIDE.md
- Ejemplos: /docs/examples/
- Guía de integración externa: /docs/INTEGRATION_GUIDE.md
- Contacto: equipo de arquitectura

---

# Onboarding para Desarrolladores ARES-11

Bienvenido a ARES-11. Este documento te guiará en la instalación, configuración, ejecución y extensión del sistema.

## Requisitos
- Python 3.10+
- pip, venv
- Acceso a Azure Blob Storage (WORM)
- Acceso a APIs externas (Telegram, Shodan, etc.)

## Instalación
1. Clona el repositorio y entra al directorio.
2. Crea un entorno virtual: `python -m venv .venv`
3. Activa el entorno: `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
4. Instala dependencias: `pip install -r requirements.txt`

## Configuración
- Edita los archivos en `/src/config/` para rutas, claves y parámetros.
- Configura variables de entorno para claves sensibles.

## Ejecución
- CLI: `python interfaces/cli/ares11.py`
- Automatizaciones: scripts en `/scripts/`
- Agentes: ver `/interfaces/agents/`

## Integración
- Usa contratos y eventos definidos en `/core`.
- Consulta los README de cada módulo para integración específica.

## Troubleshooting
- Revisa logs estructurados en `/logs/` y WORM.
- Consulta el checklist de seguridad y la guía técnica.

## Ejemplo de uso
```bash
python interfaces/cli/ares11.py --scan 192.168.1.0/24
```

## Checklist de Seguridad
- ¿Están validados todos los contratos?