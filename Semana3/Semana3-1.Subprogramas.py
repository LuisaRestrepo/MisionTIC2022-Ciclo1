#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# En ocasiones, es necesario realizar tareas similares en diferentes partes de un programa, pero con valores diferentes; por ejemplo calcular el factorial de un número o mostrar una palabra al revés o decidir si un número es primo.
# 
# Complejidad de los programas reales.
# - Divide y vencerás.
# - Evitar repeticiones 
# - DRY (Don´t Repeat Yourself) 
# 
# <img src="Figures/S3-DRY.png" width="1200" height="1200">
# 
# 

# En el siguiente código el cliente no quiere que salga por pantalla el mensaje “el precio del producto…”, si no, “Precio producto 1 es: ”.

# In[ ]:


p1 = 100
p2 = 200
p3 = 350
p4 = 250

print("El precio del producto 1 es", p1)
print("El precio del producto 2 es", p2)
print("El precio del producto 3 es", p3)
print("El precio del producto 4 es", p4)


# Pero suponga que ya no son 4 productos si no 400 productos. ¿Qué tocaría hacer?

# ## Funciones o subprogramas
# En ese caso podemos escribir subprogramas que son fragmentos aislados de código que disminuyen la complejidad de un programa y evitan reescribir código innecesariamente.
# 
# - Las funciones son esencialmente, bloques reutilizables de código.
# - Utilizar funciones permite modularizar los programas.
# - Ahora, un programa complejo, se puede dividir en una serie de partes o bloques más simples.
# - El uso de funciones provee una serie de ventajas:
#     - Se facilita la programación.
#     - Se reutiliza el código.
#     - Se reducen la cantidad de líneas de código.
#     - Se facilita el proceso de encontrar errores.
#     - Se mejora la mantenibilidad.
#     - Entre otros.

# Las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una definición de función sin contenido, coloque la instrucción `pass` para evitar errores.

# In[ ]:


def myfunction():
  pass


# ## Creando una función
# - Una función en Python es un bloque de código con un nombre asociado.
# - La función recibe cero o más parámetros.
# - Luego la función contiene un cuerpo en el cual se ejecutan una serie de instrucciones. 
# - Finalmente, la función puede retornar un valor.

# In[ ]:


#Función sin parámetros y sin retorno
def nombreFuncion():
    print("Hola amigo")
    
nombreFuncion()


# •	Ejercicio [HolaAmigo] 
# - Ahora en lugar de imprimir “Hola mundo” -> imprima “Hola amigo” 5 veces.
# 

# ## Función con parámetros
# Un parámetro es un valor que la función espera recibir cuando sea llamada (invocada), a fin de ejecutar acciones en base al mismo. Una función puede esperar uno o más parámetros (que irán separados por una coma) o ninguno.

# In[ ]:


#Función con parámetros y sin retorno
def imprimirPrecio(num:int, precio:int):
    print(f"Precio producto {num}, es {precio}")
    
imprimirPrecio(1,200)
p2 = int(input()) 
imprimirPrecio(2,p2)


# •	Ejercicio [AreaRectangulo] -> Codifique el siguiente programa:
# - Cree una funcion que reciba dos parámetros, dentro de la función imprima el resultado de multiplicar estos.
# - Por fuera de la función:
#     - Solicite repetidamente al usuario que ingrese la base y la altura de un rectángulo.
#     - Cada vez que lo haga invoque la función creada con los datos ingresados.

# In[ ]:


def imprimirArearectangulo(base, altura):
    print(f"El area es {base * altura}")

i = 0
while i < 3:
    base = float(input("ingrese la base: "))
    altura = float(input("ingrese la altura: "))
    imprimirArearectangulo(base, altura)
    i += 1


# In[ ]:


def imprimirArearectangulo():
    base = int(input("ingrese la base: "))
    altura = int(input("ingrese la altura: "))
    print(f"El area es {base * altura}")

i = 0
while i < 3:
    imprimirArearectangulo()
    i += 1


# ## Sobre los parámetros

# ##### 1. El orden y la cantidad importa

# In[ ]:


#Función con parámetros y sin retorno
def imprimirInfo(nombre, numero):
    print(f"Info nombre: {nombre},numero: {numero}")
    
imprimirInfo("Lola",200) 
imprimirInfo(200,"Lola")


# ##### 2. Es posible, asignar valores por defecto a los parámetros de las funciones.

# In[ ]:


#Función con parámetros, sin retorno y con valores por defecto
def imprimirInfo(nombre, numero = 123): #Valor por defecto
    print(f"Info {nombre},{numero}")
    
imprimirInfo("Lola",200)
imprimirInfo(200,"Lola")
imprimirInfo("Lola")


# ##### 3. Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función. Ojo: Estos argumentos, llegarán a la función en forma de tupla.

# In[ ]:


def miFuncion(*datos):
  contador = 0
  for x in datos: 
        contador +=1
  print("El último dato es ",datos[contador-1])

miFuncion("Hola", "beneficiarios", ":)")
miFuncion(1, 2, 3)


# •	Ejercicio [FuncionSuma] -> Codifique el siguiente programa:
# - Cree una función que recibe un cantidad desconocida de parámetros.
# - Dentro de esta función construya un ciclo que sume los parámetros recibidos, e imprima el resultado.
# - Por fuera de la función, invoque la función enviandole x cantidad de argumentos.

# In[ ]:


def mifuncion(*parametros):
  suma = 0
  for x in parametros:
      print(x)
      suma += x
  print(suma)

mifuncion(5,4,3,2,1)


# ## Función con retorno
# La declaración de retorno de Python es una declaración especial que puede usar dentro de una función o método para enviar el resultado de la función a la persona que llama. Una declaración de retorno consta de la palabra clave `return` seguida de un valor de retorno opcional. El valor de retorno de una función de Python puede ser cualquier objeto de Python.

# In[ ]:


def miFuncionImprime(base,altura):
  print("Resultado: ",base*altura)

def miFuncionRetorna(base,altura):
  return base*altura

y = miFuncionImprime(5,8)
print("y: ",y)

p = miFuncionRetorna(5,8)
print("p: ",p+56)

#y = miFuncion(3,8)
#print(f"Resultado de multiplicar por 5",y+5)
#print(f"Resultado de multiplicar por 5",miFuncion(3))
#print(miFuncion(3)+3)
#print(miFuncion(5))


# •	Ejercicio [FuncionPalabraInvertida] -> Codifique el siguiente programa:
# - cree una función que recibe un texto como parámetro, ese texto debe invertirlo y devolverlo al caller para que lo imprima.
# - Invoque varias veces la función.

# In[ ]:


def invertir_palabra(palabra):
    inv = ""
    for i in range(len(palabra)-1, -1, -1):
        #print(i)
        inv = inv + palabra[i]
    return inv
    
palabra = "APRENDIENDO PYTHON"
print(invertir_palabra(palabra))
#palabra = "USO DE SUBPROGRAMAS"
#print(invertir_palabra(palabra))
#palabra = "MEDIANTE ESTE EJEMPLO"
#print(invertir_palabra(palabra))
palabra = "reconocer"
print(invertir_palabra(palabra))


# # Variables locales y globales
# - Las variables definidas dentro de un subprograma, tienen alcance solamente en el subprograma y cuando este termina, las variables desaparecen.  Estas variable son llamadas locales
# - Las variables que están definidas dentro del programa principal o llamante, se pueden usar dentro del subprograma solo si se definen como globales dentro del mismo, en ese caso los cambios que le hagamos a esa variable dentro de la función, también la afectarán fuera de ella.

# In[ ]:


x = "genial"

def miFuncion():
  x = "fantastico"
  print("Python es " + x)

miFuncion()  
print("Python es " + x)


# In[2]:


x = "genial"

def miFuncion():
  global x
  x = "fantástico"
  print("Python es " + x)

miFuncion()
print("Python es " + x)


# # Archivos con funciones
# - Poder usar las funciones que definamos deberíamos escribirlas al principio del programa principal o llamante, además tendríamos que repetirlas en cada programa que escribamos.
# 
# - Por fortuna Python nos permite invocar uno o varios archivos donde podemos tener escritas las funciones y así no tener que escribirlas en cada programa!

# In[ ]:


#Archivo tablas.py
def imprima_tablas(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(f"{i} * {j} = {i*j}")


# In[ ]:


#principal.py
import tablas
tablas.imprima_tablas(10, 10)


# In[ ]:


#otra_forma.py
import tablas as t
t.imprima_tablas(10, 10)


# # Ejercicios

# •	Ejercicio [FuncionImpresion] -> Codifique el siguiente programa:
# - Cree una función que recibe un cantidad desconocida de parámetros.
# - Dentro de esta función construya un ciclo que imprima los parámetros recibidos.
# - Por fuera de la función, invoque la función enviandole x cantidad de argumentos.

# In[ ]:


def funcionImpresion(*datos):
    for x in datos:
        print(x)
        
funcionImpresion("Hola", "beneficiarios", ":)")
funcionImpresion(1,2,3,4,5)


# •	Ejercicio [holaMensaje] -> Codifique el siguiente programa:
# - Cree una función en Python (llamada holaMensaje), que reciba un parámetro.
# - Esa función por dentro debe imprimir el texto “Hola” +  el parámetro recibido.
# - Ejemplo:
#     - Al invocar holaMensaje(“juan”), debe imprimir “Hola juan”.
#     - Al invocar holaMensaje(“iphone”), debe imprimir “Hola iphone”.
#     - Al invocar holaMensaje(“sara”), debe imprimir “Hola sara”.

# In[ ]:





# •	Ejercicio [funcionPar] -> Codifique el siguiente programa:
# - Crear una función: numero_par, que acepte un número entero positivo y devuelva si el número es par.

# •	Ejercicio [funcionDescomponer] -> Codifique el siguiente programa:
# - Crear una función: descomponer_cifras, que reciba un número entero de dos cifras y retorne sus unidades y sus decenas.

# •	Ejercicio [funcionHipotenusa] -> Codifique el siguiente programa:
# - Crear una función: hipotenusa, que acepte la longitud de dos lados de un triángulo rectángulo y regrese la hipotenusa. 

# •	Ejercicio [funcionMonos] -> Codifique el siguiente programa:
# - Tenemos dos monos, a y b, y los parametros a_smile y b_smile indican si cada uno de los monos está sonriendo. Tenemos un problema si los dos están sonriendo al mismo tiempo o ninguno de los dos está sonriendo. Retornar verdadero si tenemos un problema, falso si no. 
