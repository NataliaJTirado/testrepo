import pandas as pd

df = pd.read_csv('files/datos_dummies_ventas_ejercicio.csv')
#print(df.head())

#ventas_cat = df.groupby('Categoria')['Venta_ID'].sum().value_counts()
ventas_cat = df['Categoria'].value_counts()
print('\nLos productos vendidos por categoria son:\n',ventas_cat)

top_5 = df['Producto'].value_counts()
maximo = top_5.head(5)
print('\nLos 5 productos mas vendidos son:\n',maximo)

precios_maximos = df['Precio_Unitario'].max()
precios_minimos = df['Precio_Unitario'].min()
#print(precios_maximos, precios_minimos)

df["rango de precios"] = pd.cut( #cut es un metodo estatico
    df["Precio_Unitario"], bins = [0, 25, 50, 75, 100, float('inf')], labels = ["0-25","25-50", "50-75","75-100","100+"])

rangos = df["rango de precios"].value_counts()
print('\nEl rango de los precios es:\n',rangos)

total_ventas = df.groupby('Categoria')['Precio_Total'].sum()
print('\nlas ventas totales por categoria son las siguientes\n',total_ventas)

ventas_producto = df.groupby('Producto')['Cantidad'].sum()
print('\nLa cantidad de ventas por producto son:\n',ventas_producto)