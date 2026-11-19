# Datos

**Fuente:** Encuesta Permanente de Empleo Nacional (EPEN) 2025, Instituto Nacional de Estadística e Informática (INEI), base anual del departamento de **Puno** (código 21).
**Archivos:**
- `21_Puno_EPEN_Anual_2025.csv`: 18 264 filas (personas) × 131 columnas.
- `Diccionario_EPEN.pdf`: diccionario de datos del INEI (agosto 2026).

## Población de estudio
Personas **ocupadas** (`OCUP300 = 1`) con el indicador `Informal_P` del INEI: **7 836 observaciones de 5 479 personas** (2 357 aparecen dos veces porque la EPEN es un panel).

## Variable objetivo
`informal` = 1 si `Informal_P == 1`. **77,8 %** de los casos (6 100 informales, 1 736 formales).

> ⚠️ `Informal_P` **no figura en el diccionario**. Interpretamos 1 = informal y 2 = formal porque todos los trabajadores cuya empresa no está registrada en SUNAT (`C312 = 3`) tienen código 1. Conviene confirmarlo con el INEI o el docente.

## Variables usadas (13)

| Variable | Tipo | Origen | Descripción |
|---|---|---|---|
| `edad` | numérica | `C208` | Edad en años |
| `horas_semana` | numérica | `whoraT` | Horas trabajadas la semana pasada (todas las ocupaciones) |
| `ingreso_log` | numérica | `INGTOTP` | log(1 + ingreso mensual de la ocupación principal) |
| `n_limitaciones` | numérica | `C375_1` a `C375_6` | Número de limitaciones permanentes |
| `anios_estudio` | numérica | `C366` | Años de estudio aproximados según el nivel aprobado |
| `sexo` | categórica | `C207` | Hombre / Mujer |
| `area` | categórica | `AREA` | Urbano / Rural |
| `educacion` | categórica | `C366` | Nivel educativo (10 categorías) |
| `lengua` | categórica | `C376` | Quechua / Aimara / Castellano / Otra |
| `etnia` | categórica | `C377` | Autoidentificación |
| `ocupacion` | categórica | `C308_COD` | Gran grupo CIUO-08 (primer dígito) |
| `rama` | categórica | `C309_COD` | Rama de actividad CIIU agrupada (13 ramas) |
| `quiere_mas_horas` | categórica | `C333` | Quería trabajar más horas |
| **`informal`** | **objetivo** | `Informal_P` | **1 = empleo informal (78 %)** |

Además se usa `LLAVE_PANEL` (identifica a la persona) **solo para agrupar la validación**, nunca como predictor.

## Excluidas a propósito (fuga de datos)
`Informal_P` se construye con el registro en SUNAT (`C312`), los libros contables (`C313`), el tipo de trabajador (`C310`, `C311`), el tamaño de la empresa (`C317`, `C317A`), el seguro de salud y las pensiones (`SEGURO1`, `C361` a `C365`). Usarlas haría que el modelo "descubra" la regla de cálculo. También se excluyen `C338` y los ingresos desagregados por tipo de trabajador (se usa solo `INGTOTP`).

## Sobre los pesos muestrales
La base trae el factor de expansión `FAC300_ANUAL`. **No se usa para entrenar**; los porcentajes de este repositorio describen la **muestra**, no la población de Puno.
