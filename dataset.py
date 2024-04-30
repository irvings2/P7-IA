import numpy as np
import pandas as pd

# Cargar datos desde el archivo .data
datos = pd.read_csv('bezdekIris.data')

# Calcular estadísticas para todas las columnas numéricas
stats_todas = datos.describe()
print("\nEstadísticas para todas las columnas numéricas:")
print(stats_todas)

# Separar datos por categoría
categorias = datos.dtypes[datos.dtypes == 'object'].index
for categoria in categorias:
    # Separar datos por categoría
    datos_categoria = datos.groupby(categoria)
    
    print(f"\nEstadísticas para la categoría '{categoria}': ")
    for nombre_grupo, grupo in datos_categoria:
        # Seleccionar solo las columnas numéricas del grupo
        grupo_numerico = grupo.select_dtypes(include=[np.number])
        
        # Calcular estadísticas para las columnas numéricas del grupo
        stats_grupo = grupo_numerico.describe()
        print(f"\nGrupo '{nombre_grupo}':")
        print(stats_grupo)
        