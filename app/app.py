"""Demo: ¿es informal este empleo? (EPEN 2025, Puno)

Se ejecuta con:  streamlit run app/app.py
El modelo (modelo.joblib) es el pipeline completo guardado en notebooks/05_interpretacion.ipynb.
"""
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Años de estudio aproximados por nivel (igual que en los notebooks)
ANIOS = {"Sin nivel/inicial": 0, "Primaria incompleta": 3, "Primaria completa": 6, "Secundaria incompleta": 8,
         "Secundaria completa": 11, "Superior no univ. incompleta": 12, "Superior univ. incompleta": 13,
         "Superior no univ. completa": 14, "Superior univ. completa": 16, "Posgrado": 18}

st.set_page_config(page_title="Empleo informal en Puno", page_icon="💼")
st.title("💼 ¿Es informal este empleo?")
st.write("Ingrese los datos de una persona **ocupada** en Puno. El modelo estima la probabilidad de que su "
         "empleo sea **informal** (según la definición del INEI). Fue entrenado con la EPEN 2025.")

modelo = joblib.load(Path(__file__).parent / "modelo.joblib")
cat = modelo.named_steps["prep"].named_transformers_["cat"].named_steps["onehot"]
sexos, areas, _, lenguas, etnias, ocupaciones, ramas, _ = [list(c) for c in cat.categories_]  # categorías vistas al entrenar
niveles = sorted(ANIOS, key=ANIOS.get)

col1, col2 = st.columns(2)
with col1:
    st.subheader("La persona")
    sexo = st.radio("Sexo", sexos, horizontal=True)
    edad = st.number_input("Edad", 14, 100, 35)
    educacion = st.selectbox("Último nivel educativo", niveles, index=niveles.index("Secundaria completa"))
    lengua = st.selectbox("Lengua materna", lenguas, index=lenguas.index("Castellano"))
    etnia = st.selectbox("Se considera", etnias, index=etnias.index("Mestizo"))
    area = st.radio("Área de residencia", areas, horizontal=True)
    limitacion = st.checkbox("Tiene alguna limitación permanente (moverse, ver, oír, etc.)")
with col2:
    st.subheader("El trabajo")
    ocupacion = st.selectbox("Ocupación principal", ocupaciones, index=ocupaciones.index("Servicios y vendedores"))
    rama = st.selectbox("Rama de actividad", ramas, index=ramas.index("Comercio"))
    horas = st.number_input("Horas trabajadas a la semana", 1, 112, 40)
    ingreso = st.number_input("Ingreso mensual de la ocupación principal (S/)", 0, 20000, 1200, step=50)
    quiere_mas = st.checkbox("Quisiera trabajar más horas")

caso = pd.DataFrame([{
    "edad": edad, "horas_semana": horas, "ingreso_log": float(np.log1p(ingreso)),
    "n_limitaciones": int(limitacion), "anios_estudio": ANIOS[educacion],
    "sexo": sexo, "area": area, "educacion": educacion, "lengua": lengua, "etnia": etnia,
    "ocupacion": ocupacion, "rama": rama, "quiere_mas_horas": "Sí" if quiere_mas else "No",
}])

if st.button("Estimar", type="primary"):
    prob = modelo.predict_proba(caso)[0, 1]
    st.metric("Probabilidad de empleo informal", f"{prob:.0%}")
    if prob >= 0.5:
        st.error("⚠️ Es probable que este empleo sea **informal**.")
    else:
        st.success("✅ Es probable que este empleo sea **formal**.")

st.caption("Proyecto académico · Machine Learning · Maestría en Ciencia de Datos e IA · EPG UNAJ. "
           "Datos: EPEN 2025, INEI (Puno). El modelo es una estimación estadística: solo debe usarse para "
           "priorizar programas de apoyo y formalización, nunca para negar beneficios ni sancionar.")
