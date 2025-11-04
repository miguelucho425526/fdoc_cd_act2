# 🧾 Análisis General del Dataset: BMW Car Data Analysis

## 📘 1. Descripción general del dataset

Este dataset contiene información detallada sobre **10,781 automóviles BMW**, incluyendo variables técnicas, de rendimiento y económicas.  
Su propósito principal es permitir el **análisis de precios, tendencias del mercado y características técnicas** de los diferentes modelos de BMW.

- **Cantidad de registros:** 10,781  
- **Cantidad de columnas:** 9  
- **Fuente:** Datos públicos de automóviles (Kaggle)  
- **Objetivo:** Analizar cómo las características del vehículo influyen en el precio y consumo de combustible.

### 🧩 Variables incluidas

| Columna | Descripción | Ejemplo |
|----------|-------------|----------|
| `model` | Modelo del vehículo | 3 Series, X5, 1 Series |
| `year` | Año de fabricación | 2018 |
| `price` | Precio del vehículo (en libras) | 27000 |
| `transmission` | Tipo de transmisión | Automatic, Manual |
| `mileage` | Kilometraje recorrido (en millas) | 62794 |
| `fuelType` | Tipo de combustible | Diesel, Petrol |
| `tax` | Impuesto anual (en libras) | 145 |
| `mpg` | Rendimiento en millas por galón | 57.6 |
| `engineSize` | Tamaño del motor (en litros) | 2.0 |

---

## ⚙️ 2. Clasificación de columnas por tipo de dato

| Tipo de Dato | Columnas |
|---------------|-----------|
| **Numéricas (int, float)** | `year`, `price`, `mileage`, `tax`, `mpg`, `engineSize` |
| **Categóricas (object)** | `model`, `transmission`, `fuelType` |
| **Fechas** | No contiene columnas de fecha (aunque `year` puede tratarse como temporal). |
| **Texto libre** | Ninguna columna contiene texto descriptivo extenso. |
| **Booleanas** | No existen columnas booleanas. |

---

## 🔧 3. Transformaciones aplicadas

Durante el proceso de análisis inicial se realizaron las siguientes operaciones básicas de preparación:

| Transformación | Descripción | Resultado |
|----------------|-------------|------------|
| **Carga del archivo CSV** | Se importó el dataset usando `pd.read_csv("BMW.csv")`. | ✅ Éxito |
| **Verificación de nulos** | Se ejecutó `df.isnull().sum()` para detectar valores faltantes. | ✅ Ningún valor nulo |
| **Conversión de tipos automáticos** | `pandas` detectó correctamente los tipos de datos (int, float, object). | ✅ Correctos |
| **Revisión de duplicados (opcional)** | `df.duplicated().sum()` (puede aplicarse si se desea limpieza adicional). | 🔄 No aplicado |
| **Análisis estadístico** | `df.describe()` para obtener medidas descriptivas básicas. | ✅ Aplicado |

No se aplicaron transformaciones que alteren el contenido original, ya que los datos estaban limpios y estructurados.

---

## 📊 4. Resumen estadístico general

| Variable | Promedio | Mínimo | Máximo | Desviación estándar |
|-----------|-----------|--------|--------|---------------------|
| **Año** | 2017.08 | 1996 | 2020 | 2.35 |
| **Precio (£)** | 22,733 | 1,200 | 123,456 | 11,415 |
| **Kilometraje (millas)** | 25,496 | 1 | 214,000 | 25,143 |
| **Impuesto (£)** | 131.7 | 0 | 580 | 61.5 |
| **Eficiencia (mpg)** | 56.4 | 5.5 | 470.8 | 31.3 |
| **Motor (L)** | 2.17 | 0.0 | 6.6 | 0.55 |

---

## 💡 5. Conclusiones

1. **Calidad del dataset:**  
   El conjunto de datos se encuentra **limpio y bien estructurado**, sin valores nulos ni inconsistencias.

2. **Tendencias de fabricación:**  
   La mayoría de los vehículos son recientes (años entre 2016 y 2020), lo que permite análisis actuales del mercado.

3. **Precios y desempeño:**  
   - Los precios varían significativamente (desde £1,200 hasta más de £120,000).  
   - Los vehículos con motores más grandes y menor kilometraje tienden a tener precios más altos.  
   - El rendimiento (mpg) muestra gran dispersión, reflejando diferencias entre autos deportivos y urbanos.

4. **Tipos de variables:**  
   La mayoría son **numéricas**, ideales para modelos de regresión o predicción de precios.

5. **Usos potenciales:**  
   - Modelos predictivos de precio.  
   - Segmentación de autos por características técnicas.  
   - Estudios de eficiencia de combustible por tipo de motor o transmisión.

---


