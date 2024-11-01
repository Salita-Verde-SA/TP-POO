from Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def getSuperficieTotalTerreno(self):
        return sum(a.superficieTerreno for a in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        return sum(a.superficieTerreno for a in self.viviendas if a.manzana == manzana)

    def getSuperficieTotalCubierta(self):
        return sum(a.getMetrosCuadradosCubiertos() for a in self.viviendas)
