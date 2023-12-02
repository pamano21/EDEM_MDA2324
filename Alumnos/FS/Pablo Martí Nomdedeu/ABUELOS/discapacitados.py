
import pandas as pd 
# Cargar el archivo CSV en un DataFrame (reemplaza 'usuarios.csv' con el nombre de tu archivo)

nombre_archivo = 'usuarios.csv'
data = pd.read_csv("/content/usuarios.csv")

# Verificar si 'discapacidad' es una columna en el archivo
if 'discapacidad' in data.columns:
    # Convertir los valores de discapacidad a puntos (1 punto por cada 1%)
    data['puntos'] = data['discapacidad']  # Se asume que los valores ya están en el rango de 0% a 100%

    # Ordenar los usuarios en función de los puntos de discapacidad en orden ascendente
    usuarios_ordenados_discapacidad = data.sort_values(by='puntos', ascending=True)

    # Imprimir los usuarios en orden ascendente según los puntos obtenidos por discapacidad
    print("Usuarios en orden ascendente según los puntos de discapacidad:")
    print(usuarios_ordenados_discapacidad)
else:
    print("No se encontró la columna 'discapacidad' en el archivo.")
