class Vehiculo:
    marca = ''
    velMax = 4

    def __init__(self, marca, velMax):
        self.marca = marca
        self.VelMax = velMax

    def getMarca(self):
        return self.marca
