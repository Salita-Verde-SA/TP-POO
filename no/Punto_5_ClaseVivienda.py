from Punto_5_ClaseHabitacion import Habitacion
class Vivienda:
    def __init__(self,calle,nro,manzana,nrCasa,superficieTerreno):
        self.calle=calle
        self.nro=nro
        self.manzana=manzana
        self.nroCasa=nrCasa
        self.superficieTerreno=superficieTerreno
        self.habitacion=[]
        
    def getMetrosCuadradosCubiertos(self):
        habitacion1=Habitacion("Cocina",150)
        habitacion2=Habitacion("Living",100)
        habitacion2=Habitacion("Cocina",150)
        
        
        
        