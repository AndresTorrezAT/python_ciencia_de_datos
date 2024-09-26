import pandas as pd
import numpy as np

# Ruta del archivo CSV
csv_file = 'autos.csv'  # Cambia esto por la ruta correcta de tu archivo CSV

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file, sep=';', encoding='utf-8')

# Limpieza y tratamiento de las variables
# Verificar tipos de datos
print(df.info())

# Manejo de valores nulos (puedes optar por eliminar o llenar valores nulos)
df.dropna(inplace=True)  # Elimina filas con valores nulos

# Asegúrate de que las columnas necesarias sean del tipo correcto
# Reemplaza 'var1' y 'var2' con los nombres reales de las columnas en tu DataFrame
df['var1'] = pd.to_numeric(df['var1'], errors='coerce')
df['var2'] = pd.to_numeric(df['var2'], errors='coerce')

# Elimina filas con valores nulos nuevamente si es necesario
df.dropna(inplace=True)

# Generar nuevas variables
df['log10_var1_var2'] = np.log10(df['var1'] / df['var2'])

# Condición: Si var1 > var2 → 5, caso contrario 3
df['sqrt_var1_exp_var2'] = np.sqrt(df['var1']) * np.exp(df['var2']) / 2003
df['sqrt_var1_exp_var2'] = np.where(df['var1'] > df['var2'], 5, 3)

df['logn_var1_var2'] = 1 / (np.log(df['var1'] / df['var2'])) * 100

df['var2_squared_div_var1'] = df['var2'] ** 2 / df['var1']

df['var1_div_var2_squared'] = df['var1'] / (df['var2'] ** 2)

# Mostrar el resultado
print(df.head())
