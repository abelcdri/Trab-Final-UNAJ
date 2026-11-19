# Notebooks

Ejecútenlos **en orden**. Cada uno es independiente: carga los datos y repite la misma división entrenamiento/test.

| Notebook | Producto | Qué hace |
|---|---|---|
| `01_eda.ipynb` | 1 | Análisis exploratorio, panel y fuga de datos |
| `02_modelos.ipynb` | 1 | Pipeline y comparación de 5 modelos |
| `03_optimizacion.ipynb` | 2 | Optimización (30 intentos) y comparación fold a fold |
| `04_no_supervisado_y_red.ipynb` | 2 | Perfiles con k-means y red neuronal (MLP) |
| `05_interpretacion.ipynb` | 2 | Importancia, sesgo y modelo final (`app/modelo.joblib`) |

**Tiempos aproximados (1 CPU):** 01 y 04, segundos · 02, ~15 s · 03, ~4 a 5 min · 05, ~10 s.

**Notas técnicas**
- La validación usa `StratifiedGroupKFold` con `LLAVE_PANEL`: una misma persona nunca queda en entrenamiento y en validación a la vez.
- Se usa `HistGradientBoostingClassifier` (scikit-learn) en lugar de LightGBM, para no depender de librerías extra.
- El notebook 03 usa **Optuna** si está instalado; si no, una búsqueda aleatoria con el mismo espacio y número de intentos. Los resultados de los informes se obtuvieron con la **búsqueda aleatoria**; con Optuna pueden variar ligeramente.
