import pandas as pd

# Ruta del archivo CSV
csv_file = 'proyect_2/autos.csv'

# Leer el archivo CSV en un DataFrame
df = pd.read_csv(csv_file, sep=';', encoding='utf-8')

# Definir la función de recodificación
def recodificar_pais(pais):
    if pais == 'USA':
        return 1
    elif pais == 'Europe':
        return 2
    elif pais == 'Japan':
        return 3
    else:
        return 0  # Para países no especificados, puedes devolver 0 o None
    
# Aplicar la función a la columna 'Pais_Origen'
df['Pais_Origen'] = df['Pais_Origen'].apply(recodificar_pais)

# Mostrar el DataFrame con los valores recodificados
print(df.head(10))  # Cambia el número de filas si es necesario
