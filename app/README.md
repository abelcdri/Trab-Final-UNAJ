# Demo

App de Streamlit que estima la probabilidad de que el empleo de una persona ocupada en Puno sea **informal**.

```bash
pip install -r app/requirements.txt
streamlit run app/app.py
```

- El modelo `modelo.joblib` lo genera `notebooks/05_interpretacion.ipynb`. Si lo vuelven a generar, copien el archivo nuevo aquí.
- Está guardado con `scikit-learn==1.9.1`; usen esa versión (está en `requirements.txt`) o regeneren el modelo.
- Para publicarla: **Streamlit Community Cloud** → *New app* → este repositorio → archivo `app/app.py`.
