import pandas as pd
import json 
import great_expectations as ge
from great_expectations.dataset import PandasDataset

usuarios_df = pd.read_csv('C:\\Users\\casa\\Desktop\\Python\\Integradores\\usuarios.csv')
#print(usuarios_df)

with open('C:\\Users\\casa\\Desktop\\Python\\Integradores\\productos.json') as file:
    productos_data = json.load(file)
productos_df = pd.DataFrame(productos_data)
#print(productos_df)


usuarios_df.fillna("Desconocido", inplace=True)
productos_df.fillna({"nombre": "Producto sin nombre"}, inplace=True) #limpia los nulos

usuarios_df.columns = usuarios_df.columns.str.lower()
productos_df.columns = productos_df.columns.str.lower()#renombro y normalizo las columnas para que tengan el mismo formato

usuarios_df['edad'] = pd.to_numeric(usuarios_df['edad'], errors='coerce').fillna(0).astype(int)
productos_df['precio'] = pd.to_numeric(productos_df['precio'], errors='coerce').fillna(0) #formateo los tipos de datos

usuarios_df['fecha_registro'] = pd.to_datetime(usuarios_df['fecha_registro'], errors='coerce')
productos_df['fecha_creacion'] = pd.to_datetime(productos_df['fecha_creacion'], errors='coerce') #formateo las fechas en ambos dataframe

print('datos transformados correctamente')


#cargo los datos
usuarios_df.to_csv("C:\\Users\\casa\\Desktop\\Python\\Integradores\\usuarios.csv", index=False)
productos_df.to_csv("C:\\Users\\casa\\Desktop\\Python\\Integradores\\productos.json", index=False)

print('datos cargados correctamente')

#armo las expectativas

usuarios_ge = PandasDataset(usuarios_df)
productos_ge = PandasDataset(productos_df)

#expectativas de usuarios
usuarios_ge.expect_column_values_to_not_be_null("email")  #emails no nulos
usuarios_ge.expect_column_values_to_be_in_set("edad", range(0, 120))#rango de edades
 
usuarios_ge.expect_column_values_to_match_regex("email", r".+@.+\..+") #emails en formato correcto, nombre@etc...

# expectativas de productos

productos_ge.expect_column_values_to_not_be_null("nombre") #nombres no nulos
productos_ge.expect_column_values_to_be_of_type("precio", "float") #que los precios sean float

#imprimo los resultados
print('******************* RESULTADOS DE LA VALIDACION DE USUARIOS:  ********************************')
print(usuarios_ge.validate())


print('\n******************* RESULTADOS DE LA VALIDACION DE PRODUCTOS:  ********************************')

print(productos_ge.validate())

# tuve muchos problemas con las rutas de los archivos y no pude guardarlo con great expectations
