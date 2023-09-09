""" class Persona:
    def __init__(self,nombre, edad):
        self.n = nombre
        self.e = edad
        
    def get_nombre(self):
        return self.n
    
    def get_edad(self):
        return self.e

persona1 = Persona("jimy",58)

nombre_persona1 = persona1.get_nombre()
edad_persona1 = persona1.get_edad()

print(nombre_persona1)
print(edad_persona1) """

""" #utilizaremos properties para evitar usar el llamado de persona1.getnombre() y persona1.getedad(). creamos un property y convertimos la funcion get() en una propiedad por lo tanto no necesitamos llamarla

class Persona:
    def __init__(self, nombre, edad):
        self.n = nombre #propiedades publicas
        self.e = edad #propiedades publicas
        
        
    @property#convierte la funcion get en una propiedad
    def get_nombre(self):
        return self.n
    
    
persona1 = Persona("Christian",26)
nombre_persona1 = persona1.get_nombre# no usamos get(), solamente get.
print(nombre_persona1)
        
         """
         
#utilizaremos properties para evitar usar el llamado de persona1.getnombre() y persona1.getedad(). creamos un property y convertimos la funcion get() en una propiedad por lo tanto no necesitamos llamarla

#propiedades privadas self._nombre, self._edad
""" class Persona:
    def __init__(self, nombre, edad):
        self.__n = nombre    #propiedades publicas
        self._e = edad     #propiedades publicas
        
        
    @property #al usar esto no necesito usar la funcion get()
    def nombre(self):
        return self.__n      # atributo privado
    
     # ESTE ES OTRO DECORADOR QUE NACE POR EL @PROPERTY y REEMPLAZA AL SETTER
    @nombre.setter
    def nombre(self, new_nombre):
        self.__n = new_nombre
        
    
    
persona1 = Persona("Christian",26)
datos_persona1 = persona1.nombre
print(datos_persona1)

persona1.nombre = "Valentina"
datos_persona1 = persona1.nombre
print(datos_persona1)
         """
         
class Persona:
    def __init__(self, nombre, edad):
        self.__n = nombre    #propiedades publicas
        self.__e = edad     #propiedades publicas
        
        
    @property #al usar esto no necesito usar la funcion get()
    def nombre(self):
        return self.__n      # atributo privado
    
    @property
    def edad(self):
        return self.__e
    
     # ESTE ES OTRO DECORADOR QUE NACE POR EL @PROPERTY y REEMPLAZA AL SETTER
    @nombre.setter
    def nombre(self, new_nombre):
        self.__n = new_nombre
        
    @edad.setter
    def edad(self, new_edad):
        self.__e = new_edad
    
#creamos objeto e imprimos sus propiedades.
persona1 = Persona("Christian",26)
nombre_persona1 = persona1.nombre
edad_persona1 = persona1.edad
print(nombre_persona1)
print(edad_persona1)

print("Ahora modificamos las propiedades utilizando @property:")
#modificamos las propiedades del objeto persona1
persona1.nombre = "Valentina"
nombre_persona1 = persona1.nombre
persona1.edad = "23"
edad_persona1 = persona1.edad

print(nombre_persona1)
print(edad_persona1)

class Animal:
    def __init__(self, raza, origen):
        self.__r = raza
        self.__o = origen
        
    @property
    def raza(self):
        return self.__r 
    
    @property
    def origen(self):
        return self.__o
    
    @raza.setter
    def raza(self, nueva_raza):
        self.__r =  nueva_raza
    
    @origen.setter
    def origen(self, nuevo_origen):
        self.__o = nuevo_origen
    
animal1 = Animal("Chihuahua", "Mexico")
raza = animal1.raza
origen = animal1.origen
print(raza, origen)    