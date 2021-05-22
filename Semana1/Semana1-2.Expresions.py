#!/usr/bin/env python
# coding: utf-8

# # 1. Expresiones

# In[ ]:


a = 3.14 #Constante
b = 675 #Constante
h = b #Variable  
c = -.385E+57 #Expresión aritmética
d = a + b * c #Expresión aritmética
e = 5 > 2 #Expresión lógica
f = "Hola mundo" #Mensaje
g = True #Valor lógico


# ## 1.1 Expresiones Aritméticas
# Las expresiones aritméticas implican el uso de operadores (suma , resta, ...) y operandos (variables).
# 
# Prioridades (Orden en el cual se ejecutan operaciones consecutivas con diferentes operadores)
# - Primero se ejecutan las operaciones de potenciación
# - Luego las operaciones de multiplicación, división y módulo
# - Por último, las operaciones de suma y resta
# 
# Asociatividades (Orden en el cual se ejecutan operaciones consecutivas con operadores de la misma prioridad)
# - La potenciación es asociativa por la derecha
# - Las demás operaciones son asociativas por la izquierda

# Operadores usados en Python:
# 
# |Operador||Objetivo|
# | --- || --- |
# |+||para la suma|
# |-||para la resta|
# |*||para la multiplicación|
# |/||para la división (cociente real)|
# |//||para la división (cociente entero)|
# |%||para el módulo (residuo de división entera)|
# |**||para la potenciación|

# In[ ]:


a = 5
b = 3
c = 8
d = 4
e = 2
print(c/b)
print(c//b)
print(c%b)


# In[ ]:


a = 5
b = 3
c = 8
d = 4
e = 2
print(a + b * c) #se evalúa: 5 + 24 = 29
print((a + b) * c) #se evalúa: 8 * 8 = 64
print(a / e * c) #se evalúa: 2.5 * 8 = 20.0
print(a / (e * c)) #se evalúa: 5 / 16 = 0.3125
print(a // e * c) #se evalúa: 2 * 8 = 16
print(a // (e * c)) #se evalúa: 5 / 16 = 0
print(c / d / e) #se evalúa: 2 / 2 = 1
print(c / (d / e)) #se evalúa: 8 / 2 = 4
print(c / d * e) #se evalúa: 2 * 2 = 4
print(c / (d * e)) #se evalúa: 8 / 8 = 1
print(5 + c**1 * 5 + 3**2 ) #se evalúa   5 + (8*5) + 9 = 54


# Ejercicio [Expresion2]
# - Dada la expresión algebraica, escribala en lenguaje de programación
# 
# $ \frac{a}{b*c} $

# In[ ]:


print(6/(8*6)


# Ejercicio [Expresion3]
# - Dada la expresión algebraica, escribala en lenguaje de programación
# 
# $ a - \frac{b}{c}\, + \frac{b - \frac{c}{d}}{e} $
# 

# In[ ]:


a = 5
b = 3
c = 8
d = 4
e = 2
print(a - b /c + (b - c/d) / e)
print(a - (b/c)+  b-(c/d)/e) #ERROR


# Ejercicio [Expresion4]
# - Dada la expresión algebraica, escribala en lenguaje de programación
# 
# $ \frac{(a + b) * c}{(d-e)^b} $

# In[ ]:


a = 5
b = 3
c = 10
d = 4
e = 2
print((a+b)*c / (d-e)**b)
print((a+(b*c)) / (d-e)**b)


# Ejercicio [Expresion4]
# - Dada la expresión algebraica, escribala en lenguaje de programación
# 
# $ \frac{a - \frac{b+c}{d-e} + e - f^{2.3}}{4.5+d} $

# In[ ]:


a = 10
b = 3
c = 2
d = 4
e = 2
f = 6
print((a - (b+c)/(d-e) + e - f**2.3)/(4.5+d))
print(a // b // c)
print(a // (b * c))


# ## 1.2 Expresiones relacionales y lógicas
# Expresiones en donde se realiza una comparación. El valor a retornar será verdadero o falso.

# #### Operadores de comparación (o relacionales) usados en los lenguajes de programación:
# En general los lenguajes de programaciónproporcionan seis operadores de comparación (también conocidos como operadores de relación). Veamos la siguiente tabla y encontremos el resultado suponiendo que el valor de la variable “radio” es igual a 5. 
# 
# |Operador||Nombre|| Ejemplo  |
# | --- || --- || --- |
# |>||mayor que|| radio > 0  |
# |>=||mayor o igual que|| radio >= 0 |
# |<||menor que|| radio < 0 |
# |<=||menor o igual que|| radio <= 0  |
# |==||igual|| radio == 0 |
# |!=||diferente||  radio != 0 |
# 
# 

# In[ ]:


radio = 5
print(radio > 0)
print(radio >= 0)
print(radio < 0)
print(radio <= 0)
print(radio == 0)
print( radio != 0)


# Ejercicio [ComparacionVariables] ->
# 
# Analize las siguientes comparaciones, luego codifiquelas.
# 
# x = 9, y = 5, z = 10, h = "Hola", i = "Holaaa"
# 
# x == y 
# 
# x > y 
# 
# x == z 
# 
# z < x 
# 
# x != x 
# 
# x >= y 
# 
# h == "Hola"
# 
# h <= i

# In[ ]:





# #### Operadores lógicos usados en los lenguajes de programación:
# Los operadores lógicos son usados para operaciones de álgebra Booleana, es decir, para describir relaciones lógicas, expresadas como verdadero (True) o falso (False).
# 
# 
# |Operador||Nombre|
# | --- || --- |
# |&&||and|
# | &#124; &#124; || or |
# |!||not|
# 

# Tablas de verdad
# 
# |p1||p2|| p1 && p2  |
# | --- || --- || --- |
# |F||F|| F  |
# |F||V|| F|
# |V||F|| F|
# |V||V|| V |
# 
# |p1||p2|| p1  &#124; &#124; p2  |
# | --- || --- || --- |
# |F||F|| F  |
# |F||V|| V|
# |V||F|| V|
# |V||V|| V |
# 
# |p||!p|
# | --- || --- |
# |F||V|
# |V||F|
# 

# In[ ]:


#Analize las siguientes comparaciones:
a = 16; b = True; c = 4; d = 8; e = 5
print(a > c and e <=d)
print(b or (d - e) > a / c)
print(not b)
print(not b and c < d or a/d <= e)


# In[ ]:




