#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# Similar a una cadena que puede almacenar un grupo de caracteres, se puede utilizar un arreglo (o vector) para almacenar un grupo de números, textos y/o valores booleanos. 
# 
# Los arreglos son extremadamente útiles para:
# - Agrupar datos.
# - Reducir la definición de variables.
# - Manipulación de la información.
# - Entre otros.
# 
# Suponga que se desea almacenar el valor de 100 números enteros (edades de 100 personas). Con  lo visto hasta el momento, nos tocaría definir 100 variables numéricas, y almacenar en cada una de ellas el valor de cada edad de cada persona. Con un arreglo, podemos definir una sola variable, que contenga todas las 100 edades.

# In[ ]:


#Sin arreglos
edad1 = 34
edad2 = 25
edad3 = 16
edad100 = 32


# ## Declaración de arreglos
# Los arreglos (o listas) en Python, son un tipo de dato que se utiliza para almacenar múltiples valores asociados a una sola variable.
# 
# Para declarar un arreglo basta con: (i) definir una nueva variable, (ii) colocar el símbolo de “=“, (iii) agrupar los datos que queremos almacenar dentro de corchetes [].
# 
# Veamos el siguiente ejemplo.

# In[ ]:


edades = [34,25,16,32] #Arreglos
textos = ["Hola","grupos","82-83-84"] #Arreglos
variado = [500, "Luisa", True] #Listas
x = [] #Arreglo vacio
y = []*6 #Arreglo con 6 posiciones, sin valores de inicialización
z = [1]*3 #Arreglo con 3 posiciones, inicializados con el valor 1

print(edades)
print(textos)
print(variado)
print(x)
print(y)
print(z)


# •	Ejercicio [MiPrimerArreglo] -> Codifique el siguiente programa:
# - Solicite al usuario el tamaño del arreglo.
# - Cree un arreglo del tamaño deseado más una casilla adicional e inicialize los valores en cero.

# In[ ]:


extension=int(input("Please, enter the longitude of your first array: "))

array= [0]*(extension+1)
array[0]=extension
print(array)


# # Utilizando Arreglos
# - Crear un vector:
#     - vector = $[0]*n$
# 
# - Asignarle un valor a una posición del  vector:
#     - vector[i] = dato
# 
# - Obtener el dato de alguna posición
#     - dato =  vector[i]

# ### 1. Acceso a elementos de un arreglo
# Para acceder a un elemento individual de un arreglo, basta con colocar el nombre de la variable, seguido por corchetes [], y dentro de los corchetes colocar el índice del elemento al que se quiere acceder.
# 
# Veamos el siguiente ejemplo:

# In[ ]:


edades = [34,25,16,32]
textos = ["Hola","grupos","82-83-84"]
numeros = [500, 400, 300]

print(edades)
print(textos[0],textos[1])
print(edades[1]+numeros[0])
print(edades[-1])
print(textos[-2])
print(textos[1:])
print(textos[0:2])
#print(numeros[3]) #Ojo, si ingresa un índice que esta por fuera generará error


# •	Ejercicio [RecorriendoArreglo] -> Codifique el siguiente programa:
# - Cree una función que reciba un arreglo, ese arreglo debe recorrerlo e imprimir su contenido.
# - Invoque su función enviando la variable textos.

# In[ ]:


def imprimeVector(arreglo):
 for i in arreglo:
    print(i)

edades = [34,25,16,32]
textos = ["Hola","grupos","82-83-84"]
numeros = [500, 400, 300]
imprimeVector(numeros)
imprimeVector(textos)
imprimeVector(edades)
print(edades)


# ### 2. len(arreglo)
# Similar al uso de cadenas, podemos utilizar el método len(arreglo) para retornar el número de elementos o valores del arreglo. 
# 

# In[ ]:


numeros = [1,2,3,4,5,9]
print(len(numeros))
#Cómo obtengo la última posición?

print(numeros[-1]) #Contenido
print(len(numeros)-1) #Última posición


# ### 3. Modificar elementos de un arreglo
# Para modificar datos de un arreglo basta con especificar la posición que se quiere modificar, y luego colocar un “=“, y finalmente el nuevo valor que se desea asignar.

# In[13]:


textos = ["Hola","grupos","82-83-84"]
#textos2 = textos.copy()
textos2 = textos[:]
print(textos2)
textos2[1] = "Camila"
print(textos)
print(textos2)


# •	Ejercicio [ModificandoArreglo] -> Codifique el siguiente programa:
# - Cree una función que reciba un arreglo, una posicion inicial y una posición final.
#     - En el arreglo recibido cambie los valores de las posiciones recibidas, es decir, la posición inicial debe contener el valor de la posición final, y la final debe contener el valor de la posición inicial.
# - Finalmente, invoque la función con la variable textos.

# In[ ]:


def invertirPosicion(arreglo, inicial, final):
    temp = arreglo[inicial]
    arreglo[inicial] = arreglo[final]
    arreglo[final] = temp

edades = [34,25,16,32]
textos = ["Hola","grupos","82-83-84"]
numeros = [500, 400, 300]

print(textos[::-1])
invertirPosicion(edades,0,2)
invertirPosicion(textos,0,1)
print(edades)
print(textos)


# ### Clase Random
# Devuelve un número aleatorio entre el rango dado.

# In[ ]:


import random

print(random.randint(3, 9))

arreglo = [0]*6
print(arreglo)
arreglo[3] = random.randint(1, 5)
print(arreglo)


# •	Ejercicio [construyeArreglo2] -> Codifique el siguiente programa:
# - Cree una función que reciba un arreglo y un número(tamaño del arreglo).
# - Almacene en la primera posición del arreglo el tamaño del arreglo.
# - Utilize un ciclo para llenar el resto del arreglo con números aleatorios entre 1 a 99.
# 
# Por fuera de la función realice lo siguiente:
# - Solicite al usuario el tamaño del arreglo.
# - Cree un arreglo con el tamaño ingresado + 1, inicializando los valores en cero.
# - Invoque la función creada y finalmente imprima el resultado.

# In[ ]:


import random

def construyeArreglo(vector, longitud):
    vector[0] = longitud
    print(vector)
    for i in range(1,longitud+1):
        vector[i] = random.randint(1,99)
        
tamano = int(input("Ingrese num: "))
arreglo = [0]*(tamano+1)
print(arreglo)
construyeArreglo(arreglo,tamano)
print(arreglo)


# #### Ojo: Pasar (enviar) un objeto a un método es pasar la referencia del objeto. 
# Cuando un objeto se pasa por referencia, esto implica que cualquier cambio que se haga a ese objeto dentro del método que recibe el objeto, tomará un efecto global. 
# 

# In[ ]:


def cuadrado(x):
    x = x*x

x = 10
cuadrado(x)
print(x)


# •	Ejercicio [variableGlobal] -> Codifique el siguiente programa:
# - Modifique el anterior código para que la variable x sea global dentro de la función cuadrado y así poder realizar cambios en la variable en un contexto local.

# In[ ]:


def cuadrado():
    global x
    x = x*x

x = 10
cuadrado()
print(x)


# In[ ]:


#El arreglo a, el parámetro vector y la variable arreglo comparten la misma referencia en memoria, por lo que si modifico arreglo se modifica a
def intercambio(vector, ini, fin):
    arreglo = vector
    temp = arreglo[ini]
    arreglo[ini]=arreglo[fin]
    arreglo[fin]=temp    

a = [10, 20, 30]
intercambio(a, 0, 2)
print(a)  


# In[ ]:


#El arreglo a y el parámetro vector comparten la misma referencia en memoria, pero arreglo no, debido a que tiene una copia del arreglo
def intercambio(vector, ini, fin):
    arreglo = vector.copy()
    temp = arreglo[ini]
    arreglo[ini]=arreglo[fin]
    arreglo[fin]=temp    

a = [10, 20, 30]
intercambio(a, 0, 2)
print(a)  


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

# ### 1. Añadir elementos a un arreglo
# - A un arreglo se le pueden añadir elementos mediante la función `append` o  `insert`.
# - En la función `append`, el nuevo valor será añadido al final del arreglo. En la función `insert` se debe enviar una posición específica.
# Veamos el siguiente ejemplo:

# In[ ]:


arreglo = []
arreglo.append(600)
print(arreglo[0])

arreglo2 = [1,2]
arreglo2.append(3)
print(arreglo2[2])

arreglo2.insert(2,300)
print(arreglo2)


# #### La lógica detrás de esto

# In[ ]:


def agregarDato(d, V, n):
    if esLleno(V, n):
        return
    V[0] = V[0] + 1
    V[V[0]] = d

def insertarDato(d, i, V, n):
    if esLleno(V, n):
        return
     for j in range(V[0], i – 1, –1):
         V[j + 1] = V[j]
     V[i] = d
     V[0] = V[0] + 1


# •	Ejercicio [agregarParesArreglo] -> Codifique el siguiente programa:
# - Cree una función que no reciba parámetros. Dentro de esta:
#     - Cree un arreglo vacio
#     - Utilize un ciclo que agregue en el arreglo los números pares del 10 al 20.
#     - Devuelva el arreglo creado
# - Fuera de la función, invoque la función creada e imprima el resultado.
# 

# In[ ]:


def agregarPares():
    arreglo = []
    for i in range(10,21):
        if(i%2==0):
            arreglo.append(i)
    return arreglo

x = agregarPares()
print(x)


# #### Comprensión de la lista
# La comprensión de listas ofrece una sintaxis más corta cuando desea crear una nueva lista basada en los valores de una lista existente.

# In[ ]:


a = [x for x in range(10, 21) if x%2 != 0]
print(a)

def agregarPares():
    arreglo = []
    for x in range(10,21):
        if(x%2==0):
            arreglo.append(i)
    return arreglo

a = [x for x in range(11)] #Arreglo con una secuencia de enteros del 0 al 10
a = [i for i in range(0, 20, 3)]


# In[ ]:


frutas = ["manzana", "banana", "cherry", "kiwi", "mango"]
nueva = []

for x in frutas:
  if "a" in x:
    nueva.append(x)
print(nueva)

#**********************************************************

frutas = ["manzana", "banana", "cherry", "kiwi", "mango"]
nueva = [x for x in frutas if "a" in x]
print(nueva)


# # Iniciamos 8:05pm

# In[4]:


edades = [233,434,232,232]
x = [0]*6
d = x[1]
x[4] = 5
print(x)

x.append(7)
print(x)
x.insert(1,2)
print(x)


# •	Ejercicio [agregarParesArregloIni] -> Modifique el código para que en la primera posición almacene la cantidad de elementos creados.

# In[5]:


#Primera posición con la cantidad de elementos del arreglo
def agregarPares():
    arreglo = [0]
    for i in range(10,21):
        if(i%2==0):
            arreglo.append(i)
            arreglo[0] = arreglo[0] + 1
    return arreglo

x = agregarPares()
print(x)


# ### 2. Eliminar un elemento de un arreglo
# - Para eliminar un elemento de un arreglo se puede utilizar la función `pop` o `remove`.
# - A la función `pop` se le debe enviar la posición del elemento a eliminar. A la función `remove` se le debe enviar un valor especifico a eliminar.
# - Veamos el siguiente ejemplo:

# In[8]:


textos = ["Hola","grupos","82-83-84"]
print(textos[0])
textos.pop(0)

print(textos[0])
print(textos)

textos.remove("82-83-84")
print(textos)


# #### La lógica detrás de esto

# In[ ]:


def borrarDatoEnPosicion(i, V):
 for j in range(i, V[0]):
     V[j] = V[j + 1]
 V[0] = V[0] -1

def borrarDato(d, V):
 i = buscarDato(d, V)
 if i != -1:
    borrarDatoEnPosicion(i, V)


# In[ ]:


def buscarDato(d, V):
 i = 1
 while i <= V[0] and V[i] != d:
     i = i + 1
 if i <= V[0]:
     return i
 return -1


# ### 3. Resumen otras funciones

# In[ ]:


vector = [3, 8, 3, 6]
textos = ["Hola","grupos","82-83-84"]

vector.append(55) #añande un elemento al final del vector
textos.append("HOLA")
vector.insert(3, 777) #inserta el elemento 777 en la posición 3
vector.pop(0) #elimina elementos de la posición 0
vector.remove(4) #elimina el primer elemento con el valor 4

copia = vector.copy()#crea una copia de todo el vector
copia2 = copia
copia2.append(44)
print("Imprime vector: ",vector)
print("Imprime copia: ",copia)
print("Imprime copia2: ",copia2)

print("Imprime cantidad 4: ",vector.count(4)) #retorna el número de veces  el 4 en el vector
print("Imprime cantidad Hola: ",textos.count("Hola"))

vector.extend([4, 4, 4, 4, 4, 5]) #Agrega elementos al final del arreglo
print(vector.index(4)) #retorna la posición de la primera ocurrencia del 4 en el vector
vector.reverse() #reversa el vector, o sea que lo pone al revés
vector.sort() #ordena el vector de menor a mayor
vector.sort(reverse=True) #ordena el vector de mayor a menor
#print(vector.clear()) #elimina ttodos los elementos del vector


# # Ordenamiento de Arreglos

# ## 1. Ordenamiento por selección
# - Supongamos que desea ordenar una lista en orden ascendente. La ordenación por selección (SelectSort) encuentra el número más pequeño en la lista y lo intercambia con el primer elemento.
# - Luego encuentra el número más pequeño de la lista que queda, y lo intercambia con el segundo elemento.
# - Y así sucesivamente, hasta que queda un solo número.
# 
# <center><img src="Figures/S3-SelectionSort.png" width="300" height="400"></center>

# In[ ]:


def intercambiar(vector, ini, fin):
    temp = vector[ini]
    vector[ini]=vector[fin]
    vector[fin]=temp 

#Primera posición sin la cantidad de elementos del arreglo
def ordenaAscen(arreglo):
 for i in range(0, len(arreglo)-1):
     menor = i
     for j in range(i+1, len(arreglo)):
         if arreglo[j] < arreglo[menor]:
             menor = j
     intercambiar(arreglo, i, menor)

arreglo = [30,20,10,80,60]
ordenaAscen(arreglo)
print(arreglo)


# In[ ]:


#Primera posición con la cantidad de elementos del arreglo
def ordenaAscen(arreglo):
 longitud = arreglo[0] + 1
 for i in range(1, arreglo[0]):
     menor = i
     for j in range(i + 1, longitud):
         if arreglo[j] < arreglo[menor]:
             menor = j
     intercambiar(arreglo, i, menor)
    
arreglo = [5,30,20,10,80,60]
ordenaAscen(arreglo)
print(arreglo)


# ## 2. Ordenamiento por burbuja
# El ordenamiento burbuja ordena un arreglo en varias fases. En cada fase se intercambian sucesivamente los elementos vecinos si los elementos no están en orden.
# 
# <center><img src="Figures/S3-BubbleSort.png" width="800" height="1000"></center>

# In[ ]:


#Primera posición sin la cantidad de elementos del arreglo
def bubbleSort(arreglo):
 for i in range(0, len(arreglo)-1):
     for j in range(0, (len(arreglo)-1)-i):
         if arreglo[j] > arreglo[j + 1]:
             intercambiar(arreglo, j, j + 1)

arreglo = [2,5,9,4,8,1]
bubbleSort(arreglo)
print(arreglo)

arreglo = [30,20,10,80,60]
bubbleSort(arreglo)
print(arreglo)


# In[ ]:


#Primera posición con la cantidad de elementos del arreglo
def bubbleSort(arreglo):
 for i in range(1, arreglo[0]):
     for j in range(1, (arreglo[0]-i)+1):
         if arreglo[j] > arreglo[j + 1]:
             intercambiar(arreglo, j, j + 1)

arreglo = [6,2,5,9,4,8,1]
bubbleSort(arreglo)
print(arreglo)

arreglo = [5,30,20,10,80,60]
bubbleSort(arreglo)
print(arreglo)


# ## 3. Método sort()
# El método sort() ordena la lista de forma ascendente por defecto.

# In[9]:


arreglo = [30,20,10,80,60]
arreglo.sort()
print(arreglo)

arreglo2 = [30,20,10,80,60]
arreglo2.sort(reverse=True)
print(arreglo2)


# ## Búsqueda en arreglos

# ## 1. Búsqueda lineal o secuencial
# Respecto al proceso de búsqueda en un arreglo (a menos que esté organizado de cierta manera), lo que podemos hacer es “revisar” elemento por elemento (comúnmente de izquierda a derecha). A este proceso se le llama búsqueda lineal. 

# In[ ]:


#OPCION 1: Primera posición sin la cantidad de elementos del arreglo
def buscarDato(arreglo,d):
 i = 0
 while i <= (len(arreglo)-1) and arreglo[i]!= d:
      i = i + 1
 if i <= len(arreglo)-1:
     return i
 return -1

#OPCION 2:Primera posición sin la cantidad de elementos del arreglo
def busLineal(arreglo, d):
 pos = -1
 for x in range(len(arreglo)-1):
        if(d == arreglo[x]):
            pos = x
            break
 return pos

arreglo = [10,20,30,40,50]
print(buscarDato(arreglo,20))
print(busLineal(arreglo,20))


# In[ ]:


#Primera posición con la cantidad de elementos del arreglo
def buscarDato(d, arreglo):
 i = 1
 while i <= arreglo[0] and arreglo[i]!= d:
     i = i + 1
 if i <= arreglo[0]:
     return i
 return -1

arreglo = [5,10,20,30,40,50]
print(busLineal(arreglo,20))


# ## 2. Búsqueda binaria
# Supongamos que se tiene el siguiente arreglo “a” ordenado. Y que se desea encontrar la posición (índice) del elemento con valor 20.
# 
# |0||1 ||2||3||4|
# | --- || --- || ---|| ---|| ---|
# |10||20 ||30||40||50|
# 
# La búsqueda binaria primero comparará el valor del elemento en el medio con el valor a encontrar. Luego:
# - Si el valor a encontrar es menor que el valor del elemento central, debe continuar buscando la clave solo en la primera mitad del arreglo.
# - Si el valor a encontrar es igual al valor del elemento central, la búsqueda termina con una coincidencia.
# - Si el valor a encontrar es mayor que el valor elemento del central, debe continuar buscando la clave solo en la segunda mitad del arreglo.
# 

# En el peor escenario, cuando k = log2n, solo quedará un elemento en la matriz, y solo se necesitaría una comparación más. Por esto, en este se debe realizar log2n+1 comparaciones. 
# 
# Comparación rápida. 
# - En el peor escenario para una lista de 1024 elementos, si utilizamos búsqueda lineal, necesitaríamos 1023 comparaciones.
# - En el peor escenario para una lista de 1024 elementos (2^10), si utilizamos búsqueda binaria, solo necesitaríamos 11 comparaciones.
# 
# <center><img src="Figures/S3-Binaria.png" width="600" height="800"></center>

# In[ ]:


#Primera posición sin la cantidad de elementos del arreglo
def busBinaria(arreglo, d):
 inicio = 0
 fin = len(arreglo)-1
 while inicio <= fin:
     mitad = (inicio + fin) // 2
     if arreglo[mitad] == d:
         return mitad
     if d < arreglo[mitad]:
         fin = mitad - 1
     else:
         inicio = mitad + 1
 return -1

arreglo = [10,20,30,40,50]
print(busBinaria(arreglo,20))


# In[ ]:


#Primera posición con la cantidad de elementos del arreglo
def busBinaria(arreglo, d):
 inicio = 1
 fin = arreglo[0]
 while inicio <= fin:
     mitad = (inicio + fin) // 2
     if arreglo[mitad] == d:
         return mitad
     if d < arreglo[mitad]:
         fin = mitad - 1
     else:
         inicio = mitad + 1
 return -1

arreglo = [5,10,20,30,40,50]
print(busBinaria(arreglo,20))


# # Ejercicios

# •	Ejercicio [construyeArreglo] -> Codifique el siguiente programa:
# - Cree una función que reciba un arreglo y un número(tamaño del arreglo).
# - Utilize un ciclo para llenar el arreglo con números aleatorios entre 1 a 99.
# 
# Por fuera de la función realice lo siguiente:
# - Solicite al usuario el tamaño del arreglo.
# - Cree un arreglo con el tamaño ingresado, inicializando los valores en cero.
# - Invoque la función creada y finalmente imprima el resultado.

# In[ ]:





# •	Ejercicio [Arreglo1] -> Codifique el siguiente programa:
# - Pídale al usuario un número por pantalla
# - Pídale al usuario un texto por pantalla
# - Pídale al usuario otro número por pantalla.
# - Cree un nuevo arreglo donde la primera posición sea el primer número pedido, la segunda el texto pedido, y la tercera el segundo número pedido.
# - Imprima la primer posición del arreglo y la última por pantalla.

# In[ ]:





# •	Ejercicio [Arreglo2] -> Codifique el siguiente programa:
# - Pídale al usuario un número por pantalla.
# - Pídale al usuario un texto por pantalla.
# - Cree un arreglo donde la primera posición sea el número ingresado, la segunda el texto ingresado, y a la tercera posición añádale el número 45.
# - Imprima el valor en posición 1.
# - Elimine el elemento en la posición 1.
# - Imprima nuevamente el valor en posición 1.
# - Imprima todo el arreglo (la variable donde se almacena).

# In[ ]:




