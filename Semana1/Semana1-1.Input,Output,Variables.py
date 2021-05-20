#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción a Python

# Python es un lenguaje de escritura rápido, escalable, robusto y de código abierto, ventajas que hacen de Python un aliado perfecto para la Inteligencia Artificial.
# 
# Ahora algo de sintaxis clave en el lenguaje python:
# - Python fue diseñado para facilitar la lectura y tiene algunas similitudes con el idioma inglés con influencia de las matemáticas.
# - Python usa nuevas líneas para completar un comando, a diferencia de otros lenguajes de programación que a menudo usan punto y coma o paréntesis. Ejm:
#     - Java: System.out.println("Hola mundo")**;**
#     - Python: print("Hola mundo")    
# - Python se basa en la indentación, usando espacios en blanco, para definir el alcance; como el alcance de los bucles, funciones y clases. Otros lenguajes de programación a menudo usan corchetes para este propósito.

# ### Comentarios
# Un comentario en programación es la línea de texto en nuestro código fuente que el compilador ignora. Sirve para:
# - Anular código
# - Colocar aclaraciones

# In[ ]:


#Este programa sirve para imprimir un mensaje
print("Aprendamos a imprimir mensajes en Python")
#print("Aprendamos a imprimir mensajes en Java")
print("HOLAAAA")


# ### Indentación
# Python utiliza la indentación para delimitar la estructura permitiendo establecer bloques de código.

# In[ ]:


if 5 > 2:
  print("Hola!")


# In[ ]:


if 5 > 2:
print("Hola!") # Error al saltarse la indentación


# In[ ]:


if 5 > 2:
 print("Hola!")
        print("Hola!") #Error el número de espacios no es el mismo


# # 2. Impresiones en Python

# La función print() imprime el objeto dado en el dispositivo de salida.

# In[ ]:


print("Aprendamos a imprimir mensajes con Python")


# Ejercicio [ImprimiendoMensajes] ->
# En su ambiente, imprima 3 mensajes diferentes.

# In[ ]:





# #### Se pueden usar comillas simples, dobles y hasta triples para representar strings.

# In[ ]:


print('Texto con comillas simples')
print("Texto con comillas dobles")
print("""Texto con comillas triples""")


# #### Para separar dos declaraciones ejecutables separadas en una sola línea, debe usar un punto y coma (;) para separar los comandos.

# In[ ]:


print ("Primera Linea"); print ("Segunda Linea")


# #### Se pueden enviar varios objetos con el uso de (,)

# In[ ]:


print(4)
print("Hola","mundo")
print("Hola" +   "mundo")
print("Hola",1,3)
print(5+6)


# In[ ]:





# Ejercicio [ImprimiendoMensajes] -> En su ambiente, separe las palabras con el uso de comas.

# In[ ]:


print( "Hola", "luisa", "Hola" )


# #### Parámetros sep y end pueden cambiar la forma en que se imprimen los contenidos
# ##### Parámetro end
# Los mensajes impresos siempre culminan en un salto de línea (\n). Cambiamos este comportamiento indicando un valor alternativo vía el parámetro `end`.

# In[ ]:


print("Hola")
print("mundo")

print("Hola", end=" ")
print("mundo")

print("Hola", end="**")
print("mundo")


# ##### Parámetro Sep
# Los mensajes impresos por defecto son separados por un espacio(' '). Cambiamos este comportamiento indicando un valor alternativo vía el parámetro `sep`.

# In[ ]:


print("Hola","mundo", "!", sep="", end="-")
print("Hola","mundo", "!", sep=",")
print("Hola","mundo", "!", sep="**")
print("Hola","\nmundo", "!", sep=", ")


# Ejercicio [ImprimiendoMensajes] -> Modifique la separación de sus palabras por un &

# In[ ]:


print("Hola", "luisa", "Hola", sep= "&")


# ## Impresión de variables

# In[ ]:


a = 7+5
print(a)
print(7+5)
print('Esto es un texto literal',a)


# In[ ]:


a = 8
b = "Total = "
#print(b+a) #Error, tipos incompatibles
print(b,a)


# #### Impresión de variables con f-string
# La interpolación de cadenas es un proceso de sustitución de los marcadores de posición por los valores de una cadena literal.

# In[ ]:


a = 7
b = 5
titulo = "Total= "
print(f"{titulo} 7+5")
print(f" 7+5 = {a+b}")


# Ejercicio [ImprimiendoMensajes2]
# 
# Se tienen las siguientes variables a = "planetas" y b = "celestes".
# 
# Imprima el siguiente mensaje usando f-string: los planetas son cuerpos celestes

# In[ ]:


a = "planetas"
b = "celestes"
print(f"los {a} son cuerpos {b}")


# Ejercicio [ImprimiendoMensajes3]
# 
# Se tienen las siguientes variables a = 5 y b = 8.
# 
# Imprima el siguiente mensaje usando f-string: El resultado de multiplicar 5 y 8 es 40.

# In[ ]:


a = 9
b = 8
c = a*b
print(f"El resultado de multiplicar {a} y {b} es {a*b}")
print(f"El resultado de multiplicar {a} y {b} es {c}")


# #### Impresión de variables con str.format()
# Es una forma más elegante que el f-string

# In[ ]:


a = 7
b = 5

print("Imprimir dos variables con format {} y {}".format(a,b))
print("Imprimir dos variables con format {0} y {1}".format(a,b))
print("Imprimir dos variables con format {1} y {0}".format(a,b))
print("Imprimir dos variables con format {v1} y {v2}".format(v1=a,v2=b))
print("Imprimir dos variables con format {0},{1}, y {otro}".format(a,b,otro="gato"))


# # 3. Variables
# Es el nombre que se le asigna, dentro de un programa, a una posición de memoria con el fin de poder manipular el dato almacenado en dicha posición.

# In[ ]:


#Creando variables
nombre = "Luisa"
edad = 2

print(f"La edad de {nombre} es {edad}")


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

print(type(x))
print(type(y))


# Revise el siguiente código: ¿Algún comentario?

# In[ ]:


nombre = "luisa"
edad = 28
salario = 4.5
ext = 0.2
g = z+ext


# #### Reglas para variables de Python:
# - El nombre de una variable debe comenzar con una letra o el carácter de subrayado
# - Un nombre de variable no puede comenzar con un número
# - El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _)
# - Los nombres de las variables distinguen entre mayúsculas y minúsculas (la edad, la Edad y la EDAD son tres variables diferentes)

# In[ ]:


minombre = "luisa"
mi_nombre = "luisa"
_mi_nombre = "luisa"
miNombre = "luisa"
MINOMBRE = "luisa"
miNombre1 = "luisa"

#2minombre = "luisa" # Error
#mi-nombre = "luisa" #Error
#mi nombre = "luisa" #Error


# In[ ]:


#Variables son case-sensitive
a = 4
print(a)
A = "Sally"
print(A)


# #### Nombre de variables con múltiples palabras
# Los nombres de variables con más de una palabra pueden resultar difíciles de leer.
# 
# Hay varias técnicas que puede utilizar para hacerlos más legibles:

# In[ ]:


# Camel Case
primerNombre = "luisa" #La que usaremos en el curso
# Pascal Case
PrimerNombre = "luisa"
# Snake Case
primer_nombre = "luisa"


# #### Tipos númericos

# In[ ]:


miVariableEntera = 4
miVariableReal = 4.0
multiplicación = 3.1 * -2
print(miVariableEntera)
print(miVariableReal)
print(multiplicación)
print("La suma de dos variables: ", miVariableEntera+miVariableReal)


# •	Ejercicio [VariablesNumericas]
# - Cree tres variables enteras:
#     - Una para la edad de Bill Gates
#     - Otra para la edad de Mark Zuckerberg.
#     - Otra para la edad de Mariana Pajón.
# - Encuentre el promedio de las 3 edades anteriores.
# - Imprima el resultado por pantalla.

# In[ ]:





# #### Tipos String o textos
# - Las variables de tipo string se utilizan para almacenar texto, o cadenas de caracteres.
# - Si queremos almacenar un texto, basta con escribir el texto que se desee almacenar entre comillas y asignarle una variable.
# 

# In[ ]:


string1 = "Hola"
string2 = "Beneficiario"
stringDeNumeros = "156465454"
print(string1)
print(string2)
print(stringDeNumeros)
print("Strings combinados: ",string1,string2,stringDeNumeros)


# •	Ejercicio [SolicitudInfo2]
# - Cree tres variables tipo string:
#     - Una para su nombre
#     - Otra para su apellido
#     - Otra para su edad
# - Finalmente, imprima todos esos datos por pantalla.

# #### Operaciones con strings
# str (String) es una clase propia de python y provee una serie de funciones que son muy útiles.
# 
# str funciona como un arreglo (conjunto de variables del mismo tipo que se citan y manejan con un mismo nombre). Si definimos x = "Hola mundo", internamente Python almacena ese texto de la siguiente manera (como un arreglo)
# 
#         x = "Hola mundo"
# 
# |H||o||l||a|| ||m||u||n||d||o|
# | --- || --- || --- || --- || --- || --- || --- || --- || --- || --- |
# |0||1||2||3|| 4||5||6||7||8||9|  
# 
# El número se conoce como posición o índice.

# ##### 1. Concatenación
# Una de las operaciones mas útiles cuando se trabaja con Strings es la concatenación. Esta operación se realiza mediante el uso del símbolo “+”. Dos Strings pueden ser combinados para crear un nuevo String.
# Consideremos el siguiente ejemplo:
# 

# In[ ]:


a = "Hola luisa"
b = ", cómo estás?"

print(a+b) #Concatenación


# ##### 2. Longitud
# Podemos usar el método len(str) para retornar el número de caracteres del String str. 
# 

# In[ ]:


a = "Hola luisa"
print(len(a)) 
print(len(a)-1) 


# In[ ]:


texto1 = "Hola beneficiarios "
tamano = len(texto1)
print(tamano)

texto2 = "Hola"
tamano2 = len(texto1+texto2)
print(tamano2)


# ##### 3. Extraer un carácter
# Dado que los Strings en Python son arreglos, extraer un carácter especifico resulta muy sencillo. Basta con coloca el nombre de la variable que almacena el String, luego corchetes [] y dentro de los corchetes la posición del carácter que queremos extraer.

# In[ ]:


a = "Hola luisa"
print(a[1]) #Obtener el caracter en determinada posición


# In[ ]:


texto1 = "Hola beneficiarios"
p0 = texto1[0]
p3 = texto1[3]
pfinal = texto1[len(texto1)-1]
print(p0)
print(p3)
print(pfinal)


# Ejercicio [ModificarString]
# - Cree una variable con un texto
# - Imprima la longitud del texto.
# - Imprima la última posición de la cadena
# - Imprima el primer carácter de la cadena
# - Imprima el último carácter de la cadena

# In[ ]:





# ##### 4. Extraer una cadena de una cadena
# Si queremos extraer no un carácter, si no múltiples caracteres de una cadena, podemos utilizar los corchetes [] y dentro definir, la posición inicial desde la cual queremos empezar a extraer, luego le siguen dos puntos “:” y luego la posición final + 1 hasta la cual queremos extraer.

# In[ ]:


a = "Hola luisa"
print(a[2:5]) #Cortar una cadena
print(a[:5]) #Cortar una cadena


# ##### 5. Encontrar un carácter
# Para encontrar un carácter en una cadena, o una cadena dentro de otra cadena, se puede utilizar la función str.find(str2). Esta función retorna la posición en la que aparece por primera vez el String str2, dentro del String str. O retorna -1 si no se encuentra.

# In[ ]:


a = "Hola luisa"
print(a.find("a")) #Retorna la posición en donde se encuentra el string
print(a.find("a",4)) #Retorna la posición en donde se encuentra el string, despues de esa posición

busquedad1 = a.find("a")
print(a.find("a",busquedad1+1))

print(a.find("lui"))

print("free" in a) #Validar si una palabra existe en la cadena inicial
print("expensive" not in a) #Validar si una palabra no existe en la cadena inicial


# ##### 6. Contar
# La función str.count(str2) se utiliza para encontrar cuantas veces aparece el String str2, dentro del String str.

# In[ ]:


a = "Hola luisa"
print(a.count("a")) #Encontrar cuantas veces aparece la letra a
print(a.count("lu"))


# ##### Modificando strings
# - Podemos usar el método str.lower() para retornar el String str en minúsculas. 
# - Podemos usar el método str.upper() para retornar el String str en mayúsculas. 
# - Podemos usar el método str.replace(a,b) para retornar el String str pero reemplazándole todos los texto que coindicen con a, por los textos b.
# - Podemos usar el método srt.strip() para eliminar los espacios al inicio y al final de la cadena.

# In[ ]:


a = " Hola luisa "
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))
print(a.strip())


# Ejercicio [ModificarString]
# - Cree una variable con un texto
# - Obtenga la longitud del texto.
# - Imprima la posición donde se encuentra la primera "a"
# - Imprima la posición de donde se encuentra la segunda letra "a" en el texto recibido.
# - Imprima el primer carácter de la cadena
# - Imprima el último carácter de la cadena
# 

# In[ ]:





# #### Booleanos
# - Son variables que almacenan un valor de True o False. Generalmente utilizadas para almacenar resultados de comparaciones (se ve más adelante).
# - Note que Python tiene reservadas las palabras True y False (Ojo: la inicial de True y False es en mayúscula).

# In[ ]:


x = True
y = False
print("x es: ", x)


# #### Convirtiendo Variables
# Al programar, hay ocasiones en las que necesitamos convertir valores entre tipos para manipular los valores de una manera diferente. Por ejemplo, es posible que necesitemos concatenar valores numéricos con cadenas o representar posiciones decimales en números que se inicializaron como valores enteros.

# In[ ]:


inicial = 3
x = str(inicial)    # x será '3'
y = int(inicial)    # y será 3
z = float(inicial)  # z será 3.0
print(x)
print(y)
print(z)


# In[ ]:


inicial = "hola"
#x = int(inicial) #Error
print(x)

inicial2 = "3"
x2 = int(inicial2) #Valido
print(x2)


# Ejercicio [ConvirtiendoVariables]
# - Cree una variable con un texto que contenga números.
# - Convierta ese texto a entero e imprima el resultado.
# - Convierta ese texto a real e imprima el resultado.

# In[ ]:





# # 4. Recibir datos en Python

# La función input() permite a los usuarios introducir datos de distintos tipos desde la entrada estándar (teclado).

# In[ ]:


Dato = input("Escriba el dato1")
print(Dato)


# Ejercicio [SolicitudInfo]
# - Cree un programa que solicite:
#     - Primero el nombre y lo guarde en una variable nombre
#     - Segundo el apellido y lo guarde en una variable apellido
# - Finalmente, imprima todos esos datos por pantalla.

# In[ ]:





# #### Uso de input() con f-string

# In[ ]:


nombre = input("Dígite su nombre")
apellido = input(f"ahora {nombre} Dígite su apellido")
print("Nombre:", nombre, "Apellido:", apellido)


# #### El input() por defecto recibe todo como string (texto).

# In[ ]:


edad = input("Dígite su edad")
print(type(edad))


# In[ ]:


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


# # 5. Ejercicios

# •	Ejercicio [SolicitudInfo3]
# - Cree un programa que le solicite al usuario:
#     - Sus nombres y apellidos (guárdelos como String)
#     - Su fecha de nacimiento (guárdela como String)
#     - Su edad (guárdela como int)
#     - Su estatura (guárdela como float)
# - Finalmente, imprima todos esos datos por pantalla.

# In[ ]:





# •	Ejercicio [area-circulo]
# -	Pídale al usuario el radio de un círculo (float)
# -	Calcule el área del circulo (area = 3.14 * radio * radio)
# -	Imprima por pantalla el área
# 

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





# •	Ejercicio [peso]
# 
# Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (imc).
# fórmula imc = peso / altura al cuadrado.
# 

# •	Ejercicio [pulgadas]
# 
# Escriba un programa que pida una distancia en pulgadas y que escriba esa distancia en centímetros. Una pulgada son 2,54 cm

# •	Ejercicio [celsius-farenheit]
# 
# Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit.
# $F = 1,8 * C + 32 $

# •	Ejercicio [segundos]
# 
# Escriba un programa que pida una cantidad de segundos y que escriba cuántos horas y minutos son. 
