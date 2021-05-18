#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción a Python

# Python es un lenguaje de escritura rápido, escalable, robusta y de código abierto, ventajas que hacen de Python un aliado perfecto para la Inteligencia Artificial.
# 
# Ahora algo de sintaxis clave en el lenguaje python:
# - Python fue diseñado para facilitar la lectura y tiene algunas similitudes con el idioma inglés con influencia de las matemáticas.
# - Python usa nuevas líneas para completar un comando, a diferencia de otros lenguajes de programación que a menudo usan punto y coma o paréntesis.
# - Python se basa en la indentación, usando espacios en blanco, para definir el alcance; como el alcance de los bucles, funciones y clases. Otros lenguajes de programación a menudo usan corchetes para este propósito.

# ### Comentarios
# - Anular código
# - Colocar aclaraciones
# - Fácil entendimiento

# In[ ]:


print("Aprendamos a imprimir mensajes en Python")
#print("Aprendamos a imprimir mensajes en Java")


# ### Indentación
# Python utiliza la indentación para delimitar la estructura permitiendo establecer bloques de código.

# In[ ]:


if 5 > 2:
  print("Hola!")

if 5 > 2:
print("Hola!") # Error al saltarse la indentación

if 5 > 2:
 print("Hola!")
        print("Hola!") #Error el número de espacios no es el mismo


# # 2. Impresiones en Python

# In[ ]:


print("Aprendamos a imprimir mensajes con Python")


# #### Se pueden usar comillas simples, dobles y hasta triples para representar strings.

# In[ ]:


print('Texto con comillas simples')
print("Texto con comillas dobles")
print("""Texto con comillas triples""")


# #### Para separar dos declaraciones ejecutables separadas en una sola línea, debe usar un punto y coma (;) para separar los comandos.

# In[ ]:


print ("Primera Linea"); print ("Segunda Linea")


# #### Se pueden unir palabras con (+) ó (,). Lo más recomendable es usar (,)

# In[ ]:


print("Hola","mundo")
print("Hola"+"mundo")


# #### Parámetros sep y end pueden cambiar la forma en que se imprimen los contenidos
# ##### Parámetro end

# In[ ]:


print("Hola",)
print("mundo")

print("Hola", end=" ")
print("mundo")

print("Hola", end="**")
print("mundo")


# ##### Parámetro Sep

# In[ ]:


print("Hola","mundo", "!", sep="")
print("Hola","mundo", "!", sep=",")
print("Hola","mundo", "!", sep="**")
print("Hola","\nmundo", "!", sep=", ")


# ##Impresión de variables

# In[ ]:


a = 7+5
print(a)
print(7+5)
print("Esto es un texto literal",a)


# In[ ]:


a = 8
b = "Total = "
#print(b+a) #Error, tipos incompatibles
print(b,a)


# ##Impresión de variables con f-string

# In[ ]:


a = 7
b = 5
titulo = "Total = "
print(f"{titulo} 7+5")
print(f" 7+5 = {a+b}")


# ##Impresión de variables con str.format()

# In[ ]:


a = 7
b = 5
titulo = "Total = "

print("Imprimir dos variables con format {} y {}".format(a,b))
print("Imprimir dos variables con format {0} y {1}".format(a,b))
print("Imprimir dos variables con format {1} y {0}".format(a,b))
print("Imprimir dos variables con format {v1} y {v2}".format(v1=a,v2=b))
print("Imprimir dos variables con format {0},{1}, y {otro}".format(a,b,otro="gato"))


# # 3. Recibir datos en Python

# In[ ]:


Dato1 = input("Escriba el dato1")
print(Dato1)


# #### Uso de input() con f-string

# In[ ]:


nombre = input("Dígite su nombre")
apellido = input(f"ahora {nombre} Dígite su apellido")
print("Nombre:", nombre, "Apellido:", apellido)


# In[ ]:


edad = input("Dígite su edad")
print(type(edad))

edad = int(input("Dígite su edad"))
operacion = edad +2;
print(operacion)


# In[ ]:


a = input("Entre un número")
b = input("Entre otro número")
print(a+b)

a = int(input("Entre un número"))
b = int(input("Entre otro número"))
print(a+b)

a = float(input("Entre un número"))
b = float(input("Entre otro número"))
print(a+b)


# # 4. Variables

# - En programación, el tipo de datos es un concepto importante.
# - Las variables pueden almacenar datos de diferentes tipos y diferentes tipos pueden hacer cosas diferentes.
# - Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:
# 
#     - Tipo de texto:	str
#     - Tipos númericos:	int, float, complex
#     - Tipos de secuencia:	list, tuple, range
#     - Tipo de mapeo:	dict
#     - Tipo de conjunto:	set, frozenset
#     - Tipo booleano:	bool
#     - Tipos binarios:	bytes, bytearray, memoryview

# ### Declaración de variables
# - Para declarar una variable, primero debemos darle un nombre cualquiera a la variable utilizando letras y números sin espacios, teniendo en cuenta que las mayúsculas importan. 
# - Luego de darle un nombre a la variable, se le asigna un valor por medio del operador “=”. 
# - De esta forma, el programa puede separar un bloque de memoria para la variable y guardar en dicho bloque el valor de esta. 
# - A diferencia de otros lenguajes de programación, en Python no se puede declarar una variable sin asignarle un valor.

# In[ ]:


#Creando variables
x = 5
y = "Luisa"

print(x, type(x))
print(y, type(y))


# #### Tipos númericos

# In[ ]:


miVariableEntera = 4
miVariableReal = 4.0
multiplicación = 3.1 * -2
print(miVariableEntera)
print(miVariableReal)
print(multiplicación)
print("La suma de dos variables: ", miVariableEntera+miVariableReal)


# In[ ]:





# #### Tipos String o textos
# - Las variables de tipo string se utilizan para almacenar texto, o cadenas de caracteres.
# - Si queremos almacenar un texto, basta con escribir el texto que se desee almacenar entre comillas y asignarle una variable.

# In[ ]:


string1 = "Hola"
string2 = "Beneficiario"
stringDeNumeros = "156465454"
print(string1)
print(string2)
print(stringDeNumeros)
print("Strings combinados: ",string1,string2,stringDeNumeros)


# #### Booleanos
# - Son variables que almacenan un valor de True o False. Generalmente utilizadas para almacenar resultados de comparaciones (se ve más adelante).
# - Note que Python tiene reservadas las palabras True y False.

# In[ ]:


x = True
y = False
print("x es: ", x)


# Ojo: la inicial de True y False es es mayúscula. 

# In[ ]:


#Conviritiendo variables
inicial = 3
x = str(inicial)    # x will be '3'
y = int(inicial)    # y will be 3
z = float(inicial)  # z will be 3.0
print(x)
print(y)
print(z)


# In[ ]:


#Variables son case-sensitive
a = 4
print(a)
A = "Sally"
print(A)


# # 5. Ejercicios

# •	Ejercicio [VariablesNumericas]
# - Cree tres variables:
#     Una para la edad de Bill Gates
#     Otra para la edad de Mark Zuckerberg.
#     Otra para la edad de Mariana Pajón.
# - Encuentre el promedio de las 3 edades anteriores.
# - Imprima el resultado por pantalla.

# In[ ]:





# •	Ejercicio [SolicitudInfo]
# - Cree un programa que le solicite al usuario:
#     Sus nombres y apellidos (guárdelos como String)
#     Su fecha de nacimiento (guárdela como String)
#     Su edad (guárdela como int)
#     Su estatura (guárdela como float)
# - Finalmente, imprima todos esos datos por pantalla.

# In[ ]:





# •	Ejercicio [area-rectangulo]
# -	Pídale al usuario por pantalla la base de un rectángulo (float)
# -	Pídale al usuario por pantalla la altura de un rectángulo (float)
# -	Calcule el área del rectángulo (base*altura) -> asigne el resultado a una nueva variable (declaración)
# -	Muestre el resultado por pantalla
# 

# In[ ]:





# •	Ejercicio [edad]
# -	Pídale al usuario por pantalla el año en el que nació (ingrese números ej: 1990) (int)
# -	Pídale al usuario por pantalla el nombre (string)
# -	Calcule la edad del usuario
# -	Muéstrele por pantalla la edad al usuario
# 

# In[ ]:





# •	Ejercicio [asteroides]
# -	Pídale al usuario un numero de asteroides (int)
# -	Pídale al usuario un nombre para todos los asteroides (string)
# -	Imprima por pantalla lo siguiente: “Los NUMERO_ASTEROIDES asteroides NOMBRE_ASTEROIDES caerán mañana”. (Nota reemplace NUMERO_ASTEROIDES y NOMBRE_ASTEROIDES por los valores recogidos por pantalla)
# 

# In[ ]:





# •	Ejercicio [area-circulo]
# -	Pídale al usuario el radio de un círculo (float)
# -	Calcule el área del circulo (area = 3.14*radio*radio)
# -	Imprima por pantalla el área
# 

# In[ ]:




