#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# Analicemos el siguiente código:

# In[1]:


radio = float(input("Ingrese el radio: "))
print(radio)
area = 3.14 * radio**2
print(area)

# ¿Qué pasa si agregó un número negativo? ¿Es correcto el resultado?


# - Hasta ahora hemos visto que los programas se ejecutan siguiendo un orden que definimos al codificar cada línea. En nuestro caso, el orden de ejecución arranca desde la primera línea del “IDE” en el que estamos trabajando, y continua hacia abajo.
# - Independiente de los datos que ingresemos (o que le pidamos por pantalla al usuario), el orden (flujo de control) es el mismo. 
# - Esto quiere decir que no tenemos una respuesta diferente o un orden diferente cuando se ingresan diferentes entradas o valores.
# - Pero que tal si podemos definir un orden diferente, dependiendo de las entradas de los usuarios, o de los valores de ciertas variables.

# ## Estructuras de selección o condición
# En este caso podríamos por ejemplo: (i) ejecutar el programa en un orden normal si el valor de un radio es mayor que cero, o (ii) ejecutar otro camino si el valor del radio es menor igual a cero.
# 
# Para poder brindarle a nuestra código esta habilidad. Necesitamos utilizar “estructuras de selección”.
# 
# <img src="Figures/S2-Secuencia.png" width="200" height="400">

# ### 1.1 Estructura if-then
# Es la más básica de la estructuras de selección.
# 
# Su funcionamiento es el siguiente:
# Si una condición particular es verdadera, entonces la porción “then” es ejecutada; de lo contrario, la porción “then” no es ejecutada.
# 
# Ejemplo:
# Similar a lo lenguajes naturales donde se puede decir: ¿Es un día caluroso? Entonces, compro un helado.
# 
# <img src="Figures/S2-EstructuraIfThen.png" width="400" height="600">

# In[8]:


temp = float(input("Ingrese la temperatura"))
if temp > 30:
    print("Comprar helado")
    print("Comprar limonada")
print("Fin programa")


# •	Ejercicio [CondicionalBasico]
# 
# Modifique el programa anterior: Ahora, cuando la temperatura sea mayor a 30, se mostrará el mensaje “Comprar helado” y otro mensaje que diga “Comprar limonada”.

# •	Ejercicio [CondicionalBasico2]
# 
# Cree un programa donde solicite un número al usuario, si el número es par, se mostrará el mensaje "El número ingresado es par", al final del programa siempre debe imprimir "Sigo ejecutando instrucciones"

# In[ ]:


numero = int(input("Ingrese la temperatura"))
if numero%2 == 0:
    print("El número es par")
print("Sigo ejecutando instrucciones")


# ### 1.2 Estructura if-then-else
# - La estructura If-then es muy necesaria para lograr cambiar el control de flujo de un programa (ofrecer varios caminos). Sin embargo, que pasa si se requiere que el programa deba hacer el algo en ambas alternativas: caso verdadero y caso falso. 
# - La sección “else” (en caso contrario) es una sección opcional que se puede añadir a la estructura “if-then”. Las instrucciones de esta sección se ejecutarán SOLO SI todas las condiciones anteriores se evaluaron como falsas.
# 
# Ejemplo: si el total de créditos aprobados es mayor o igual a 120 la persona se gradúa; en caso contrario no se gradúa.
# 
# <img src="Figures/S2-EstructuraIfThenElse.png" width="400" height="600">

# In[10]:


creditos = int(input("Ingrese los créditos aprobados"))
if(creditos >= 120):
    print("Se gradúa")
else:
    print("No se gradua")
print("Fin programa")


# In[12]:


texto2= "sdasd"
if texto2:
    print("Verdadera")
else:
    print("Falso")
    
#Forma simplificada    
print("Verdadera") if texto2 else print("Falso") #Operador ternario


# •	Ejercicio [Area-cuadrado] -> Codifique el siguiente programa:
# - El programa pedirá al usuario un lado de un cuadrado (int)
# - Si el lado es mayor a 0:
#     - Calculará el área 
#     - Imprimirá “El área del cuadrado es: ” + area.
# - En caso contrario imprimirá “¿De qué me hablas viejo?”
# - En ambos casos al final, imprimirá “Fin programa”
# 

# In[14]:


lado = int(input("¿Cuál es la medida de uno de los lados del cuadrado?"))
if lado > 0:
  a = lado**2
  print("El área del cuadrado es:",a)
else:
  print("¿De qué me hablas viejo?")
print("Fin programa")


# ### 1.3 Estructura if-then-else if-..... ó Elif
# - La estructura If-then-else if-… nos permite ofrecer múltiples caminos dependiendo de múltiples comprobaciones. 
# - El else if sirve para añadir una nueva condición en caso de que la condición anterior no se cumpla (sea falsa).
# - Una instrucción if puede incluir cualquier número de bloques else if. “else if” significa (de lo contrario, si …). 
# - Como máximo, se ejecuta un solo else if, y ese else if se ejecutará solo si todas las condiciones anteriores se evaluaron como falsas.
# 
# Ejemplo: si la temperatura es mayor a 27 compramos helado; de lo contrario, si la temperatura es mayor a 24 compramos gaseosa; en caso contrario, compramos leche.

# <img src="Figures/S2-Elif.png" width="400" height="600">

# In[ ]:


temp = float(input("Ingrese la temperatura"))
if(temp > 27):
    print("Comprar helado")
print("Fin programa")


# In[19]:


temp = float(input("Ingrese la temperatura"))
if(temp > 27):
    print("Comprar helado")
elif(temp > 24):
    print("Comprar gaseosa")
else:
    print("Comprar leche")   
    


# ¿Cuál seria la salida por pantalla si ingresamos: (i) 2  (ii) 4 y (iii) 1?

# In[22]:


nota = int(input("Ingrese la nota"))
if(nota > 4):
    print(":)")
elif(nota < 3):
    print(":(")
elif(nota == 2):
    print(":|")    
else:
    print(":O")   
print("Fin programa")


# •	Ejercicio [Elif] -> Codifique el siguiente programa utilizando elif:
# 
# <img src="Figures/S2-ElifEjercicio.png" width="500" height="800">

# In[ ]:





# ### 1.4 If anidados
# También es posible contener ifs, dentro de otros ifs. Veamos el siguiente ejemplo.

# <img src="Figures/AnidadoTempDinero.png" width="700" height="1000">

# In[ ]:


temp = float(input("Ingrese la temperatura"))
dinero = 6
if(temp > 27):
    if(dinero > 5):
        print("Comprar helado")
print("Fin programa")

#Con cuál operador lógico podría simplificar esto?


# <img src="Figures/NoAnidadoTempDinero.png" width="500" height="800">

# In[ ]:


temp = float(input("Ingrese la temperatura"))
if((temp > 27) and (dinero > 5)):
        print("Comprar helado")
print("Fin programa")


# # Ejercicios

# •	Ejercicio [EdadPermitida] -> Codifique el siguiente programa:
# - El programa pedirá al usuario la edad (int)
# - El programa validará que la edad sea mayor o igual a 18 
# - Si la edad es mayor o igual a 18 el programa imprimirá “bienvenido a la fiesta!

# •	Ejercicio [ComparandoAños] -> Codifique el siguiente programa:
# - Pídale al usuario el año en el que estamos (int – fecha1).
# - Pídale al usuario otro año cualquiera (puede ser futuro, pasado o el mismo año) (int – fecha2).
# - Si la fecha1 es mayor que la fecha2 imprima:
#     - Desde el año {fecha2} han pasado {fecha2-fecha1} años.
# - Si la fecha1 es menor que la fecha2 imprima:
#     - Para llegar al año {fecha2} faltan {fecha2-fecha1} años.
# - De lo contrario imprima:
#     - Son el mismo año.

# •	Ejercicio [if.then-else] -> Codifique el siguiente programa:
# - El programa pedirá al usuario el genero (string)
# - Si el genero es “masculino” imprimirá “Bienvenido al grupo”
# - En caso contrario imprimirá “Bienvenida al grupo”
# - En ambos casos al final, imprimirá “Bienvenidos a la U”

# •	Ejercicio [Loteria] -> Codifique el siguiente programa:
# - Cree un programa, que tenga dos dígitos guardados,  decenas y unidades, por ejemplo 54,  int decenas = 5 y int unidades = 4.
# - Por medio de la consola solicite al usuario que ingrese el número de la lotería (dos dígitos).
# - Si los números coinciden en el orden exacto imprima “Coincidencia exacta gano 10.000”.
# - Si los números coinciden pero están inversos, imprima “Coinciden los dígitos, pero no en el orden exacto, gano 3.000”.
# - Si uno de los dígitos coincide sin importar el orden, imprima “Coincidencia de un dígito, gano 1.000”
# - Si ninguno coincide, imprima “Lo siento, no hay coincidencias”

# In[33]:


loteria = 54
loteriaD = loteria//10
loteriaU = loteria%10

usuario = 86
usuarioD = usuario//10
usuarioU = usuario%10

if(loteria == usuario):
    print("Ganó 10000")
elif((loteriaD == usuarioU) and (usuarioD == loteriaU)):
    print("Ganó 3000")
elif((loteriaD == usuarioD or loteriaD == usuarioU) or (loteriaU == usuarioU or loteriaU== usuarioD)):
    print("Ganó 1000")
else:
    print("Ninguna coincidencia, lo siento")

