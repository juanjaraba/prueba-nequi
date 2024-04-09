#Cargamos librerías principales
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Se hace la lectura de la sabana de datos
data = pd.read_csv('./data/bankdataset.csv')

#Se conocen los datos
print(data.info())
#print(data.head())

#Se busca si hay datos duplicados
print(data[data.duplicated()])

total_duplicates = len(data) - len(data.drop_duplicates())
print(f"Total duplicates: {total_duplicates}")

#print(data.describe())
print(data.head())

print(type(data["Date"]))
#Transformación del campo fecha para crear una nueva columna fecha en formato número
#Esto se hace porque la data esta muy depurada y para aplicar el ejercicio de transformacion se crea este nuevo campo
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data["Date_Integer"] = data["Date"].dt.strftime("%Y%m%d").astype(int)
print(data)
