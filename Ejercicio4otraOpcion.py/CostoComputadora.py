from ComponentesCPU import ComponentesCPU
from Computadora import Computadora
marca=input("Ingrese la marca de la computadora: ")
modelo=input("Ingrese el modelo de la computadora: ")
computadora=Computadora(marca,modelo)

while True:
    nombre=input("Ingrese el nombre del componente: ")
    marca=input("Ingrese la marca del componente: ")
    cantidad=int(input("Ingrese la cantidad: "))
    precio=float(input("Ingrese el precio: "))
    componentes=ComponentesCPU(nombre,marca,cantidad,precio)
    computadora.cargar_componentes(componentes)
    respuesta=input("Desea seguir cargando componentes? (1.SI / 2.NO): ")
    if respuesta=="2":
        break
suma_precios=computadora.sumar_precios()

#Impresion
computadora.mostrar_informacion()

    

