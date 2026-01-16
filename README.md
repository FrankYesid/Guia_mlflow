# Guia MLflow: Proyecto Churn Telco

Este proyecto implementa un flujo de trabajo de Machine Learning para predicción de churn de clientes de telecomunicaciones usando MLflow, organizado con una arquitectura hexagonal para separar dominio, aplicación, infraestructura e interfaces.

## Dataset
- Ubicación: `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`
- Ejemplo de contenido: [Telco Churn:L1-L6](file:///d:/GitHub/Guia_mlflow/data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv#L1-L6)
- Se normaliza `TotalCharges` a numérico y se descartan filas con valores nulos en esa columna.

## Arquitectura Hexagonal
- Dominio: puertos y contratos que definen cómo se accede a los datos y lógica central.
- Aplicación: casos de uso orquestan procesos (entrenamiento, registro en MLflow).
- Infraestructura: implementaciones concretas (repositorios, pipelines de ML).
- Interfaces: puntos de entrada (CLI, servicios) que invocan casos de uso.

## Estructura de Carpetas
- Configuración
  - [settings.py](file:///d:/GitHub/Guia_mlflow/src/config/settings.py): rutas, parámetros y nombre del experimento MLflow.
- Dominio
  - [dataset_repository.py](file:///d:/GitHub/Guia_mlflow/src/domain/repositories/dataset_repository.py): contrato para cargar datasets tabulares.
- Infraestructura
  - [csv_churn_dataset_repository.py](file:///d:/GitHub/Guia_mlflow/src/infrastructure/repositories/csv_churn_dataset_repository.py): lectura y limpieza del CSV Telco.
  - [preprocessing.py](file:///d:/GitHub/Guia_mlflow/src/infrastructure/pipelines/preprocessing.py): pipeline con imputación, OneHotEncoder y LogisticRegression.
- Aplicación
  - [train_churn_model.py](file:///d:/GitHub/Guia_mlflow/src/application/use_cases/train_churn_model.py): entrenamiento, métricas y registro en MLflow.
- Interfaces
  - [train.py](file:///d:/GitHub/Guia_mlflow/src/interfaces/cli/train.py): CLI de entrenamiento.
- Documentación
  - [guia_basica.md](file:///d:/GitHub/Guia_mlflow/docs/guia_basica.md)
  - [proximos_pasos.md](file:///d:/GitHub/Guia_mlflow/docs/proximos_pasos.md)

## Requisitos
- Python 3.8+
- Dependencias (ver `requirements.txt`):
  - mlflow
  - pandas
  - scikit-learn
  - numpy
  - scipy
  - sweetviz
  - jupyter

## Instalación
1. Crear entorno virtual (Windows PowerShell):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución
1. Entrenamiento y registro en MLflow:
   ```bash
   python -m src.interfaces.cli.train
   ```
   Imprime `accuracy` y, si está disponible, `roc_auc`.
2. Visualización de experimentos:
   ```bash
   mlflow ui --port 5000
   ```
   Abrir `http://localhost:5000` para explorar ejecuciones, métricas y artefactos.

## Notebooks
- Exploración descriptiva:
  - [01_data_overview.ipynb](file:///d:/GitHub/Guia_mlflow/notebooks/01_data_overview.ipynb)
  - Muestra dimensiones, encabezados, describe columnas, tipos y valores nulos.
- Reporte automatizado con Sweetviz:
  - [02_sweetviz_report.ipynb](file:///d:/GitHub/Guia_mlflow/notebooks/02_sweetviz_report.ipynb)
  - Genera HTML en [telco_churn_sweetviz.html](file:///d:/GitHub/Guia_mlflow/notebooks/reports/telco_churn_sweetviz.html)
- Abrir cuadernos:
  ```bash
  jupyter notebook notebooks/
  ```

## MLflow: Detalles de Tracking
- Experimento: `churn_telco` (configurado en `settings.py`).
- Parámetros: `model`, `test_size`, `random_state`.
- Métricas: `accuracy`, `roc_auc` (si `predict_proba` está disponible).
- Artefactos: modelo sklearn (`artifact_path="model"`).

## Buenas Prácticas
- Reproducibilidad: fijar semillas y registrar versiones de librerías.
- Trazabilidad: usar `mlflow.set_tag` con dataset, entorno y propósito.
- Seguridad: no registrar datos sensibles, gestionar accesos al servidor MLflow.
- Artefactos: mantener organización por ejecución para fácil auditoría.

## Próximos Pasos
- Configurar servidor de tracking persistente y artifact store externo.
- Definir convenciones de etiquetas y estructura de proyectos.
- Pipeline de validación y promoción en Model Registry.
- CLI de inferencia y servicio con `mlflow models serve`.
- Pruebas unitarias y CI/CD para reproducibilidad.
- Más detalles en: [proximos_pasos.md](file:///d:/GitHub/Guia_mlflow/docs/proximos_pasos.md)

## Ignorados (.gitignore)
- Archivo: [.gitignore](file:///d:/GitHub/Guia_mlflow/.gitignore)
- Incluye reglas para:
  - Artefactos MLflow (`mlruns/`) y logs.
  - Entornos virtuales (`.venv/`, `venv/`, etc.).
  - Archivos temporales de Python (`__pycache__/`, bytecode).
  - IDEs y editores (`.vscode/`, `.idea/`).
  - Datos: ignora `data/**` pero versiona `data/raw/**`.

## Licencia
- Este proyecto está bajo la licencia MIT. Ver [LICENSE](file:///d:/GitHub/Guia_mlflow/LICENSE).
