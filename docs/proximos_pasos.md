# Próximos pasos organizados

## Objetivo
Consolidar una guía operativa de MLflow lista para equipos, cubriendo tracking, registro de modelos y despliegue, con enfoque en reproducibilidad y gobernanza.

## Decisiones iniciales
- Backend store de tracking:
  - Local (SQLite) para pruebas.
  - Producción: PostgreSQL/MySQL gestionado.
- Artifact store:
  - Local para pruebas.
  - Producción: S3/Azure Blob/GCS con políticas de retención.
- Autenticación y acceso:
  - Detrás de proxy (NGINX) y SSO/OAuth si aplica.

## Tareas técnicas prioritarias
1. Configurar servidor de tracking persistente
   - Definir `--backend-store-uri` (p.ej. Postgres) y `--default-artifact-root`.
   - Desplegar con systemd/Docker y backups.
2. Estandarizar estructura de proyectos
   - Carpetas: `data/`, `src/`, `experiments/`, `models/`, `reports/`.
   - Plantilla de experimentos con registro mínimo requerido.
3. Añadir etiquetas y convenciones
   - Tags: `dataset`, `env`, `purpose`, `owner`.
   - Naming: `exp_<proyecto>_<fecha>`, `run_<objetivo>_<semilla>`.
4. Pipeline de validación y promoción
   - Automatizar pruebas de desempeño/calidad antes de promover a Staging/Production.
   - Reglas de aprobación y rollback documentadas.
5. Integración CI/CD
   - Validar ejecuciones en PR (smoke tests).
   - Empaquetado con `mlflow projects` y conda/requirements reproducibles.
6. Monitoreo y observabilidad
   - Métricas de servicio (latencia/errores) y drift de datos.
   - Alertas en degradaciones o cambios de distribución.
7. Seguridad y gobernanza
   - Protección de datos sensibles (PII).
   - Auditoría de cambios en Model Registry.

## Checklist incremental
- [ ] Servidor MLflow con persistencia (dev/staging/prod).
- [ ] Artifact store externo configurado (S3/Blob/GCS).
- [ ] Plantilla de experimentos y convenciones publicadas.
- [ ] Flujo de promoción con validaciones automatizadas.
- [ ] Dashboards de métricas y notificaciones.
- [ ] Políticas de acceso y auditoría implementadas.

## Entregables sugeridos
- Documento de arquitectura (tracking, artifacts, seguridad).
- Plantilla de proyecto reproducible (cookiecutter).
- Scripts de arranque: `mlflow server`, backup/restore, limpieza de artefactos.
- Guías de operación: promoción, rollback, versionado, soporte.

## Riesgos y mitigaciones
- Crecimiento de almacenamiento: políticas de retención y compresión.
- Deriva de datos: validaciones periódicas y alertas.
- Fugas de secretos: uso de vaults/variables de entorno, revisiones de código.

## Próxima iteración
- Priorizar el servidor de tracking persistente y artifact store externo.
- Definir y socializar convenciones de etiquetado y estructura de proyectos.
- Preparar un ejemplo end-to-end con registro y despliegue.

