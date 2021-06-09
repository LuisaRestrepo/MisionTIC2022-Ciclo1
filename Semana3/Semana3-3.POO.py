#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# - La programación orientada a objetos (POO) es esencialmente una tecnología para desarrollar software reutilizable.
# - La POO implica programar utilizando objetos. Un objeto representa una entidad del mundo real que puede identificarse claramente. 
# - Por ejemplo: un estudiante, un escritorio, un círculo, una casa, un carro, cualquier objeto en especifico. 
# - Cada objeto tiene una identidad única, unas propiedades (atributos), y unos comportamientos (métodos).
# 
# <center><img src="Figures/S3-Paradigma.png" width="700" height="1000"></center>

# ## Clase
# - Los objetos del mismo tipo se definen usando una clase común.
# - Una clase es una plantilla, modelo o contrato que define cuáles serán los atributos y métodos de un objeto. 
# - Un objeto es una instancia de una clase. 
# - Un programador puede crear muchas instancias de una clase. 
# - Crear una instancia se conoce como instanciación.
# 
# Si mi clase es una fruta, ¿Cuáles serían los objetos?

# 
# <center><img align="center" src="Figures/S3-Frutas.png" width="700" height="1000"></center>
# 
# 

# ### Componentes de una clase
# #### Propiedades (atributos)
# - Representan datos con valores pertenecientes al objeto. 
# - Mencione algunas propiedades que podría tener un objeto "Carro", "Circulo", "Rectangulo"
# 
# #### Comportamientos (métodos)
# - Representan acciones o métodos. Cada objeto puede invocar o ejecutar diferentes tipos de acciones.
# - Por ejemplo: un objeto circulo podría invocar métodos como getArea() – para obtener el área del circulo. O getPerimeter() para obtener el perímetro.
# - Mencione algunos comportamiento que podría tener un objeto "Carro"
# 
# <center><img src="Figures/S3-ClaseCarro.jpg" width="400" height="800"></center>

# ### UML
# - UML (lenguaje unificado de modelado) es el lenguaje de modelado de sistemas de software más conocido y utilizado en la actualidad.
# - La ventaja de utilizar modelos UML, es que permiten que programadores de diferentes regiones o incluso continentes, “hablen” en un mismo idioma.
# - Existen muchos tipos de modelos o diagramas UML. En este curso nos enfocaremos en el “diagrama de clases UML”. 
# <center><img src="Figures/S3-UMLLogo.png" width="300" height="400"></center>

# ### Diagrama de clases
# - Se utiliza para representar la clases del sistema.
# - Permite obtener un panorama general de mi aplicación sin necesidad de ir a mirar 200 archivos o más.
# - Permite observar de manera grafica como se relacionan las diferentes clases de mi sistema (se ve mas adelante).
# - Permite establecer un diseño de mi aplicación y presentársela a otros colegas o interesados.
# 
# <center><img src="Figures/S3-Clase.png" width="700" height="700"></center>

# ## 1. Creando una clase
# <center><img src="Figures/S3-Circulo.png" width="400" height="500"></center>

# In[ ]:


class Circulo: #Nombre de la clase
    pass
  
print(type(Circulo))


# # Creando un objeto
# Para crear un nuevo objeto Circulo se debe invocar el “nombre de la Clase” seguido por “()” -> Circulo(). 

# In[ ]:


circulo1 = Circulo() #Objeto de la clase circulo
print(circulo1)


# •	Ejercicio [ClasePersona] -> Codifique el siguiente programa:
# - Cree la clase Persona
# <center><img src="Figures/S3-NombreClase.png" width="500" height="600"></center>
# - Cree dos intancias de persona.

# In[ ]:


class Persona:
    pass

persona1 = Persona()
persona2 = Persona()


# ## 2. Atributos de instancia
# Representan datos con valores pertenecientes al objeto.
# Por ejemplo: un objeto estudiante podría tener: nombre, edad, genero, correo, entre otros. 
# - Ejm: Piense en los atributos que podría tener las clases Frutas, Carro

# ## 2.1 Inicializador de python (Constructor)
# 
# Función \__init\__ es una función especial que se le puede colocar a una clase en Python. El objetivo fundamental de la función \__init\__ es inicializar los atributos del objeto que creamos.
# 
# Características de la función \__init\__:
# - Se ejecuta inmediatamente luego de crear un objeto.
# - La función \__init\__ no puede retornar dato.
# - La función \__init\__ puede recibir parámetros que se utilizan normalmente para inicializar atributos.
# - La función \__init\__ es un método opcional, pero de todos modos es muy común declararlo.
# 

# In[ ]:


class Circulo:
    def __init__(self):
        print("Se creó un objeto")
           


# # Creando un objeto con __init__

# - `self` es un parámetro que reciben la mayoría de las funciones definidas en las clases. Sirve para identificar el objeto actual.
# - Para crear un nuevo objeto Circulo se debe invocar el “nombre de la Clase” seguido por “()” -> Circulo(). Automáticamente se llamará la función init. Y aunque esa función recibe un parámetro (self), ese parámetro no hay que enviarlo, ya que Python lo carga automáticamente.

# In[ ]:


class Circulo:
    def __init__(self):
        print("Se creó un objeto")
        
circulo1 = Circulo()
circulo2 = Circulo()


# # Agregando atributos
# Para invocar un atributo de instancia: $referenciaInstancia.atributoInstancia$
# 
# <center><img src="Figures/S3-Circulo.png" width="300" height="300"></center>

# In[ ]:


class Circulo:
    def __init__(self):
        self.radio = 8
        self.descripcion = "Hola Circulo"


# In[ ]:


circulo1 = Circulo()
print(circulo1.radio) #Ojo: invocando un atributo de instancia
print(circulo1.descripcion) #Ojo: invocando un atributo de instancia
circulo2 = Circulo()
print(circulo2.radio) #Ojo: invocando un atributo de instancia


# ## 2.1 Inicializador de python con parámetros
# - En el ejemplo anterior, todos los círculos quedaban con radio de 8.0. Sin embargo, en los sistemas reales, cada Circulo debería poder tener su propio radio.
# - Veamos como mejorar el sistema anterior para que a cada Circulo se puede asignar su propio radio.

# In[ ]:


class Circulo:
    descripcion = "Hola Circulo"
    pi = 3.14
    
    def __init__(self, x,color = "rojo"): #x = 5
        self.radio = x
        self.color = color
    
circulo1 = Circulo(5)
print(circulo1.radio) #Ojo: invocando un atributo
print(circulo1.descripcion) 
print(circulo1.color)
circulo2 = Circulo(5)
print(circulo2.radio)

print(Circulo.descripcion)


# •	Ejercicio [AtributosPersona] -> Codifique el siguiente programa:
# - Cree los atributos para la clase Persona: (El atributo nacimiento se refiere al año de nacimiento)
# <center><img src="Figures/S3-AtributosClase.png" width="500" height="600"></center>
# - Cree dos intancias de persona y envié parámetros diferentes.
# - Imprima la información de cada persona.

# In[ ]:


class Persona:
  def __init__(self, n, a, nac):
      self.nombre = n
      self.apellido = a
      self.nacimiento = nac


# In[ ]:


n = input("Ingrese nombre")

persona1 = Persona(n, "", 1992) #Objeto persona1
print(persona1)
print(persona1.nombre)  #Ojo: invocando un atributo de instancia
print(persona1.apellido)
print(persona1.nacimiento)

persona2 = Persona("Andrés", "Mesa", 1990) #Objeto persona2
print(persona2)
print(persona2.nombre)  #Ojo: invocando un atributo de instancia
print(persona2.apellido)
print(persona2.nacimiento)

persona2.apellido = "Gomez"
print(persona2.nombre)  #Ojo: invocando un atributo de instancia
print(persona2.apellido)
print(persona2.nacimiento)


# # 3. Atributos de clase (static)
# Atributos pertenecientes a la clase, no depende de la existencia de los objetos y es compartida para todas las instancias.

# In[ ]:


class Gafa:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.IVA = 0.19
        self.ENVIO = 500
    
gafa1 = Gafa("Gafita1",70000)
    


# ¿Algún comentario? Si creo 10000 gafas

# <center><img src="Figures/S3-GafaM.png" width="700" height="800"></center>

# Se gasta espacio en memoria repitiendo los mismos valores 20 o más veces
# 

# # Iniciamos 8:05pm
# - A mitad de la sesión la tutora dara algunas sugerencias sobre el desarrollo del reto
# - Reto 1 - 10% del ciclo

# In[ ]:


class Gafa:    
    IVA = 0.19
    ENVIO = 500
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

print(Gafa.IVA) #Invocando un atributo de clase


# Ahora los atributos ENVIO e IVA no le pertenecen a cada objeto, ahora se comparten por la clase.
# 
# <center><img src="Figures/S3-GafaR.png" width="700" height="800"></center>

# •	Ejercicio [precioPagarGafa] -> Codifique el siguiente programa:
# - Calcule el precio total a pagar para cada gafa.

# In[ ]:


class Gafa:    
    IVA = 0.19
    ENVIO = 500
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

print(Gafa.IVA) #Invocando un atributo de clase

gafa1 = Gafa("Gafita1",5000)
totalGafa1 = gafa1.precio + (gafa1.precio * Gafa.IVA) + Gafa.ENVIO
print(totalGafa1)
gafa2 = Gafa("Gafota",1005000)
totalGafa2 = gafa2.precio + (gafa2.precio * Gafa.IVA) + Gafa.ENVIO
print(totalGafa2)


# # 4. Agregando métodos
# Representan acciones o métodos. Cada objeto puede invocar o ejecutar diferentes tipos de acciones.

# ## Funciones
# - Tal como vimos en el diagrama de clases, nos quedaría faltando una zona para completar la transición, entre el diagrama de clases y el código. Esa zona es la zona de funciones. 
# 
# - En Python a las clases se les pueden asociar funciones, para hacer esto, basta con definir la función dentro del espacio de la definición de la clase.
# 
# - Esa función estará disponible para todas las instancias pertenecientes a esa clase.
# 
# <center><img src="Figures/S3-Circulo.png" width="300" height="300"></center>

# In[ ]:


import math
class Circulo: #Nombre de la clase
    
    descripcion = "Hola Circulo"
    
    #Atributos de intancia
    def __init__(self, radio): 
        self.radio = radio
        
    #Métodos
    def getRadio(self):
        return self.radio
    
    def setRadio(self,n):
        self.radio = n
    
    def getPerimetro(self):
        p = 2*math.pi*self.radio
        return  p
    
    def getArea(self):
        a = math.pi*self.radio**2
        print("Perimetro",self.getPerimetro())
        return a    
    
circulo1 = Circulo(5)
print("Area",circulo1.getArea())
circulo1.setRadio(7)
print("Area",circulo1.getArea())


# ## Sugerencia:
# - Siempre que vaya a invocar un atributo o método de instancia dentro de la misma clase, invóquela siguiendo el patrón:
#     - Atributo: $self.nombreAtributo $
#     - Método: $self.nombreMetodo()$
# 
# - Siempre que vaya a invocar un atributo o método de clase, invóquela siguiendo el patrón:
#     - Atributo: $NombreClase.atributoDeClase$
#     - Método: $NombreClase.metodoDeClase()$
#     
# - Siempre que vaya a invocar un atributo o método de instancia, invóquela siguiendo el patrón:
#     - Atributo: $NombreInstancia.atributoDeInstancia$
#     - Método: $NombreInstancia.metodoDeInstancia()$
# 

# In[ ]:


circulo1 = Circulo(4)
print("Radio - ",circulo1.radio) # Invocando un atributo de instancia
print("Descripción 1 - ",Circulo.descripcion) # Invocando un atributo de clase ** la forma común
print("Descripción 2 - ",circulo1.descripcion) # Invocando un atributo de clase

print("Perimetro 1 - ",circulo1.getPerimetro()) # Invocando un método OPCION1 ** la forma común
print("Perimetro 2 - ",Circulo.getPerimetro(circulo1)) # Invocando un método OPCION2
print(circulo1.getArea())


# •	Ejercicio [precioPagarGafa] -> Codifique el siguiente programa:
# - Cree el método precioPagar() para la clase gafa, la cual debe ser el precio+iva+envio, y devuelva el total
# - Por fuera de la función cree dos instancias de gafa e invoque el método creado, finalmente imprima el resultado.

# In[ ]:


class Gafa:
    IVA = 0.19
    ENVIO = 500
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def precioPagar(self):
        return self.precio + (self.precio * Gafa.IVA) + Gafa.ENVIO
    
    def setPrecio(self, p):
        if(p > 10000):
            self.precio = p
        else:
            print("No se puede modificar")
   
gafa1 = Gafa("Gafita1",5000)
print(gafa1.precioPagar())

gafa1.setPrecio(8000)
print(gafa1.precioPagar())
gafa1.precio = 80000

gafa2 = Gafa("Gafota",1005000)
print(gafa2.precioPagar())


# •	Ejercicio [MetodosPersona] -> Codifique el siguiente programa:
# - Cree los métodos para la clase Persona:
#     - getNacimiento() debe devolver el año de nacimiento de la persona.
#     - setNacimiento() debe modificar el año de nacimiento solo si la edad calculada de la nueva fecha es mayor o igual a 18 años, de no ser así imprima un mensaje que diga "Cambio no realizado: no se permiten empleados menores de edad".
#     - calcularEdad() debe calcular los años de la persona a partir de la fecha de nacimiento.
#     - imprimirInfo() debe devolver un string con la información de la persona (nombre, apellido y edad)
# <center><img src="Figures/S3-MetodosClase.png" width="500" height="600"></center>
# - Cree dos intancias de persona y envié parámetros diferentes.
# - Invoque todos los métodos creados.

# In[ ]:


import datetime

class Persona:
    def __init__(self, n, a, nac): 
        self.nombre = n
        self.apellido = a
        self.nacimiento = nac
        
    def getNacimiento(self):
        return self.nacimiento
    
    def setNacimiento(self, n):
        anno = datetime.datetime.now().year
        c = anno-n
        print(c)
        if(c>=18):
            self.nacimiento = n
        else:
           print("Cambio no realizado: no se permiten empleados menores de edad") 
    
    def calcularEdad(self):
        anno = datetime.datetime.now().year
        return anno-self.nacimiento
    
    def imprimirInfo(self):
        s = f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.calcularEdad()}"
        return s
        
persona1 = Persona("Luisa","Restrepo",1992)
persona1.setNacimiento(2010)
print(persona1.calcularEdad())
print(persona1.imprimirInfo())

persona2 = Persona("Andres","Rincon",1998)
print(persona2.calcularEdad())
print(persona2.imprimirInfo())


# In[ ]:


#from nombreArchivo import Persona # Si están en otro archivo

persona1 = Persona("Lina", "Mesa", 34)
print(persona1.nombre)  
print(persona1.apellido)
#print(persona1.__edad) # Error
print(persona1.getEdad())

persona1.setEdad(12)
print(persona1.toString())

persona1.setEdad(25)
print(persona1.toString())


# # Clases en diferentes archivos
# Para importar la clase en otro archivos, hay dos formas:

# In[ ]:


#Mi archivo se llama CirculoClass.py
import math
class Circulo: 
    
    #Atributos de instancia
    def __init__(self, radio): 
        self.radio = radio
        self.descripcion = "Hola Circulo"


# In[ ]:


import CirculoClass #Forma1
from CirculoClass import Circulo #Forma2

circulo1 = Circulo(4)
print(circulo1.radio) #Ojo: invocando un atributo
print(circulo1.descripcion)


# # Utilizando los métodos

# ### Arreglo de objetos

# In[ ]:


circulo1 = Circulo(8.0)
circulo2 = Circulo(5.0)
circulo3 = Circulo(3.5)
arregloCirculos = []
arregloCirculos.append(circulo1)
arregloCirculos.append(circulo2)
arregloCirculos.append(circulo3)

print(arregloCirculos)

for circ in arregloCirculos:
    print(circ.radio)

print(arregloCirculos[0].radio)
print(arregloCirculos[0].getPerimetro())


# In[ ]:


class Circulo: 
    
    #Atributos de instancia
    def __init__(self, radio): 
        self.radio = radio
        self.descripcion = "Hola Circulo"

#Utilizando un for para crear objetos
arregloCirculos = []
for i in range(5):
    r = input("radio")
    circulo = Circulo(r)
    arregloCirculos.append(circulo)
    print(f"Radio en la posicion {i} tiene radio {arregloCirculos[i].radio}")


# ### Envió de arreglo a método

# In[ ]:


import math
class Circulo: 
    descripcion = "Hola Circulo"   
    def __init__(self, radio): 
        self.radio = radio
    
    def imprimirRadiosConIndice(arregloCirculos):
        for x in range(len(arregloCirculos)): 
            print(f"Radio del cículo {x+1} es {arregloCirculos[x].radio}")        
            
    def imprimirRadiosSinIndice(arregloCirculos):
        for circ in arregloCirculos: 
            print("Radio",circ.radio)  
           

Circulo.imprimirRadiosConIndice(arregloCirculos)
Circulo.imprimirRadiosSinIndice(arregloCirculos)


# ### Métodos que reciben otros objetos

# In[ ]:


import math
class Circulo: 
    descripcion = "Hola Circulo"   
    def __init__(self, radio): 
        self.radio = radio
    
    def dobleCirculo(self,circ):
        print("Radio del circulo que invoca",self.radio)
        print("Radio del circulo que recibo",circ.radio)

circulo1 = Circulo(8.0)
circulo2 = Circulo(5.0)

circulo1.dobleCirculo(circulo2)


# ### Métodos que devuelven objetos

# In[ ]:


class Circulo: 
    descripcion = "Hola Circulo"   
    def __init__(self, radio): 
        self.radio = radio
    
    def nuevoCirculo(self):
        nuevo = Circulo(self.radio*5)
        return nuevo
        

circulo1 = Circulo(8.0)
otroCirc = circulo1.nuevoCirculo()
print(otroCirc.radio)


# # Visibilidad de los atributos y métodos
# Una clase revela sus métodos y atributos a otras clases usando visibilidad (encapsulamiento)
# Hay cuatro tipos diferentes de visibilidad que se pueden aplicar a los atributos y métodos de una clase (Publica “+”, Protegida, de Paquete y Privada “-”).
# 
# | Representación Clase  || Python  || Java  ||  Objetivo |
# |  --             ||  --     || --    || --        |
# |  +              ||   **Default**       || public || Pública: accesible para todos|
# |  -              ||  \__    || private||Privada: Solo podrá ser accedida o modificada por la misma clase|
# |  #              || (no aplica) || protected || Protegida: Establece que solo puede ser accedido por esa clase y sus sub-clases|
# |  ~              || (no aplica) || **Default**  || Paquete: Establece que solo puede ser accedido por las clases dentro del paquete|

# In[ ]:


import math
class Circulo: 
    
    def __init__(self, radio): 
        self.radio = radio
        self.descripcion = "Hola Circulo"
        
    def getRadio(self):
        return self.radio;
    
    def setRadio(self,radio):
        if(radio >= 0):
            self.radio = radio;
        else:
            print("No se puede asignar un radio negativo")
    
circulo1 = Circulo(4)
print("Antes del cambio: ",circulo1.radio)
circulo1.radio = 8 #No debería permitir modificar la variable directamente
print("Después del cambio: ",circulo1.radio)


# Para encapsular, básicamente tendremos que añadirle dos guiones bajos "_ _ " delante de la propiedad que queremos ocultar.

# In[ ]:


import math
class Circulo: 
    
    def __init__(self, radio): 
        self.__radio = radio
        self.descripcion = "Hola Circulo"
        
    def getRadio(self):
        return self.__radio;
    
    def setRadio(self,radio):
        if(radio >= 0):
            self.__radio = radio;
        else:
            print("No se puede asignar un radio negativo")
    
circulo1 = Circulo(4)
#print("Error: ",circulo1.__radio)
print("Error: ",circulo1.getRadio())

circulo1.__radio = -10
print("Radio: ",circulo1.getRadio())

circulo1.setRadio(5)
print("Radio: ",circulo1.getRadio())

circulo1.setRadio(-10)


# •	Ejercicio [VisibilidadPersona] -> Codifique el siguiente programa:
# - Modifique la visibilidad del atributo nacimiento para que no pueda ser modificado por fuera de la clase.
# <center><img src="Figures/S3-VisibilidadClase.png" width="300" height="300"></center>

# In[ ]:





# # Ejercicios

# •	Ejercicio [PointClass] -> Codifique el siguiente programa:
# - Cree la estructura de la siguiente clase que nos permitirá almacenar las coordenadas en un plano carteasino.
# <center><img src="Figures/S3-PointClass.png" width="300" height="300"></center>

# In[ ]:





# •	Ejercicio [PointDistance] -> Codifique el siguiente programa:
# - Suponga que se le pide calcular la distancia entre dos puntos.
# - La formula es la siguiente:
# <center><img src="Figures/S3-PointDistance.png" width="300" height="300"></center>
# - Cree la lógica del método distance. 
# - Cree dos intancias de la clase Point y calcule la distancia entre los dos puntos.

# In[ ]:





# •	Ejercicio [PointMidP] -> Codifique el siguiente programa:
# - Suponga que queremos encontrar el punto medio entre dos puntos.
# <center><img src="Figures/S3-PointMedio.png" width="300" height="300"></center>
# - Construya un método llamado midP() en la clase Point, que encuentre el punto medio entre dos puntos (debe recibir el objeto p como parámetro). Y la función deberá retornar un nuevo objeto (con las coordenadas x y y del punto medio) de la clase Point.

# In[ ]:





# •	Ejercicio [Planetas] -> Codifique el siguiente programa:
# - Cree la siguiente clase en Python.
# - Cree el constructor que reciba el nombre y la masa, y los asigne a los atributos respectivos.
# - Por fuera de la clase, cree objetos de la clase Planeta y pruebe los métodos que crearon.
# <center><img src="Figures/S3-Planeta.png" width="300" height="300"></center>
