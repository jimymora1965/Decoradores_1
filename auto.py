class Auto:
    def __init__(self, modelo, año):
        self._m = modelo
        self._a = año
        
   
    @property
    def modelo(self):
        return self._m
    
    @property
    def año(self):
        return self._a
    
    @modelo.setter
    def modelo(self,nuevo_modelo):
        self._m = nuevo_modelo
        
    @año.setter
    def año (self, nuevo_año):
        self._a = nuevo_año        
        
carro = Auto("Aveo", "2010")
#auto1 = carro.modelo,carro.año: Si imprimo asi me muestra una lista
#print(auto1)
chevrolet_m= carro.modelo
chevrolet_a = carro.año
print(chevrolet_a,chevrolet_m)


