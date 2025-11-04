import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("bmw.csv")

# Mostrar las primeras filas del dataset
print("📄 Primeras 5 filas del dataset:")
print(df.head(), "\n")

# Información general del DataFrame
print("📊 Información general:")
print(df.info(), "\n")

# Descripción estadística de las columnas numéricas
print("📈 Descripción estadística:")
print(df.describe(), "\n")

# Mostrar los nombres de las columnas
print("🧩 Columnas del dataset:")
print(df.columns, "\n")

# Verificar si hay valores nulos
print("❌ Valores nulos por columna:")
print(df.isnull().sum())