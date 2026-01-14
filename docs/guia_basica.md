# Guía básica de MLflow

## ¿Qué es MLflow?
MLflow es una plataforma abierta para gestionar el ciclo de vida del ML: experimentación, reproducibilidad y despliegue. Sus cuatro componentes principales:
- Tracking: registro de parámetros, métricas, artefactos y código.
- Projects: empaquetado reproducible de proyectos.
- Models: formato estándar de modelos y herramientas de inferencia.
- Model Registry: catálogo central para versionado, estados y gobernanza.

## Requisitos e instalación
- Requisitos: Python 3.8+, pip, entorno virtual recomendado.
- Instalación:

```bash
pip install mlflow
```

## Primeros pasos con Tracking
Registra parámetros, métricas y artefactos en una ejecución:

```python
import mlflow
import time

mlflow.set_experiment("demo_guia_mlflow")

with mlflow.start_run(run_name="primer_intento"):
    mlflow.log_param("modelo", "baseline")
    for step in range(5):
        metric = 1.0 / (step + 1)
        mlflow.log_metric("loss", metric, step=step)
        time.sleep(0.2)
    mlflow.log_text("Notas de la ejecución", "notas.txt")
```

Inicia la interfaz UI local:

```bash
mlflow ui --port 5000
```

Accede a http://localhost:5000 para visualizar experimentos y ejecuciones.

## Artefactos y organización
- Artefactos: archivos generados (plots, datasets, modelos) por ejecución.
- Buenas prácticas:
  - Usa `mlflow.set_experiment("nombre_proyecto")` para agrupar trabajos.
  - Nombra `run_name` con contexto (dataset, versión, fecha).
  - Registra datos mínimos: hiperparámetros, métricas clave, seed, versión de código.

## Guardado de modelos
Ejemplo con modelos Python (formato pyfunc):

```python
import mlflow.pyfunc
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=3, noise=0.1, random_state=42)
model = LinearRegression().fit(X, y)

class SklearnWrapper(mlflow.pyfunc.PythonModel):
    def __init__(self, mdl):
        self.mdl = mdl
    def predict(self, context, model_input):
        return self.mdl.predict(model_input)

with mlflow.start_run(run_name="modelo_lineal"):
    mlflow.sklearn.log_model(model, artifact_path="model_sklearn")
    mlflow.pyfunc.log_model(
        artifact_path="model_pyfunc",
        python_model=SklearnWrapper(model)
    )
```

## Model Registry (catálogo de modelos)
- Permite versionar modelos, asignar estados (Staging, Production, Archived) y comentarios.
- Flujo típico:
  1. Registrar el modelo desde una ejecución.
  2. Promocionar de Staging a Production tras validación.
  3. Auditar cambios y revertir si es necesario.

## Despliegue básico
Sirve un modelo pyfunc localmente:

```bash
mlflow models serve -m runs:/<RUN_ID>/model_pyfunc -p 8080
```

Para cargar y predecir en código:

```python
import mlflow.pyfunc
model = mlflow.pyfunc.load_model("runs:/<RUN_ID>/model_pyfunc")
preds = model.predict([[0.1, 0.2, 0.3]])
```

## Buenas prácticas esenciales
- Reproducibilidad: fija semillas, registra hashes/commit del código y versiones de librerías.
- Trazabilidad: usa etiquetas (`mlflow.set_tag`) para dataset, entorno y propósito.
- Limpieza: estructura artefactos por ejecución para evitar mezcla de resultados.
- Seguridad: evita registrar datos sensibles, controla accesos al servidor de tracking.

## Problemas comunes y soluciones
- La UI no muestra métricas: verifica que el proceso escribió en el mismo backend store.
- Métricas discontinuas: asegura que `step` sea creciente y consistente.
- Artefactos grandes: usa un artifact store externo (S3, Azure Blob, GCS).

## Referencias rápidas
- Comandos:
  - `mlflow ui`: interfaz gráfica de experimentos.
  - `mlflow server`: servidor de tracking multiusuario.
  - `mlflow models serve`: servicio HTTP de modelos.
- APIs clave:
  - `mlflow.start_run`, `mlflow.log_param`, `mlflow.log_metric`, `mlflow.log_artifact`.

