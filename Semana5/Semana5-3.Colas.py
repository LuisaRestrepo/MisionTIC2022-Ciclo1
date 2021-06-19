#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# - Una cola (queue en inglés) es una lista ordenada o estructura de datos que permite almacenar y recuperar datos.
# - La cola presenta un modo de acceso a sus elementos de tipo FIFO (del inglés First In First Out, «Primero en entrar, primero en salir»).
#     -  __Encolar__: agrega un nuevo elemento al final de la cola.
#     -  __Desencolar__: elimina el primero de la cola y lo devuelve.
# 
# <center><img src="Figures/S5-Encolando.png" width="1000" height="1100"></center>

# # Utilidades de las Colas
# - Es especialmente útil en la programación en hilo cuando la información debe intercambiarse de forma segura entre varios subprocesos.
# - Atender solicitudes en un solo recurso compartido, como una impresora, programación de tareas de CPU, etc.
# - En el escenario de la vida real, los sistemas telefónicos del centro de llamadas utilizan Colas para mantener a las personas que las llaman en un orden, hasta que un representante de servicio está libre.
# - Manejo de interrupciones en sistemas en tiempo real. Las interrupciones se manejan en el mismo orden en que llegan, es decir, primero en llegar, primero en ser atendido.
# 

# In[ ]:


from multiprocessing import Process

def funcion1():
    print("Ingresó por la función 1")
    x = 5 + principal()
    return x
    
def funcion2():
    print("Ingresó por la función 2")
    x = 3 + principal()
    return x

def principal():
    print("Ingresó por el principal")
    x = 7
    return x

p = Process(target=funcion1())
p.start()
p2 = Process(target=funcion2())
p2.start()

p.join()
p2.join()


# # 1. Colas con listas

# In[ ]:


queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
print("\nElementos desencolados de la cola")
print(queue.pop(0))
print("\nDespués de eliminar los elementos")
print(queue)


# ## Métodos de la clase Cola
# - __init__: Crea una cola vacía.
# - __encolar__: Agrega el elemento x como último de la cola.
# - __desencolar__: Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError.
# - __es_vacia__: devuelve True o False según si la cola está vacía o no.
# - __muestraCola__: imprime lo que tiene la cola.

# In[8]:


class Cola:
    def __init__(self):
        self.items=[]
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    def es_vacia(self):
        return self.items == []
    def muestraCola(self):
        print(self.items)
        
q = Cola()
print("Está vacía? ",q.es_vacia())
q.encolar(1)
q.encolar(2)
q.encolar(3)
q.muestraCola()
print("Está vacía? ",q.es_vacia())
q.desencolar()
q.muestraCola()


# •	Ejercicio [colas] -> Codifique el siguiente programa:
# - Construya un ciclo infinito, donde:
#     - Dentro del ciclo, solicite al usuario que ingrese una opción:
#         - 1 - para encolar, acaba debe solicitar el valor a encolar e ingresarlo en la cola
#         - 2 - para desencolar e imprimir el valor desencolado
#         - 3 - para imprimir el contenido de la cola
#         - 0 - para salir
#    
# 

# In[ ]:


queue=[]
while True:
    x=int(input("ingrese una opcion: "))   
    if (x == 1):
        valor=int(input("ingrese valor a encolar: "))
        queue.append(valor)
    elif (x == 2):
        try:
            queue.pop(0)
        except IndexError:
            print("La cola está vacía")
    elif (x == 3):
        print(queue)
    else:
        print("saliendo del sistema")
        break


# # 2. Colas con la clase vector
# ### Métodos de la clase Cola
# - __init__: Crea un objeto vector.
# - __encolar__: Agrega el elemento x como último de la cola.
# - __desencolar__: Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError.
# - __esVacia__: devuelve True o False según si la cola está vacía o no.
# - __esLlena__: devuelve True o False si la cola está llena o no.
# - __siguiente__: deveulve el elemento próximo a desencolar.

# In[ ]:


class colaVector(vector):
    def __init__(self, n):
        vector.__init__(self, n)
        self.primero = 0
        self.ultimo = 0
    def esLlena (self):
        return self.primero == self.ultimo
    def esVacia (self):
        return self.primero == self.ultimo
    def encolar (self, d):
        self.ultimo = (self.ultimo + 1) % self.n
        if self.esLlena():
            print("cola llena, no se puede encolar\n")
            self.ultimo = (self.ultimo - 1 + self.n) % self.n
            return
        self.V[self.ultimo] = d
    def desencolar (self):
        if self.esVacia():
            print("cola vacía, no se puede desencolar\n")
            return None
        self.primero = (self.primero + 1) % self.n
        return self.V[self.primero]
    def siguiente (self):
        if self.esVacia():
            print("cola vacía, no hay siguiente\n")
            return None
        aux = (self.primero + 1) % self.n
        return self.V[aux]
    
qu = colaVector(10)
print("Está vacía? ",qu.esVacia())
print("Está llena? ",qu.esLlena())
qu.encolar("a")
qu.encolar("b")
qu.encolar(316)
print("Elemento próximo a desencolar", qu.siguiente())
d = qu.desencolar()
print("\nDato desencolado:", d)


# # 3. Colas con la clase LSL
# ### Métodos de la clase Cola
# - __init__: Crea un objeto lista ligada.
# - __encolar__: Agrega el elemento x como último de la cola.
# - __desencolar__: Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError.
# - __siguiente__: deveulve el elemento próximo a desencolar.

# In[ ]:


class colaLSL(LSL):
 def __init__(self):
     LSL.__init__(self)
 
 def encolar(self, d):
     self.agregarDato(d)
 
 def desencolar(self):
    if self.esVacia():
        print("\nCola vacía no hay datos para desencolar")
        return None
    d = self.primero.retornarDato()
    p = self.primerNodo()
    self.borrar(p)
    return d
 
 def siguiente (self):
     if self.esVacia():
         print("\nCola vacía no hay siguiente")
         return None
     d = self.primero.retornarDato()
     return d

a = colaLSL()
b = a.esVacia()
print(b)
a.encolar("a")
a.encolar("e")
a.encolar("i")
a.encolar("o")
a.recorrerLista()
b = a.esVacia()
print("\nEstá vacía? ", b)
d = a.desencolar()
print("\ndato desencolado es: ", d)
a.recorrerLista()
d = a.siguiente()
print("\nel siguiente es:", d)
a.recorrerLista()


# # 4. Cola con la clase queue

# In[7]:


import queue

q = queue.Queue()
print(q.qsize())

for i in range(5):
    q.put(i)
print("Tamaño,",q.qsize())

print("Está vacía?,",q.empty())
print("Desencolar",q.get())
print("Tamaño,",q.qsize())

while not q.empty():
    print(q.get(), end=' ')

print(q)


# # Ejercicios

# In[ ]:


import random

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
       y = nodoSimple.nodoSimple()
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


# In[ ]:


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

