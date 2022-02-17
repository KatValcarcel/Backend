class Vehiculo:
    """clase que sirve para el uso de los vehiculos"""

    def _init_(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        self.velocidad = 0

    def acelerar(self):
        '''metodo que acelera el vehiculo de 20 en 20'''
        self.velocidad += 20
        return 'La velocidad actual es {} km/h'.format(self.velocidad)
