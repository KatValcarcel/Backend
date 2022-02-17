class Vehiculo:
    """clase que sirve para el uso de los vehiculos"""

    def _init_(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        self.__velocidad = 0

    def acelerar(self):
        '''metodo que acelera el vehiculo de 20 en 20'''
        self.__velocidad += 20

    def desacelerar(self):
        '''metodo que desacelera el vehiculo de 20 en 20'''
        self.__velocidad -= 20
        return self.__velocidad

    def getVelocidad(self):
        return self.__velocidad

# hereda


class VehiculoVolador(Vehiculo):
    def __init__(self, color, modelo, traccion, vuela=False):
        super().__init__(color, modelo, traccion)
        self.__vuela = vuela

    def volar(self):
        self.__vuela = True

    def aterrizar(self):
        self.__vuela = False

    def estado(self):
        estado_volando = 'está volando' if self.__vuela else 'está aterrizado'
        return 'El vehículo es de color {}, modelo {}, tracción {}, y {}'.format(self.color, self.modelo, self.getVelocidad(), self.estado_volando)


objVehiculoVolador = VehiculoVolador('azul', 'modelo', '4x4', True)
print(objVehiculoVolador.estado())
