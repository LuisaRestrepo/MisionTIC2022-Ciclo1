#!/usr/bin/env python
# coding: utf-8

# # Iniciamos 8:05pm

# # 1. Introducción
# - También llamados módulos en Python, son un conjunto de implementaciones funcionales codificadas en un lenguaje de  programación. Ofrecen paquetes de código ya estructurados a modo de funciones que pueden ser usadas por el programador. 
# - Las librerías no se ejecutan de manera autónoma, sino que es el programa que las invoca lo que les da a estas su respectivo uso a través de funciones denominadas métodos o funciones. Estas funciones son propias de cada librería, aunque algunas librerías requieran de otras para funcionar. 
# - Para invocar una librería en Python se usa la palabra reservada ‘import’, y luego, dejando un espacio, se escribe el nombre de la librería..
# 
# <center><img src="Figures/S6-Librerias.png" width="600" height="800"></center>

# # Instalando librerías
# 
# - Para utilizar una librería no instalada debe instalar usando el comando `pip`:
#     - Abrir la consola (Command prompt) como administrador 
#     - Escribir el comando: `pip install nombreLibrería`
#     - Enter y esperar a que se instale.
# - Es importante que se importen las librerías al principio del programa; de esa manera se podrán identificar más  fácilmente y serán funcionales desde el principio. 

# In[ ]:


# Archivo llamado miLibreria.py
def imprimir():
    print("Holaaaa")


# In[ ]:


import csv
import mi_libreria 

miLibreria.imprimir()


# # Ficheros
# - Hasta el momento todas las aplicaciones que hemos desarrollado son aplicaciones en las cuales los datos no persisten.
# 
# - Esto quiere decir, que luego de que ejecutamos la aplicación, empezamos a agregar datos (crear productos por ejemplo), modificar información, y realizar impresiones. Sin embargo, cuando se detiene la ejecución de la aplicación, la información y los cambios realizados durante la ejecución de la aplicación se pierden.
# 
# - En la vida real, las aplicaciones no funcionan así. Cada vez que se realiza un cambio, se agrega un producto, se elimina un producto, etc. Esa información se almacena en un fichero (archivo), o en una base de datos.
# 
# - De esta manera la información persiste, y las aplicaciones se vuelven mas confiables. 

# # Librería CSV
# - Esta librería nos permite crear, borrar, escribir y modificar fácilmente un archivo tipo tablas de Excel manejado por filas y columnas. 
# 

# In[ ]:


import csv


# ### 1. Open 
# - Python provee una función para abrir un archivo. 
# - Esa función se llama open().
# - Debemos crear un archivo llamado notas.txt en el directorio del proyecto
# - Una vez creado el archivo y asignados los valores, podemos utilizar la función open para acceder a ese archivo, y posteriormente leer la información contenida.

# In[ ]:


import csv
miArchivo = open("notas.txt")
miArchivo2 = open("notasExcel.csv")


# ### 2. Read
# Para leer la información contenida en el archivo, basta con utilizar la variable que representa el archivo, y luego invocar la función read().
# La función read() retornará un string con el contenido del archivo.

# In[ ]:


import csv
miArchivo = open("notas.txt")
notasJuntas = miArchivo.read()
print(notasJuntas)

notasSeparadas = notasJuntas.split(",")
print(notasSeparadas)


# In[ ]:


miArchivo2 = open("notasExcel.csv")
print(miArchivo2.read())

with open('C:/Users/USUARIO/Desktop/notasExcel.csv') as File:
    reader = csv.reader(File) 
    for row in reader:
        print(row)


# In[ ]:


with open('C:/Users/USUARIO/Desktop/notasExcel.csv') as File:
    reader = csv.reader(File)
    headers = next(reader)
    print(headers)
    columns = len(headers)
    s = [0]*columns
    for row in reader:
        for i in range(len(row)):
            s[i] = s[i]+float(row[i])
    print(s)


# ## 3. Write

# In[ ]:


a = [["e1","e2","e3"],[25,15,65]]
import csv
with open('prueba.csv', 'a', newline='') as file: #w: abre en modo escritura
    writer = csv.writer(file)
    for i in a:
        writer.writerow([i])


# ### Ejercicio
# - Crear el método descargarInfo() en la clase parqueadero. Está debe alamacenar la información de los vehiculos creados hasta el momento.

# In[ ]:


def descargarArchivo(self):
    with open('Parqueadero.csv', 'a', newline='') as file: #w: abre en modo escritura
            writer = csv.writer(file)
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz[0])):
                    if(self.matriz[i][j]==0):
                        writer.writerow([f"Piso {i}, Espacio {j} -> Está vacío, \n"])
                    else:
                        writer.writerow([f"Piso {i}, Espacio {j} -> {self.matriz[i][j].info()}, \n"])


# # Librería Tabulate
# - La librería tabulate nos permite extraer los datos de una lista, un diccionario o algún otro tipo de conjunto de datos y mostrarlos de manera ordenada. 
# - Para utilizar una librería no instalada debe instalar usando el comando `pip`:
#     - Abrir la consola (Command prompt) como administrador 
#     - Escribir el comando: `pip install tabulate`
#     - Enter y esperar a que se instale.

# In[ ]:


from tabulate import tabulate
tabla = [["Sol",696000,1989100000],["Tierra",6371,5973.6], ["Luna",1737,73.5],["Marte",3390,641.85]]
print(tabulate(tabla))


#Diccionario Key:value
diccionario = {"Name": ["Alice", "Bob"], 
               "Age": [24, 19]}
print(tabulate(diccionario, headers="keys"))


# Además de lo anterior, podemos agregar otro parámetro, 
# llamado tablefmt, que significa formato de tabla y trae 
# distintas formas de mostrarla: 
# "plain", "simple", "github", "grid", "fancy_grid", "pipe", 
# "orgtbl", "jira", "presto", "pretty", "psql", "rst", "mediawiki", 
# "moinmoin", "youtrack", "html", "latex", "latex_raw", "latex_
# booktabs", "textile". 

# In[ ]:


from tabulate import tabulate
table = [["spam",42],["eggs",451],["bacon",0]] 
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="plain"))


# # Pandas
# Es una herramienta de manipulación de datos de alto 
# nivel desarrollada por Wes McKinney. Es construido 
# con el paquete Numpy y su estructura de datos clave se 
# llama DataFrame. El DataFrame nos permite almacenar 
# y manipular datos tabulados en filas de observaciones y 
# columnas de variables. 
# Pandas no permite tantas modificaciones y estilos como 
# tabulate, pero hace dataFrames de una forma lógica sin 
# necesidad de usar tantos parámetros:
# 
# - Para utilizar una librería no instalada debe instalar usando el comando `pip`:
#     - Abrir la consola (Command prompt) como administrador 
#     - Escribir el comando: `pip install pandas`
#     - Enter y esperar a que se instale.

# In[ ]:


import pandas as pd

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli","Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98] }
conjunto = pd.DataFrame(dict) 
print(conjunto)


# In[ ]:


#Buscando un registro
conjunto.loc[3]

conjuntoIndices = pd.DataFrame(dict, index=['a','b','c','d','e']) 
print(conjuntoIndices)
print()
print(conjuntoIndices.loc["a"])
print()
print(conjuntoIndices.iloc[2])
print()


# # Numpy
# Es un paquete de Python y significa “Numerical Python”. 
# Es la librería principal para la informática científica, pues 
# proporciona potentes estructuras de datos implementando 
# matrices y matrices multidimensionales. Estas estructuras de 
# datos garantizan cálculos eficientes con matrices. 
# Con Numpy podemos realizar una gran variedad de 
# operaciones matemáticas y estadísticas; por ejemplo, 
# distintas operaciones con cada dato de un Array:

# In[ ]:


import numpy as np
z = np.array([5.6, 7.3, 7.7, 2.3, 4.2, 9.2])

print(z.max()) # Valor máximo de los elementos del array
print(z.min()) # Valor mínimo de los elementos del array
print(z.mean()) # Valor medio de los elementos del array
print(z.std()) # Desviación estándar de los elementos del array
print(z.sum()) # Suma de todos los elementos del array
print(np.median(z)) # Mediana de los elementos del array

