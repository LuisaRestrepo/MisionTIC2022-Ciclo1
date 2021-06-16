#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# En Python, cualquier tabla se puede representar como un arreglo de arreglos (un arreglo, donde cada elemento es a su vez un arreglo)
# 
# <center><img src="Figures/S4-DistanceTable.png" width="800" height="1100"></center>

# In[ ]:


distances = [
[0,    983,  787, 714, 1375, 967, 1087],
[983,  0,    214, 1102, 1763, 1723, 1842],
[787,  214,  0, 888, 1549, 1548, 1627],
[714,  1102, 888, 0, 661, 781, 810],
[1375, 1763, 1549, 661, 0, 1426, 1187],
[967,  1723, 1548, 781, 1426, 0, 239],
[1087, 1842, 1627, 810, 1187, 239, 0],
]

print(distances)
print(distances[0])
print(distances[1])
print(distances[1][0])


# ## Declaración de arreglos de dos dimensiones
# Veamos el siguiente ejemplo.

# In[ ]:


edadesEmpresa = [[34,25,16,32],
                 [34,13,76,23]] # Arreglo simétrico
edadesEmpresa2 = [[34,25,16,32], 
                  [34,13,76]   ] # Arreglo asimétrico


# ### 1. Primera forma:
# Puede crear una lista de n elementos (por ejemplo, de n ceros) y luego hacer que cada uno de los elementos sea un enlace a otra lista unidimensional de m elementos:

# In[ ]:


f = 2
c = 3
a = [0] * f
for i in range(f):
    a[i] = [0] * c
print(a)


# ### 2. Segunda forma:
# Otra forma (pero similar): crear una lista vacía y luego append un nuevo elemento n veces (este elemento debe ser una lista de longitud m ):

# In[ ]:


f = 2
c = 3
a = []
for i  in range(f):
    x = [0] * c
    a.append(x)
print(a)


# ### 3. Tercera forma:
# Pero la forma más fácil es usar generator, creando una lista de n elementos, cada uno de los cuales es una lista de m ceros:

# In[ ]:


f = 6
c = 3
a = [[0]*c for i in range(f)]
print(a)


# <center><img src="Figures/S4-FilasColumnas.png" width="500" height="800"></center>

# # Utilizando los arreglos de dos dimensiones

# ## Métodos que se pueden usar con arreglos (o listas)
# 
# |Método||Descripción|
# | --- || --- |
# |append()||Agrega un elemento al final de la lista|
# |clear()||Elimina todos los elementos de la lista|
# |copy()||Devuelve una copia de la lista|
# |count()||Devuelve el número de elementos con el valor especificado|
# |extend()||Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual|
# |index()||Devuelve el índice del primer elemento con el valor especificado|
# |insert()||Agrega un elemento en la posición especificada|
# |pop()||Elimina el elemento en la posición especificada|
# |remove()||Elimina el primer elemento con el valor especificado|
# |reverse()||Invierte el orden de la lista|
# |sort()||Ordena la lista|

# ### 1. Acceso a elementos de un arreglo
# Para acceder a un elemento individual de un arreglo, basta con colocar el nombre de la variable, seguido por dos corchetes [][], y dentro de los corchetes colocar los indices del elemetos al que se quiere acceder.
# 
# <center><img src="Figures/S4-Asignacion.png" width="500" height="800"></center>
# 
# Veamos el siguiente ejemplo:

# In[6]:


edadesEmpresa = [[34,25,16,32],[34,13,76,23]]
print(edadesEmpresa)
print(edadesEmpresa[0])
print(edadesEmpresa[0][1])
print(len(edadesEmpresa))
print(len(edadesEmpresa[0]))
print(len(edadesEmpresa[1]))

edadesEmpresa2 = [[34,25,16,32],[34,13,76]]
print(len(edadesEmpresa2))
print(len(edadesEmpresa2[0]))
print(len(edadesEmpresa2[1]))


# In[7]:


edadesEmpresa2 = [[34,25,16,32],[34,13,76]]

#Recorriendo matriz por filas
for i in range(len(edadesEmpresa2)):
    for j in range(len(edadesEmpresa2[i])):
        print(f"Valor en la posición i={i}, j={j} ->{edadesEmpresa2[i][j]}")


# In[10]:


edadesEmpresa2 = [[34,25,16,32],[34,13,76]]

#Recorriendo matriz por columnas
for i in range(len(edadesEmpresa2[0])):
    for j in range(len(edadesEmpresa2)):
        try:
            print(f"Valor en la posición j={j}, i={i} ->{edadesEmpresa2[j][i]}")
        except IndexError: 
            print(f"Valor en la posición j={j}, i={i} -> Esta vacía")


# ## 2. Modificar elementos de un arreglo de dos dimensiones
# Para modificar datos de un arreglo basta con especificar la posición que se quiere modificar, y luego colocar un “=“, y finalmente el nuevo valor que se desea asignar.

# In[11]:


f = 6
c = 3
a = [[0]*c for i in range(f)]
print(a)

a[2][1] = 7
print(a)

#¿Dónde coloca el valor?


# <center><img src="Figures/S4-FilasColumnasValor.png" width="500" height="800"></center>

# ### Llenando una matriz con input

# In[12]:


f = int(input("Cuántas empresas?"))
c = int(input("Cuántos empleados?"))
matriz = [[0] * c for i in range(f)]
print(matriz)

for i in range(f):
    for j in range(c):
        valor = int(input(f"Ingrese el valor para la empresa {i}, empleado{j}"))
        matriz[i][j] = valor
        
print(matriz)


# •	Ejercicio [PromedioEmpleado] -> Codifique el siguiente programa:
# 
# - Modifique el anterior programa para que muestre el promedio de edades de los trabajadores de cada empresa.
# 

# In[13]:


f = int(input("Cuántas empresas?"))
c = int(input("Cuántos empleados por empresa?"))
matriz = [[0] * c for i in range(f)]
print(matriz)

for i in range(f):
    suma = 0
    for j in range(c):
        valor = int(input(f"Ingrese el valor para la empresa {i}, empleado{j}"))
        matriz[i][j] = valor
        suma = suma + matriz[i][j]
    promedio = suma / c
    print(f"El promedio de la empresa {i} es {promedio}")
    
print(matriz)


# •	Ejercicio [PromedioEmpleado2] -> Codifique el siguiente programa:
# 
# - Debe crear una función llamada calcularPromedio(int[] edades); el cual recibe un arreglo de edades. Y retorna el promedio de las edades (double).
# 
# - Cree un for que recorre las empresas e invoque ese método desde el for cree construyo, y verifique que el programa funciona igual que el ejercicio 1.

# In[15]:


def calcularPromedio(empresas):
    suma = 0
    for i in empresas:
        suma = suma + i
    return suma/len(empresas)

f = int(input("Cuántas empresas?"))
c = int(input("Cuántos empleados?"))
matriz = [[0] * c for i in range(f)]
print(matriz)

for i in range(f):
    for j in range(c):
        valor = int(input(f"Ingrese el valor para la empresa {i}, empleado{j}"))
        matriz[i][j] = valor
        
# For que recorra filas y mande cada fila a la función calcular promedio, se imprime el resultado
for i in range(f):
    print("Empresa", i)
    x = calcularPromedio(matriz[i])
    print("Edad promedio", x)
        
print(matriz)


# # Operaciones con matrices
# Usar la clase matriz o usar la libreria numpy.
# 
# - Para utilizar numpy debe intalar la librería:
#     - Abrir la consola (Command prompt) como administrador 
#     - Escribir el comando: `pip install numpy`
#     - Enter y esperar a que se instale.

# In[16]:


import numpy as np

edadesEmpresa2 = np.array([[34,25,16,32],[34,13,76,76]])
print(edadesEmpresa2)
print("Número de filas", len(edadesEmpresa2))
print("Número de columnas", len(edadesEmpresa2[0]))


# In[19]:


import numpy as np
#Sumar todo
a = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])
print(np.sum(a))

# Sumar filas
a = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])
print(np.sum(a, axis = 1))

#Sumar columnas
a = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])
print(np.sum(a, axis = 0)) 


# In[20]:


# Transpuesta
a = np.array([[3,1,6,2,8],[9,7,7,2,1],[4,1,2,2,5],[7,5,4,4,1]])
print(a)

print(a.transpose())


# In[21]:



#Suma de dos matrices
a = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])
b = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])

print(np.add(a,b))


# In[22]:


#Producto diagonal
a = np.array([[3,12,55,1,3],[1,9,6,1,6],[4,1,2,2,5],[7,5,4,4,1]])
print(a.diagonal())
print(a.diagonal().prod())


# In[23]:


#Multiplicación de dos matrices
a = np.array([[3,12,55,1],[1,9,6,1],[4,1,2,2],[7,5,4,4]])
b = np.array([[3,12,55,1],[1,9,6,1],[4,1,2,2],[7,5,4,4]])

print(np.dot(a,b))


# In[25]:


a = np.array([[3,12,55,1],[1,9,6,1],[4,1,2,2],[7,5,4,4]])

#Matriz triangular superior
print(np.triu(a))
print(np.triu(a).sum())

#Matriz triangular extrictamente superior
print(np.triu(a,1))
print(np.triu(a).sum())


#Matriz triangular inferior
print(np.tril(a))
print(np.tril(a).sum())

#Matriz triangular extrictamente inferior
print(np.tril(a,-1))
print(np.tril(a,-1).sum())


# # Ejercicios

# •	Ejercicio [ArregloEmpleados] -> Codifique el siguiente programa:
# - Cree un método de clase en la clase PrincipalEmpleado. 
# 
# - Ese método recibirá un arreglo de empleados, y retornará un valor double (el cual contiene el valor del mayor salario).
# 
# - Modifique el método main para imprimir ese mayor salario.

# In[ ]:


class Empleado:
    def __init__(self, n, s):
        self.nombre = n
        self.salario = s

