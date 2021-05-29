#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# Suponga que le piden mostrar 100 veces el mensaje “Bienvenido a Python”.
# ¿Cómo lo solucionamos con lo que hemos visto hasta el momento?

# In[ ]:


print("Bienvenido a Python")
print("Bienvenido a Python")
print("Bienvenido a Python")
print("Bienvenido a Python")
print("Bienvenido a Python")
print("Bienvenido a Python")
#................

# ¿Qué les parece?


# # Ciclos
# 
# - Afortunadamente, Python provee unas estructuras llamadas “ciclos” (loop).
# - Los ciclos permiten controlar cuantas veces se realiza una operación, o una secuencia de operaciones.
# - Usando un ciclo, se le puede decir a la computadora que muestre un texto cien veces sin tener que codificar “la declaración de impresión” cien veces. Veamos un ejemplo:

# In[ ]:


for i in range(0,5):
    print("Bienvenido a Python")
print("Fin programa")


# ### Estructura ciclo
# Todo ciclo consta de 3 partes fundamentales:
# 
# - Inicialización variable de control
#     - Se inicializa una variable que servirá para controlar la ejecución del ciclo.
# - Prueba variable de control
#     - Se realiza una prueba sobre la variable de control para verificar si se puede o no seguir ejecutando el ciclo.
# - Cambio variable de control
#     - Se realiza un cambio sobre la variable de control.

# <img src="Figures/S2-EstructuraCiclo.png" width="800" height="1000">

# Python proporciona dos tipos de estructuras de bucles las cuales se detallarán a continuación: “while” y “for”.

# # 2. While
# Un ciclo while ejecuta instrucciones repetidamente, mientras una condición definida en el ciclo sea verdadera.
# Generalmente, la sintaxis para el ciclo while es la siguiente:

# In[ ]:


i = 1 #Inicialización variable control
while i<6: #Prueba variable control
    print(i)
    i=i+1 #Cambio variable control, lo mimos que i += 1
print("Sigo ejecutando instrucciones")


# Ojo -> su ciclo puede quedarse ejecutando infinitamente si:
# - Su condición no puede validarse como False en algún momento.
# - No modifica la variable de control

# In[ ]:


i = 1 
while i >= 0: #Infinito
    print(i)
    i=i+1 
    
i = 1 
while i < 8: 
    print(i) # Infinito 
    


# •	Ejercicio [CicloNumeros] 
# - Programe un ciclo que imprima los números del 6 al 14 (inclusivo)

# In[ ]:


i = 6 
while i <= 14: #Infinito
    print(i)
    i=i+1
else:
    print("Salio del ciclo")


# •	Ejercicio [CicloPares] 
# - Programe un ciclo que imprima los números pares del 2 al 20 (inclusivo)

# In[ ]:


i=2
while i<=20:
  if(i%2==0):
    print(i)
  i+=1 


# ## While con centinela
# - En los programas anteriores, conocemos exactamente cuantas veces se ejecutará cada ciclo while. A esto se le conoce como ciclo controlado por contador.
# 
# - Otra técnica común para controlar un ciclo es definir un valor especial que recogeremos del usuario. 
# 
# - Este valor de entrada especial, conocido como valor centinela, significará el final de la ejecución de un ciclo. 
# 
# - Un ciclo que utiliza un valor centinela para controlar su ejecución se denomina ciclo controlado por centinela.

# In[ ]:


num = int(input("Ingrese un num positivo, o 0 para salir")) #Inicialización variable control
while num !=0: #Prueba variable control
    print(num)
    num = int(input("Ingrese un num positivo, o 0 para salir")) #Cambio variable control, lo mimos que i += 1 


# In[ ]:


while True:
    num = int(input("Ingrese un num positivo, o 0 para salir"))
    if(num==0):
        break
        print("holaaaaaaaa")
    else:
        print(num)
print("Sigo por acá")
# “break”, es una palabra reservada de Python que sirve para salir de la ejecución del ciclo que la contiene


# •	Ejercicio [Acumulado]
# - Cree un ciclo while infinito
# - Pídale al usuario dentro del ciclo un número (int) (num1)
# - Si el usuario ingresa 0, detenga el ciclo (utilice un break).
# - Si el usuario ingresa cualquier otro número súmelo en un acumulador, y vaya mostrando el acumulado hasta el momento.

# In[ ]:


acumulado = 0
while True:
    num = int(input("num"))
    if(num == 0):
        break
    else:
        acumulado = acumulado + num # acumulado += num
        print("El acumulado es: ", acumulado)
print("El acumulado total es:", acumulado)


# # 3. Ciclo for
# - Un bucle for se utiliza para iterar sobre una secuencia (que es una lista, una tupla, un diccionario, un conjunto o una cadena).
# 
# - Con el ciclo for podemos ejecutar un conjunto de declaraciones, una vez para cada elemento de una lista, tupla, conjunto, etc.
# 
# - Su función es más como un iterador a diferencia de otros lenguajes de programación, por lo que:
# 
#     - Se debe declarar la variable de control, pero esta no se inicializa, ya que siempre tomará el primer valor de la secuencia.
#     - El cambio a la variable  de control lo hace el for, inicialmente tomará el primer valor de la secuencia y ejecuta las intrucciones, luego el segundo valor, y así sucesivamente
#     - La prueba en este caso la hace el for al verificar que los elemento de la secuencia recibida no se han terminado.

# In[ ]:


texto = "Hola luisa"
for x in texto: # X es la variable de control que itera por los valores de la variable texto
    print(x)

 


# ## For con la función range
# - Tener que definir manualmente arreglos con los valores a iterar se vuelve muy tedioso.
# 
# - Por lo tanto, Python provee una función que nos facilita la definición de esos valores. Esa función se llama range.
# 
# - La función range(n) devuelve una secuencia de números.
#     - Por defecto, comenzará desde el número 0.
#     - Por defecto, incrementará de a 1.
#     - Y terminará antes de llegar al número n enviado (es decir, hasta n-1).

# In[ ]:


for i in range(5):
    print(i)


# ### Variaciones de la función range
# - La función range también funciona si se le envían 2 o 3 parámetros. Veamos la documentación de la función range.
# 
# - range(inicio, parada, incremento).
#     - inicio (opcional): indica el número desde el cual inicia la secuencia.
#     - parada (requerido): indica el número en el cual termina la secuencia.
#     - incremento (opcional): indica como incrementa la secuencia.
# 
# - Si definimos por ejemplo range(1,7,2). Se crearía una secuencia con los números (1, 3, 5).

# In[ ]:


for i in range(10,0,-1):  #(0,11,3) (10,20,30) (10,0,-1)
    print(i) 


# •	Ejercicio [MultiplosDe5] -> Codifique el siguiente programa:
# - Pídale al usuario un número por pantalla.
# 
# - Cree un ciclo que imprima todos los múltiplos de 5, desde 5, hasta el número que ingreso el usuario.
# 
# - Si el usuario ingreso el número 16. El algoritmo debería imprimir los números 5, 10 y 15.

# In[ ]:


num = int(input("Ingrese num: "))
for i in range(5,num+1,5):
    print(i)
    
num = int(input("Ingrese un numero: "))
for i in range(0,num+1,5):  #(inicio,numero ingresa usuario, iteracion o aumento)
    print(i)


# ### Range con len
# También podemos crear una mezcla de range con len, para recorrer los valores de un arreglo, y que la variable de control almacene la información de la “posición” actual del arreglo que esta siendo recorrido. Veamos:

# In[ ]:


texto = "Hola mundo"
for i in range(len(texto)):
    print("Posición:",i,"Carácter",texto[i])


# •	Ejercicio [CaracteresInversos] -> Codifique el siguiente programa:
# - Pídale al usuario un texto por pantalla.
# - Cree un ciclo for con range que lea el texto de forma inversa, es decir de derecha a izquierda.
# - Imprima la posición del carácter y el carácter.
# 

# In[ ]:


texto = "Hola mundo"
for i in range(len(texto)-1,-1,-1):
    print("Posición:",i,"Carácter",texto[i])

texto = "Hola mundo adasd"
for i in range(len(texto)):
    print("Posición:",(len(texto)-1)-i,"Carácter",texto[(len(texto)-1)-i])


# ### Break
# La palabra break puede utilizarse dentro de bucles, para terminar inmediatamente el bucle.
# 

# In[ ]:


for x in "string":
    if x == "i":
        break
    print(x)
print("Fin programa")


# •	Ejercicio [EntradasConcierto] -> Codifique el siguiente programa que permitirá comprar boletas para un concierto:
# - Se tiene que el precio de la boleta es de 3 pesos.
# - Vamos a tener una variable acumulada con el total de entradas compradas por el usuario.
# - Solicite al usuario que ingrese el dinero que posee para comprar boletas.
# - Cree un ciclo en donde el usuario no podrá comprar más de 100 boletas y en donde para cada iteración debe:
#     - Imprimir un mensaje que diga: "Vamos a verificar si puedes comprar" 
#     - Valide si el dinero del usuario es suficiente para comprar UNA boleta.
#        - Si es así, aumente en una unidad la cantidad de las boletas compradas y reste el precio pagado a la cantidad de dinero del usuario.
#        - De lo contrario, salga del ciclo.
# - Imprima al final del programa, el total de boletas compradas y el dinero sobrante.

# In[ ]:


precio = 3
dinero = 10000
entradas = 0

while(entradas < 100):
    print("Vamos a verificar si puedes comprar")
    if(dinero >= 3):
        entradas+=1
        dinero = dinero - precio
    else:
        break
print("Dinero sobrante", dinero)
print("Entradas compradas", entradas)


# In[ ]:


precio=3
totalEntradas=0
dineroUsuario=int(input("Ingrese el dinero que posee para comprar las boletas: "))
print("Vamos a verificar si puedes comprar")

while (dineroUsuario>=precio) and (totalEntradas<100):
    totalEntradas =totalEntradas+1
    dineroUsuario=dineroUsuario-3
print("Boletas compradas: ", totalEntradas)
print("Dinero Sobrante: ", dineroUsuario)


# ### Continue
# - También se puede usar la palabra continue en un bucle. 
# - Cuando se ejecuta la palabra continue, esta hace que se finalice la iteración actual y el control del programa va al final del cuerpo del bucle.
# - En otras palabras, continue “salta” una iteración, mientras que la palabra “break” “sale” del bucle.

# In[ ]:


for x in "string":
    if x == "i":
        continue
    print(x)
print("Fin programa")


# •	Ejercicio [SumaContinue] -> Codifique el siguiente programa:
# 
# - Se tiene un rango de números desde el 0 hasta el 6.
# - El programa debe iterar sobre cada número y sumarlo con el anterior, pero debe omitir el número 4 y el 5 del rango.
# - Imprima el resultado al final del programa.

# In[ ]:


suma = 0
for x in range(7):
    if(x==4 or x==5):
        continue
    suma = suma + x
print(suma)


# In[ ]:


suma = 0
x = 0
while x < 6:
    x=x+1; # Ojo con la ubicación del cambio de la variable de control
    if(x==4 or x==5):
        continue
    suma = suma + x
print(suma)


# # 4. Ciclos Anidados
# - Tal como las estructuras de selección, las estructuras de iteración también se pueden anidar.
# - Incluso, una estructura de iteración se puede anidar dentro de una estructura de selección, y al revés. 
# - Cuando se anida una estructura de iteración dentro de otra estructura de iteración, se deben considerar ciertos aspectos.
# - Veamos el siguiente ejemplo.
# 

# 
# Nota: 
# - Cada iteración debe tener su propia variable de control. Si utiliza la misma variable de control para iteraciones anidadas, lo mas probable es que termine con bucles infinitos. 
# - Los ciclos anidados suelen usarse recorrer matrices donde un ciclo recorre cada fila y otro cada columna o viceversa.
# - el ciclo externo no avanza hasta que el ciclo interno termine y una vez el ciclo externo avanza un paso vuelve a esperar al interno y así sucesivamente hasta que el externo termina.

# <img src="Figures/S2-CicloAnidado.png" width="500" height="800">

# In[ ]:


i = 1                           #Inicialización variable control CICLO1
while i<=3:                     #Prueba variable control CICLO1
    j = 1                       #Inicialización variable control CICLO2
    while j <=2:                #Prueba variable control CICLO2
        print("i=",i,"j=",j)
        j = j+1                 #Cambio variable control CICLO2
    i=i+1                       #Cambio variable control CICLO1
print("Fin programa")


# •	Ejercicio [CicloAnidadoFor]
# - Codifique un ciclo anidado con for que imprima la misma información del anterior ciclo

# In[ ]:


for i in range(1,4):
    for j in range(1,3):
        print("i=",i,"j=",j)
        


# •	Ejercicio [MultiplicationTable] -> Codifique un programa que genere el siguiente resultado:
# 
# <img src="Figures/S2-MultiplicationTable.png" width="500" height="800">

# In[ ]:


print("",1,2,3,4,5,6,7,8,9,sep = "\t")
print("---------------------------------------------------------------------------")
for i in range(1,10):
  print(i,"|",end = "\t")
  for j in range(1,10):
    print(i * j, end = "\t")
  print(sep = "\t")


# # Ejercicios

# •	Ejercicio [Divisible3] -> Codifique el siguiente programa:
# - Un programa que imprima los números divisibles por 3. Iniciando desde el 3 hasta el 100.

# •	Ejercicio [Puntajes] -> Codifique el siguiente programa:
# - Pídale al usuario por pantalla un puntaje (int)
# - Vaya guardando la suma de los puntajes, la cantidad de puntajes ingresados
# - Vaya guardando el puntaje más alto
# - Si el puntaje es -1 finalice el bucle
# - Finalmente, imprima el promedio de puntajes, y el puntaje mas alto.

# In[14]:


#pedir un puntaje entero
suma=0
acum=0
max=0
while (acum>=0):
  puntaje=int(input("Ingrese un puntaje: "))
  if (puntaje==-1):
    break
  else:
    suma=suma+puntaje
    acum+=1
    if (puntaje>max):
      max=puntaje
print("El promedio de puntajes es ", suma/acum," Y el puntaje más alto es ",max)

