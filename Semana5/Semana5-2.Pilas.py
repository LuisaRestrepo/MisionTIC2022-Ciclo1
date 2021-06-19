#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# - Una pila (stack en inglés) es una lista ordenada o estructura de datos que permite almacenar y recuperar datos.
# - La pila presenta un modo de acceso a sus elementos de tipo LIFO (del inglés Last In, First Out, «último en entrar, primero en salir»).
#     -  __Apilar__: consiste en insertar un registro al principio de una lista ligada.
#     -  __Desapilar__: consiste en eliminar el primer nodo de la lista y retornar el dato que se hallaba en ese nodo
# 
# <center><img src="Figures/S5-Apilando.png" width="1000" height="1100"></center>

# # Utilidades de las Pilas
# - Un ejemplo clásico de aplicación de pilas en computadores  se presenta en el proceso de llamadas a subprogramas y  sus retornos.
# - Cada vez que se llama a un subprograma (subrutina o función) es necesario guardar el estado del programa que realiza la llamada: o Dirección del programa a la que debe volver cuando termine, o las variables del programa, junto con sus valores antes de la llamada.
# - Tratamiento de expresiones aritméticas
# 

# In[ ]:


def funcion1():
    print("Ingreso por el método 1")
    x = 5 + funcion2()
    return x
    
def funcion2():
    print("Ingreso por el método 2")
    x = 3 + funcion3()
    return x

def funcion3():
    print("Ingreso por el método 3")
    x = 7
    return x
    
x = funcion1()
print(x)


# # Recursión
# - La recursión es una técnica que conduce a soluciones elegantes, a problemas que son difíciles de programar usando bucles simples.
# - Para utilizar recursión en un programa, se deben codificar métodos recursivos, es decir, codificar métodos que se invoquen a sí mismos.
# - Muchas funciones matemáticas se definen mediante recursividad.
# 
# El factorial de un número n puede definirse recursivamente de la siguiente manera:
# 
# <center>
# $0! = 1;$
# <center>
# $5! = 5*4*3*2*1$
# <center>
# $n! = n × (n − 1)!; n > 0$
# 

# In[ ]:


def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)
    
factorial(5)


# In[ ]:


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
print(fibonacci(8))


# In[ ]:


def fibonacci2(n):
    previo1 = 1
    previo2 = 1
    for i in range(2,n):
        temp = previo1
        previo1 = previo1+previo2
        previo2 = temp
    return previo1

fibonacci2(5000)


# # 1. Pilas con Listas

# In[ ]:


stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

print("\nElementos desencolados de la cola")
i = stack.pop()
print(i)
print("\nDespués de eliminar los elementos")
print(stack)


# # 2. Clase Pila
# ## Métodos de la clase Pila
# - __init__: inicializa una pila nueva, vacía.
# - __apilar__: agrega un nuevo elemento a la pila.
# - __desapilar__: elimina el tope de la pila y lo devuelve. El elemento que se devuelve es siempre el último que se agreg6.
# - __es_vacia__: devuelve True o False según si la pila está vacía o no.
# - __muestraPila__: imprime lo que tiene la pila

# In[ ]:


class Pila:
    def __init__(self):
        self.arreglo=[]
    def apilar(self, x):
        self.arreglo.append(x)
    def desapilar(self):
        try:
            return self.arreglo.pop()
        except IndexError:
            print("La pila está vacía")
    def es_vacia(self):
        return self.arreglo == []
    def muestraPila(self):
        for i in self.arreglo:   
            print(i, end=", ")   
        print()


# In[ ]:


p = Pila()
print("Es vacia?",p.es_vacia())
p.apilar(1)
print("Es vacia?",p.es_vacia())
p.muestraPila()
p.apilar(6)
p.apilar("+")
p.apilar(7)
p.muestraPila()
p.desapilar()
p.muestraPila()
p.desapilar()
p.desapilar()
p.desapilar()
p.desapilar()


# •	Ejercicio [pilas] -> Codifique el siguiente programa:
# - Construya un ciclo infinito, donde:
#     - Dentro del ciclo, solicite al usuario que ingrese una opción:
#         - 1 - para apilar, aca debe solicitar el valor a apilar e ingresarlo en la pila
#         - 2 - para desapilar e imprimir el valor desapilado
#         - 3 - para imprimir el contenido de la pila
#         - 0 - para salir
#    
# 

# In[ ]:


pila=[]
while True:
    x=int(input("ingrese una opcion: "))   
    if (x == 1):
        valor=int(input("ingrese valor para apilar: "))
        pila.append(valor)
    elif (x == 2):
        try:
            pila.pop()
        except IndexError:
            print("La pila está vacía")
    elif (x == 3):
        print(pila)
    else:
        print("saliendo del sistema")
        break


# # 3. Clase Pila con Vector
# ## Métodos de la clase Pila
# - __init__: crea un objeto vector con el tamaño ingresado + 1.
# - __apilar__: agrega un nuevo elemento a la pila.
# - __desapilar__: elimina el tope de la pila y lo devuelve. El elemento que se devuelve es siempre el último que se agreg6.
# - __muestraPila__: imprime lo que tiene la pila

# In[ ]:


class pilaVector(vector):
 def __init__(self, n):
     vector.__init__(self, n)
 
 def apilar(self, d):
    self.agregarDato(d)
    
 def muestraPila(self):
     self.imprimeVector()
     
 def desapilar(self):
     if self.V[0] == 0:
         print("Pila vacía")
         return None
     d = self.V[self.V[0]]
     self.V[0] = self.V[0] - 1
     return d

st = pilaVector(10)
st.apilar("a")
st.apilar("b")
st.apilar(316)
st.muestraPila()
d = st.desapilar()
print(d)
st.muestraPila()


# # 4. Pila usando la clase LSL
# - __init__: inicializa un objeto LSL.
# - __apilar__: agrega un nuevo elemento a la pila.
# - __desapilar__: elimina el tope de la pila y lo devuelve. El elemento que se devuelve es siempre el último que se agreg6.
# - __muestraPila__: imprime lo que tiene la pila

# In[ ]:


class pila(LSL):
     def __init__(self):
         LSL.__init__(self)
     def apilar(self, d):
         self.insertar(d)
     def muestraPila(self):
         self.recorrerLista()
     def desapilar(self):
         p = self.primerNodo()
         d = p.retornarDato()
         self.borrar(p)
         return d
    
a = pila()
a.apilar("a")
a.apilar("e")
a.apilar("i")
a.apilar("o")
a.recorrerLista()
b = a.esVacia()
print("\n Está vacía?", b)
d = a.desapilar()
print("\ndato desapilado", d)
a.recorrerLista()


# # Ejercicios

# In[ ]:


class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None
    
    def primerNodo (self):
        return self.primero
    
    def ultimoNodo (self):
        return self.ultimo
    
    def esVacia (self):
        return self.primero == None
    
    def finDeRecorrido (self, p):
        return p == None
    
    def recorrerLista (self):
        p = self.primerNodo()
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end = ", ")
            p = p.retornarLiga()
            
    def agregarDato (self, d):
        x = nodoSimple(d)
        p = self.primerNodo()
        if p == None:
            self.primero = x
            self.ultimo = x
        else:
            self.ultimo.liga = x
            self.ultimo = x
            
    def buscarDondeInsertar (self, d):
        p = self.primerNodo()
        y = None
        while not self.finDeRecorrido(p) and p.retornarDato() < d:
            y = p
            p = p.retornarLiga()
        return y
    
    def insertar (self, d, y=None): #cambio
        x = nodoSimple(d) #cambio
        self.conectar(x, y)
        
    def conectar (self, x, y):
        if y == None:
            if self.primero == None:
                self.ultimo = x
            else:
                x.asignarLiga(self.primero)
            self.primero = x
            return
        x.asignarLiga(y.retornarLiga())
        y.asignarLiga(x)
        if y == self.ultimo:
            self.ultimo = x
            
    def longitud (self):
       p = self.primerNodo()
       n = 0
       while not self.finDeRecorrido(p):
           n = n + 1
           p = p.retornarLiga()
       return n
    
    def buscarDato (self, d, y):
       x = self.primerNodo()
       while not self.finDeRecorrido(x) and x.retornarDato() != d:
           y.asignarDato(x)
           x = x.retornarLiga()
       return x
    
    def buscarDato2 (self, d):
       y = nodoSimple()
       x = self.primerNodo()
       while not self.finDeRecorrido(x) and x.retornarDato() != d:
           y.asignarDato(x)
           x = x.retornarLiga()
       return x, y
   
    
    def borrar (self, x, y = None):
       if x == None:
           print("Dato no está en la lista")
           return
       if y == None:
           if x != self.primero:
               print("Falta el anterior del dato a borrar")
               return
       else:
          y = y.retornarDato()
          
       self.desconectar(x,y) #cambié identación
          
    def desconectar (self, x, y):
        if y == None:
            self.primero = x.retornarLiga()
            if self.esVacia():
                self.ultimo = None
        else:
            y.asignarLiga(x.retornarLiga())
            if x == self.ultimo:
                self.ultimo = y
class nodoSimple:
 def __init__(self, d = None):
     self.dato = d
     self.liga = None
 def asignarDato(self, d):
     self.dato = d
 def asignarLiga(self, x):
     self.liga = x
 def retornarDato(self):
     return self.dato
 def retornarLiga(self):
     return self.liga
    
class vector:

    def __init__(self, n):
         self.n = n
         self.V = [0] * (n + 1)
     
    def construyeVector(self, m, r): 
         self.V[0] = m   
         for i in range(1, m + 1):  
                 self.V[i] = random.randint(1, r)
        
    def imprimeVector(self, mensaje = "vector sin nombre: \t"): 
        print("\n", mensaje, end=" ")  
        for i in range(1, self.V[0] + 1):   
                print(self.V[i], end=", ")   
        print()
       
    def agregarDato(self, d):   
        if self.esLleno():    
             return    
        self.V[0] = self.V[0] + 1    
        self.V[self.V[0]] = d
    
    def asignaDato(self, d, i):    
        self.V[i] = d
    
    def retornaDato(self, i):    
        return self.V[i] 
       
    def intercambiar(self, a, b):    
        aux = self.V[a]    
        self.V[a] = self.V[b]
        self.V[b] = aux
       
    def seleccion(self):    
         for i in range(1, self.V[0]):    
             k = i    
             for j in range(i + 1, self.V[0] + 1):    
                   if self.V[j] < self.V[k]:    
                           k = j    
             self.intercambiar(k, i) 
       
    def mayor(self):    
        mayor = 1    
        for i in range(1, self.V[0] + 1):    
                if self.V[i] > self.V[mayor]:    
                     mayor = i    
        return mayor    
    
    def menor(self):    
         menor = 1    
         for i in range(1, self.V[0] + 1):    
               if self.V[i] < self.V[menor]:    
                     menor = i    
         return menor
    
    def buscarDato(self, d):    
        i = 1    
        while i <= self.V[0] and self.V[i] != d:    
                 i = i + 1    
        if i <= self.V[0]:    
                return i    
        return -1
       
    def borrarDatoEnPosicion(self, i):    
         if i <= 0 or i > self.V[0]:    
               print("\nParámetro i inválido")    
               return    
         for j in range(i, self.V[0]):    
               self.V[j] = self.V[j + 1]    
         self.V[0] = self.V[0] -1
      
    def borrarDato(self, d):   
         i = self.buscarDato(d)   
         if i != -1:   
               self.borrarDatoEnPosicion(i)  
    
    def posicionesUsadas(self):   
          return self.V[0]      
    
    def esVacio(self):   
          return self.V[0] == 0
          
    def esLleno(self):    
         return self.V[0] == self.n   
       
    def tamagno(self):    
          return self.n
        
    def asignaNumeroElementos(self, m): 
         self.V[0] = m
         
    def buscaDondeInsertar(self, d):   
         i = 1   
         while i <= self.V[0] and self.V[i] < d:   
                 i = i + 1   
         return i  
       
    def insertar(self, d, i = 0):  
         if self.esLleno():  
                print("\nVector lleno, no se puede insertar")  
                return  
         if i == 0:     
               i = self.buscaDondeInsertar(d)   
         for j in range(self.V[0], i -1, -1):   
               self.V[j + 1] = self.V[j]    
         self.V[i] = d   
         self.V[0] = self.V[0] + 1       
    
    def sumaDatos(self):    
         s = 0  
         for i in range(1, self.V[0] + 1):  
                 s = s + self.V[i]   
         return s

