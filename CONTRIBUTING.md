# Guía de Contribución

## Normas de contribución
- Toda contribución debe estar alineada con la visión, arquitectura y estándares de calidad de ARES-11.
- Abre un issue antes de iniciar cambios significativos.
- Los cambios deben ser atómicos y bien documentados.
- No se aceptan cambios que modifiquen lógica crítica sin revisión de los responsables.

## Estilo de código
- JavaScript/Node.js: seguir el estándar [Airbnb JavaScript Style Guide](https://airbnb.io/javascript/).
- Go: seguir [Effective Go](https://go.dev/doc/effective_go).
- Usar comentarios claros y descriptivos.
- Mantener consistencia en nombres, estructura y modularidad.

## Estructura de ramas
- `main`: rama estable y protegida.
- `develop`: integración de nuevas funcionalidades.
- `feature/*`: nuevas características.
- `fix/*`: correcciones de errores.
- `docs/*`: mejoras de documentación.

## Proceso de Pull Request (PR)
- Hacer PRs contra `develop`.
- Incluir descripción clara, contexto y motivación.
- Referenciar issues relacionados.
- Asegurar que el código pase pruebas y linting.
- Esperar revisión y aprobación antes de merge.

## Estándares de calidad
- Cobertura de pruebas mínima: 80%.
- Documentación actualizada y coherente.
- Cumplimiento de buenas prácticas de seguridad y telemetría.
- Validación de entradas y salidas.
- Revisión cruzada obligatoria para cambios críticos.
