#!/usr/bin/env python
# coding: utf-8

# # 1. Introducción
# - La programación orientada a objetos le permite definir nuevas clases a partir de clases existentes. A esto se le llama herencia.
# 
# - La herencia es una característica importante y poderosa para reutilizar software.
# 
# - Suponga que necesita definir clases para modelar tipos de empleados. Estas clases tienen muchas características comunes. 
# 
# ¿Cuál es una buena manera de diseñar estas clases para evitar la redundancia y hacer que el sistema sea fácil de comprender y mantener*?

# ### Herencia en Diagramas de Clases
# Para representar una herencia en un diagrama de clases se utiliza una flecha con punta blanca, que va desde la clase hija hacia la clase padre.
# 
# - Herencia simple: La herencia simple se apoya en el uso de clases base para compartir sus atributos y comportamientos con otros clases derivadas.
# 
# - Herencia múltiple: A diferencia de lenguajes como Java y C#, el lenguaje Python permite la herencia múltiple, es decir, se puede heredar de múltiples clases. 
# 
# <center><img src="Figures/S4-Extends.png" width="500" height="800"></center>

# #### Diferencias entre la superclase y la subclase
# 
# - Superclase: también llamada clase padre o clase base. 
#     - Una superclase no necesita a las subclases para existir, y cualquier modificación en cualquiera de las subclases no afecta el comportamiento, ni los elementos de la superclase.
# 
# - Subclase: también llamada clase hija.
#     - Una subclase hereda todos los atributos y métodos de la clase padre.
#     - Sin embargo, dependiendo de la manera en que se definan estos métodos o atributos, y del lenguaje de programación, la subclase puede tener o no acceso a ciertos elementos heredados.
#     - La subclase, también podrá agregar o redefinir elementos heredados.
#     - Una subclase requiere que exista la superclase.
#     
#  <center><img src="Figures/S4-Extends.png" width="700" height="1000"></center>

# PREGUNTAS
# 1. ¿Cuáles son los atributos de Estudiante?
# 2. ¿Cuáles son los métodos de Estudiante?
# 3. ¿Cuáles son los atributos de ProfesorAyudante?
# 4. ¿Cuáles son los métodos de ProfesorAyudante?
# 5. ¿Cuáles son los atributos de Persona?
# 6. ¿Cuál método redefine Estudiante?
# 
# <center><img src="Figures/S4-Extends.png" width="700" height="1000"></center>

# # Herencia simple
# <center><img src="Figures/S4-PersonaEmpleado.png" width="600" height="800"></center>

# In[ ]:


#SUPERCLASE
class Persona:   
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def getNombre(self):
        return self.nombre;
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def info(self):
        return f"Persona con nombre :{self.nombre}, edad {self.edad}"

persona1 = Persona("Lina",43)
print(persona1.nombre)
print(persona1.info())


# # Herencia simple
# <center><img src="Figures/S4-PersonaEmpleado.png" width="600" height="800"></center>

# In[ ]:


#SUBCLASE
#from empleadoPrueba import Persona
class Empleado(Persona): 
      pass


# •	Ejercicio [subClases] -> Codifique el siguiente programa:
# - Cree solo el nombre de las subclases (Estudiante y Profesor) e indique que heredan de persona.
# 
# <center><img src="Figures/S4-EjercicioSubclases.png" width="600" height="800"></center>

# In[ ]:


class Estudiante(Persona):
    pass

class Profesor(Persona):
    pass


# # Invocando los constructores de otras clases
# Un constructor de una subclase puede invocar al constructor de su superclase.
# 

# In[ ]:


class Empleado(Persona):
    
    def __init__(self, nombre, edad, empresa, supervisor):
        #Persona.__init__(self,nombre,edad) #Invocando al constructor de la superclase opcion1
        super().__init__(nombre,edad) # Forma común, OPCION2
        self.__empresa = empresa
        self.supervisor = supervisor
        
    def getEmpresa(self):
        return self.__empresa


# In[ ]:


persona2 = Persona("Andres", 36)
#persona2.supervisor # Error - persona no tiene ese atributo

empleado1 = Empleado("Camilo", 34,"MinTIC", "Lina")
print(empleado1.nombre)
print(empleado1.supervisor)
print(empleado1.getEmpresa())
empleado1.setNombre("Rosa")
print(empleado1.nombre)
#print(empleado1.__empresa()) #Error empresa es privado


# ¿Qué imprime al final?

# In[ ]:


class Persona:
    def __init__(self):
        self.nombre = "hola"
        print("Ejecuta constructor de persona")

class Empleado(Persona):
    def __init__(self):     
        Persona.__init__(self)
        print("Ejecuta constructor de empleado")

class Facultad(Empleado):
    def __init__(self): 
        Empleado.__init__(self)
        print("Ejecuta constructor de facultad")
        
facultad1 = Facultad()
print(facultad1.nombre)


# Si ninguno se invoca explícitamente, el compilador automáticamente busca el constructor del ancestro más cercano. 

# In[ ]:


class Persona:
    def __init__(self):
        self.nombre = "hola"
        print("Ejecuta constructor de persona")
 
class Empleado(Persona): 
     pass

class Facultad(Empleado):
     pass
        
facultad1 = Facultad() 
print(facultad1.nombre)


# •	Ejercicio [constructoresSubClases] -> Codifique el siguiente programa:
# - Desarrolle los constructores de las clases (Estudiante y Profesor) para que envién los atributos respectivos a la superclase Persona.
# - Cree una instancia de estudiante y persona, y pruebe que funcione correctamente.
# 
# <center><img src="Figures/S4-EjercicioSubclases.png" width="600" height="800"></center>

# In[ ]:


class Estudiante(Persona):
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre,edad)
        self.__nota = nota

class Profesor(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre,edad)
        self.salario = salario

e1 = Estudiante("Carlos",34,5)


# In[ ]:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad
        
    def getNombre(self) :
        return self.nombre;
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def info(self):
        result = f"Persona con nombre :{self.nombre}, edad {self.edad}"
        return result


# # Invocando los métodos de la superclase (Super())
# 
# Heredar de una superclase nos permite acceder a métodos y/o atributos de una superclase desde una subclase.
# 
# - Atributo de clase: nombreSuperClase.attribute
# - Atributo de instancia: self.attribute
# - Método: Super().nombreMétodo(parametros) 
# nombreSuperClase.method(self,parametros)
# 
# 
# 
# 
# 

# <center><img src="Figures/S4-PersonaEmpleado.png" width="600" height="800"></center>

# In[ ]:


class Empleado(Persona):
    
    def __init__(self, nombre, edad, empresa, supervisor):
        super().__init__(nombre,edad)
        self.__empresa = empresa
        self.supervisor = supervisor
        
    def getEmpresa(self):
        return self.__empresa;
    
    def setEmpresa(self,empresa):
        self.__empresa = empresa;        
    
    def info(self):
        #Invocando atributos y métodos de la superclase
        result1 = f"Empleado con nombre :{self.getNombre()}, edad:{self.edad}, empresa:{self.__empresa}, supervisor: {self.supervisor}"
        result2 = f"Empleado con nombre :{super().getNombre()},edad:{self.edad}, empresa:{self.__empresa}, supervisor: {self.supervisor}" 
        result3 = f"{super().info()}, empresa:{self.__empresa}, supervisor: {self.supervisor}"
        return result3  
    
#Qué pasa si borro el método info en Empleado?


# In[ ]:


persona2 = Persona("Andres", 36)
#print(persona2.info())
#persona2.getEmpresa() # Error - persona no tiene ese método

empleado1 = Empleado("Camilo", 34,"MinTIC", "Lina")
#print(empleado1.getNombre())
print(empleado1.info())


# •	Ejercicio [métodosSubClases] -> Codifique el siguiente programa:
# - Desarrolle los métodos de las clases (Estudiante y Profesor).
# - Cree una instancia de estudiante y persona, y pruebe que funcionen correctamente los métodos.
# 
# <center><img src="Figures/S4-EjercicioSubclases.png" width="600" height="1000"></center>

# # Iniciamos 8:05pm

# In[ ]:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad
        
    def getNombre(self):
        return self.nombre;
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def info(self):
        result = f"Persona con nombre :{self.nombre}, edad {self.edad}"
        return result

class Estudiante(Persona):
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre,edad)
        self.__nota = nota
        
    def info(self):
        f = f"{super().info()}, Nota {self.__nota}"
        return f

class Profesor(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre,edad)
        self.salario = salario
        
    def getSalario(self):
        return self.salario
        
    def setSalario(self, s):
        self.salario = s
    
    def info(self):
        f = f"{super().info()}, Salario {self.salario}"
        return f

e1 = Estudiante("Carlos",34,5)
e1.info()

p1 = Profesor("Carlos",34,5000000)
p1.info()
p1.setSalario(6000000)


# Al invocar la super clase, esta siempre trata de buscar la definición del método en el ancestro mas cercano (“el padre”); si no la encuentra, sigue con “el abuelo”, y así sucesivamente.
# 

# In[ ]:


class Vehiculo:
    def info(self):
        print("Mensaje desde Vehiculo")

class Terrestre(Vehiculo):
    def otro(self):
        print("Otro")
    
class Aereo(Vehiculo):
    def info(self):
        super().info()
        print("Mensaje desde aereo")

class Moto(Terrestre):
    def info(self):
        super().info()
        print("Mensaje desde moto")
    
aereo1 = Aereo()
aereo1.info()
moto1 = Moto()
moto1.info()


# # Herencia múltiple
# 
# - La herencia múltiple es la capacidad de una subclase de heredar de múltiples súper clases.
# 
# - Esto conlleva un problema, y es que si varias súper clases tienen los mismos atributos o métodos, la subclase sólo podrá heredar de una de ellas.
# 
# - En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase.
# 
# <center><img src="Figures/S4-HerenciaMultiple.png" width="500" height="800"></center>

# ## Herencia Múltiple
# <center><img src="Figures/S4-HerenciaMultiple.png" width="500" height="800"></center>

# In[ ]:


class FiguraGeometrica:
    def __init__(self,alto,ancho):
        self.alto = alto
        self.ancho = ancho
        
    def info(self):
        print("Soy FG")

class Color:
    def __init__(self,c):
        self.color = c
        
    def info(self):
        print("Soy Color")

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,alto,ancho, color = "Negro"):
        FiguraGeometrica.__init__(self,alto,ancho)
        Color.__init__(self,color)
        
    def area(self):
        a = self.alto * self.ancho
        return a
    
    def info(self):
        super().info()
        print("Soy Cuadrado")
    
c1 = Cuadrado(4,4)
print(c1.color)
print(c1.ancho) 
print(c1.area())  
c1.info()
c1.color = "Rojo"
print(c1.color)        
        


# In[ ]:





# •	Ejercicio [multipleProfesorAyudante] -> Codifique el siguiente programa:
# - Cree la clase faltante (ProfesorAyudante)
# 
# <center><img src="Figures/S4-Extends.png" width="500" height="800"></center>

# In[ ]:


class ProfesorAyudante(Estudiante,Profesor):
    def __init__(self,nombre, edad, nota, salario):
        Persona.__init__(self, nombre, edad)
        Estudiante.__init__(self,nota)
        Profesor.__init__(self,salario)
        
    def info(self):
        print(super().info())
        
pa1 = ProfesorAyudante("Carlos", 34,5,20000) 
print(pa1.nombre)
pa1.info()


# In[ ]:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad
        
    def getNombre(self):
        return self.nombre;
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def info(self):
        result = f"Persona con nombre :{self.nombre}, edad {self.edad}"
        return result

class Estudiante(Persona):
    def __init__(self,nota):
        self.nota = nota;
    def info(self):
        result = f"{super().info()}, nota {self.nota}"
        return result
        
class Profesor(Persona):
    def __init__(self,salario):
        self.salario = salario;
    def info(self):
        result = f"{super().info()}, salario {self.salario}"
        return result    


# ## Polimorfismo
# Dependiendo del objeto que pasemos en la referencia (self) es le método que se va a ejecutar.

# In[ ]:


class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Error - Las subclases son las que tienen sonido"
        
    def imprimirSonido(self):
        self.sonido()
        
class Gato(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def sonido(self):
        return "Miau Miau"
        
class Perro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def sonido(self):
        return "Guau Guau"
        
g1 = Gato("Jackie")
g2 = Gato("Ozzy")
p1 = Perro("Galaxia")
p2 = Perro("Trosqui")

t = [g1,g2,p1,p2]

def sonidos(arreglo): # arreglos = animales
    for i in arreglo:
        print(f"{i.nombre} tiene sonido {i.sonido()}")
        
sonidos(t)


# La variable animales toma la forma de Perro o Gato. Depende de la que se este ejecutando en el momento.

# # Ejercicios

# •	Ejercicio [Vehiculo] -> Codifique el siguiente programa:
# - Cree la clase Vehiculo con los atributos nombre y precio (privados).
# - Cree el método getPrecio(), que retorne el precio del vehiculo.
# 
# - Cree la clase Maritimo (que herede de Vehiculo) con el atributo de clase IVA = 20 (considérelo un porcentaje).
# - Cree el método getPrecio(), que retorne el precio de la instancia, más el IVA.
# 
# - Cree la clase Buque (que herede de Maritimo) 
# - Cree el método getPrecio(), que retorne la suma del getPrecio() del padre, más 40.
# 
# - Cree un archivo donde cree 4 vehículos (2 marítimos y 2 buques / invéntese valores de nombre y precios). En el proceso cree los constructores necesarios. 
# 
# - Imprima los precios finales de cada instancia.
# 
