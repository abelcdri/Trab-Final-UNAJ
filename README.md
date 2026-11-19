# 💼 Empleo informal en Puno: ¿quién tiene un empleo informal?

> **Machine Learning · Maestría en Ciencia de Datos e Inteligencia Artificial · EPG UNAJ**

**Equipo:** Abel Condori Carcasi

🔗 **Demo:** [enlace a la app publicada en Streamlit Community Cloud] · 📄 **Informes:** [Producto 1](informe/Producto1.md) · [Producto 2](informe/Producto2.md)

---

## 1. El problema

El empleo informal deja a los trabajadores sin contrato, seguro de salud ni pensión. En nuestra muestra de Puno, **casi 8 de cada 10 ocupados (78 %) tienen un empleo informal**. Un modelo que estime quién lo tiene, a partir de rasgos de la persona y de su trabajo, sirve para **focalizar programas de formalización y protección social**.

**Pregunta:** dadas las características de una persona ocupada en Puno, ¿tiene un empleo informal?

- **Tipo de problema:** clasificación binaria (informal / formal).
- **Métrica principal:** **exactitud balanceada**. Con 78 % de informales, un modelo que dice "todos son informales" tendría un recall de informales de 1,00 sin aprender nada. Reportamos también el **ROC-AUC** y el recall de cada grupo.

## 2. Los datos

| Campo | Detalle |
|---|---|
| Fuente | Encuesta Permanente de Empleo Nacional (EPEN) 2025, INEI, base anual de Puno |
| Tamaño | 18 264 registros; **7 836 ocupados** (5 479 personas distintas) |
| Variables usadas | 13: edad, horas, ingreso, educación, ocupación, rama, sexo, zona, lengua, etnia, etc. |
| Variable objetivo | `informal` (1 = empleo informal): **77,8 %** |

Excluimos las variables con las que el INEI define la informalidad (registro SUNAT, seguro, pensiones, tamaño de empresa) para evitar **fuga de datos**. Como la EPEN es un panel, **toda la validación es por persona**. Detalles en [`data/README.md`](data/README.md).

## 3. Resultados principales

| Modelo | Exactitud balanceada (CV) | ROC-AUC (CV) |
|---|---|---|
| Baseline (clase mayoritaria) | 0,500 | 0,500 |
| k-NN (k = 15) | 0,827 ± 0,009 | 0,933 ± 0,003 |
| Random Forest | 0,869 ± 0,008 | 0,949 ± 0,003 |
| Gradient boosting | 0,869 ± 0,007 | 0,948 ± 0,004 |
| Regresión logística (L2) | 0,870 ± 0,003 | 0,948 ± 0,004 |
| **Gradient boosting optimizado · modelo final** | — | **0,951 ± 0,006** (5×5) |
| Red neuronal (MLP) | — | 0,947 ± 0,005 |

**En el test**, el modelo final obtiene exactitud balanceada = **0,888** y ROC-AUC = **0,956** (detecta al 90 % de los informales y al 88 % de los formales).

**Hallazgos clave:**
- La señal más fuerte es el **ingreso** y la **rama de actividad**; después, los años de estudio.
- El boosting optimizado supera a la logística en **24 de 25 folds**, pero por solo **0,004 de ROC-AUC**: mejora consistente y modesta.
- k-means encontró, sin conocer la respuesta, **dos perfiles con 97–98 % de informalidad** que suman el 46 % de los trabajadores.
- ⚠️ El modelo se equivoca más con **trabajadores formales jóvenes** (acierta 74 %) y con **mujeres formales** (16 % mal clasificadas, contra 10 % en hombres).

## 4. Estructura del repositorio

```
├── README.md
├── requirements.txt
├── data/
│   ├── README.md                      ← fuente, variables y exclusiones
│   ├── 21_Puno_EPEN_Anual_2025.csv
│   └── Diccionario_EPEN.pdf
├── notebooks/
│   ├── 01_eda.ipynb                   ← Producto 1
│   ├── 02_modelos.ipynb               ← Producto 1
│   ├── 03_optimizacion.ipynb          ← Producto 2
│   ├── 04_no_supervisado_y_red.ipynb  ← Producto 2
│   └── 05_interpretacion.ipynb        ← Producto 2 (guarda app/modelo.joblib)
├── app/                               ← demo en Streamlit
├── informe/                           ← Producto1.md, Producto2.md y figuras/
```

## 6. Limitaciones y uso responsable

- Los datos son de **un solo departamento y un solo año**; solo se esta viendo el departamento de Puno.
- El ingreso puede ser en parte *consecuencia* de la informalidad; sin él, el modelo baja a 0,864 de exactitud balanceada.
- El modelo solo debe usarse para **priorizar programas de apoyo y formalización**, nunca para negar beneficios ni sancionar a trabajadores o empresas.
