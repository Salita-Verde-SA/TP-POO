# Main.py
from Barrio import Barrio
from Vivienda import Vivienda
from Habitacion import Habitacion

barrio = Barrio("Colonia", "Constructora")

vivienda1 = Vivienda(
    "Salta", 123, "A", 1, 150.0,
    [Habitacion("Living", 30.0), Habitacion("Cocina", 20.0), Habitacion("Dormitorio", 25.0)])

vivienda2 = Vivienda(
    "Rivadavia", 456, "A", 2, 200.0,
    [Habitacion("Living", 40.0), Habitacion("Cocina", 25.0), Habitacion("Dormitorio", 35.0)])

vivienda3 = Vivienda(
    "San Martin", 789, "B", 1, 180.0,
    [Habitacion("Living", 35.0), Habitacion("Cocina", 15.0), Habitacion("Dormitorio", 30.0)])


barrio.viviendas.extend([vivienda1, vivienda2, vivienda3])

print("Superficie total de terreno del barrio:", barrio.getSuperficieTotalTerreno())
print("Superficie total de terreno de la manzana 'A':", barrio.getSuperficieTotalTerrenoXManzana("A"))
print("Superficie total de terreno de la manzana 'B':", barrio.getSuperficieTotalTerrenoXManzana("B"))
print("Superficie total cubierta del barrio:", barrio.getSuperficieTotalCubierta())
