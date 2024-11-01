from Habitacion import Habitacion
class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno, habitaciones):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = habitaciones

    def getMetrosCuadradosCubiertos(self):
        total_cubierto = sum(h.metrosCuadrados for h in self.habitaciones)
        if total_cubierto > self.superficieTerreno:
            raise Exception("Error")
        return total_cubierto
