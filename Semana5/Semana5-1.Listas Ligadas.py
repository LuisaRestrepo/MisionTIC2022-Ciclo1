#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# - Una lista ligada es una colección de elementos que están enlazados entre sí, en donde cada elementos contiene un valor hacia los otros elementos.
# - Se dice que es eficiente porque permiten un menor desperdicio de memoria y además los algoritmos para se manejo suelen ser menos costosos computacionalmente.
# - Forma alterna de  representación en la cual las operaciones de inserción y borrado sean eficientes.
# 
# <center><img src="Figures/S5-ListaLigadaSimple.png" width="1000" height="1100"></center>

# Forma general de como se debe agregar un nuevo elemento a la estructura:
#  
# 
# <center><img src="Figures/S5-LLNuevoValor.png" width="800" height="1000"></center>

# # Nodo
# - El bloque constructivo básico para la implementación de la lista enlazada es el nodo. 
# - Cada objeto nodo debe contener al menos dos piezas de información. En primer lugar, el nodo debe contener el ítem de lista en sí mismo. 
# - Cada nodo debe contener una referencia al siguiente nodo. 
# - Para construir un nodo, usted debe proporcionar el valor inicial del dato del nodo.
# - El valor de referencia de Python `None` indicará el hecho de que no hay nodo siguiente.
# 
# 
# <center><img src="Figures/S5-Nodo.png" width="500" height="800"></center>

# In[10]:


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


# In[ ]:


nodo1 = nodoSimple("Hola")
nodo2 = nodoSimple("grupos")
nodo3 = nodoSimple("82-83-84")


# # Lista
# 
# Ventajas:
# 
# - Una lista ligada estará representada por objetos de la clase LSL, los cuales tendrán una variable de instancia que apunte al primer objeto NodoSimple de la lista y otro que apunte al último, cuando la lista está vacía dichas variables apuntarán a None
# - La lista no ordenada se construirá a partir de una colección de nodos.
# - Cada uno vinculado al siguiente mediante referencias explícitas. 
# - La clase LSL debe mantener una referencia al primer nodo y el último. 
# 
# Desventajas:
# - Utilizan más memoria que las matrices debido al almacenamiento utilizado por sus punteros.
# - Los nodos en una lista vinculada deben leerse en orden desde el principio, ya que las listas vinculadas son intrínsecamente de acceso secuencial.

# In[8]:


#from nodoSimple import nodoSimple
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
        x = nodoSimple(d) #cambio
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
        self.desconectar(x,y)
          
    def desconectar (self, x, y):
        if y == None:
            self.primero = x.retornarLiga()
            if self.esVacia():
                self.ultimo = None
        else:
            y.asignarLiga(x.retornarLiga())
            if x == self.ultimo:
                self.ultimo = y


# - El método `estaVacia()`, simplemente comprueba si el primero de la lista es una referencia a None. El resultado de la expresión booleana self.primero == None sólo será verdadero si no hay nodos en la lista enlazada.

# In[3]:


class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None
    def esVacia (self):
        return self.primero == None


# In[4]:


miLista = LSL()
print("miLista está vacía?",miLista.esVacia()) # Aún no hay elementos


# ### Agregando nodos
# 1. El método `agregarDato()`. Crea un nuevo nodo y hace que el dato del nodo sea el elemeto recibido. Luego une el nuevo nodo a la estructura existente (en la última posición).  Cambia la referencia de la liga del nodo de ser necesario y la referencia del último nodo.
# 2. El método `recorrerLista()`. Imprime el dato de cada nodo y el valor del atributo liga del último nodo.
# 3. El método `finDeRecorrido()`. Válida si el valor del atributo liga para el nodo es None. Devolviendo True o False.
# 4. El método `longitud()`. Devuelve la cantidad de nodos que posee la lista ligada.

# In[6]:


class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None
    def agregarDato (self, d):
        x = nodoSimple(d)
        p = self.primerNodo()
        if p == None:
            self.primero = x
            self.ultimo = x
        else:
            self.ultimo.liga = x
            self.ultimo = x
    def primerNodo(self):
        return self.primero
    def finDeRecorrido (self, p):
        return p == None
    def recorrerLista (self):
        p = self.primerNodo()
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end = ", ")
            p = p.retornarLiga()


# In[11]:


miLista = LSL() #Creando un objeto de lista ligada
miLista.agregarDato("Hola")
miLista.agregarDato("grupos")
miLista.agregarDato("82-83-84")

miLista.recorrerLista()
print("Longitud: ",miLista.longitud())


# •	Ejercicio [crearLSL] -> Codifique el siguiente programa:
# - Cree un objeto de la clase lista ligada
# - Construya un ciclo que solicité repetidamente datos al usuario, y termine la ejecución cuando el valor ingresado sea cero.
# - Agregue el dato ingresado a su lista ligada.
# - Al finalizar el ciclo, imprima el contenido de la lista ligada y la longitud de esta.

# In[14]:


d = input("Ingrese el dato del nodo o ingrese cero para terminar: ")
while d != "0":
    miLista.agregarDato(d)
    d = input("Ingrese el dato del nodo o ingrese cero para terminar: ")
miLista.recorrerLista()   
print("Longitud: ",miLista.longitud())
l = miLista.longitud()


# ### Insertar un nodo en la posición correspondiente
# 1. El método `buscarDondeInsertar()`. Retorna una referencia al nodo inmediatamente anterior (donde la longitud sea menor que el dato ingresado) a donde debemos insertar el nuevo, entonces insertar crea el nuevo nodo, actualiza la liga nuevo nodo y la del anterior.
# 2. El método `insertar()`. Recibe el dato del nuevo nodo y la referencia del nodo que debe conectar con el nuevo. Este método crea un nuevo nodo con el dato recibido e invoca el método conectar enviandole el nuevo nodo y la referencia del nodo a conectar.
# 3. El método `conectar()`, si el resultado de `buscarDondeInsertar()` es None, inserta el nuevo nodo en la primera posición, de no ser así, cambia las referencias de los nodos respectivos.

# In[ ]:


class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None
    def buscarDondeInsertar(self, d):
        p = self.primerNodo()
        y = None
        while not self.finDeRecorrido(p) and p.retornarDato() < d:
            y = p
            p = p.retornarLiga()
        return y
    def insertar (self, d, y):
        x = nodoSimple(d)
        self.conectar(x, y)
    def primerNodo(self):
        return self.primero
    def finDeRecorrido (self, p):
        return p == None
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


# In[15]:


d = "cómo están?"
x = miLista.buscarDondeInsertar(d)
print(x.dato)
miLista.insertar(d,x)
e = "Hi"
miLista.insertar(e) #Ingresa en la primera posición
miLista.insertar("Hi")
miLista.insertar("Hi")
miLista.insertar("Hi")
print(miLista.recorrerLista())


# •	Ejercicio [insertarLSL] -> Codifique el siguiente programa:
# - Construya un ciclo que solicité 10 datos al usuario.
# - Inserte el dato en lista ligada de manera ordenada.
# - Al finalizar el ciclo, imprima el contenido de la lista ligada y la longitud de esta.

# In[ ]:





# ### Eliminar un nodo
# 1. El método `buscarDato()`. Recibe el dato a buscar y un nodo vacío. Si encuentra el nodo que coincide, devuelve la referencia al nodo.
# 2. El método `borrar()`. Recibe el resultado del método `buscarDato()` y el nodo creado anteriormente. Si el resultado no fue None, se procede a desconectar el nodo.
# 3. El método `desconectar()`. Modifica las referencias en el atributo liga, para desconectar el nodo a eliminar.
# 

# In[ ]:


class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None
    def buscarDato (self, d, y):
        x = self.primerNodo()
        while not self.finDeRecorrido(x) and x.retornarDato() != d:
            y.asignarDato(x)
            x = x.retornarLiga()
        return x
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
            self.desconectar(x,y)
       
    def desconectar (self, x, y):
         if y == None:
                self.primero = x.retornarLiga()
                if self.esVacia():
                    self.ultimo = None
        else:
            y.asignarLiga(x.retornarLiga())
            if x == self.ultimo:
                self.ultimo = y
    def finDeRecorrido (self, p):
        return p == None


# - Para borrar un nodo de la lista, tenemos que encontrarlo en la lista; el método buscarDato("Hi", y) retorna una referencia al nodo que tiene a la “Hi” como dato y  el objeto __y__ será el nodo anterior. 
# 
# - Por lo tanto __x__ será una referencia al nodo donde está “Hi” y __y__ será una referencia al nodo anterior (o None si es el primero), luego se llama al método borrar(x, y) que finalmente lo que hace es cambiar la liga de __y__ que es el nodo anterior por la liga de __x__ que es el nodo actual.

# In[20]:


miLista.recorrerLista()

d = "grupos"
y = nodoSimple()
x = miLista.buscarDato(d,y)
print("Dato encontrado",x.dato)
miLista.borrar(x, y)
miLista.recorrerLista()


# In[21]:


miLista.recorrerLista()
x = miLista.primerNodo()
miLista.borrar(x)
print("Después de borrar el primer nodo")
miLista.recorrerLista()
print("Longitud: ",miLista.longitud())

