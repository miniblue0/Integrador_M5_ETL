import pandas as pd
import json 
from great_expectations.dataset import PandasDataset

data_csv = pd.read_csv('Integradores/usuarios.csv')
#print(data_csv)

with open('Integradores/productos.json') as file:
    data_json = pd.DataFrame(json.load(file))
#print(data_json)


data_csv.fillna({'edad': 0, 'nombre': 'Desconocido'}, inplace=True) #limpia los nulos

data_csv.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True) #renombro y normalizo las columnas para que tengan el mismo formato

data_csv['edad'] = data_csv['edad'].astype(int) #formateo la edad a numeros

data_csv['fecha_nacimiento'] = pd.to_datetime(data_csv['fecha_nacimiento'], errors='coerce') #formateo las fechas

#armo el dataframe y empiezo a comprobar los cambios
df_transformed = data_csv

ge_df = PandasDataset(df_transformed)
ge_df.expect_column_values_to_be_of_type('edad', 'int') #verifivo si los cambios estan bien

ge_df.expect_column_values_to_be_unique('id') #reviso que no haya id repetidos

ge_df.expect_column_values_to_be_in_range('edad', 0, 120) #verifico el rango de edades

ge_df.expect_column_values_to_not_be_null('nombre') #no hay valores nulos

ge_df.expect_column_values_to_match_strftime_format('fecha_nacimiento', '%Y-%m-%d') #las fechas estan en el mismo formato

results = ge_df.validate()
print(results)

#great_expectations docs build








