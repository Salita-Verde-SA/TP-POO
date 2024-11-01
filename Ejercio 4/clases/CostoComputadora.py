from . import Computadora
from . import ComponenteCPU as comp


class CostoComputadora:
    def main():
        while True:
            marca=input("Ingrese la marca de la computadora: ")
            modelo=input("Ingrese el modelo de la computadora: ")
            print("<<<< Carga de componentes >>>>")
            compu = Computadora.Computadora(marca, modelo)

            # CPU
            marcaCPU = input("Ingrese la marca de la CPU: ")
            cpu = input("Ingrese el modelo de la CPU: ")
            precioCPU = float(input("Ingrese el precio de la CPU: "))
            compu.cargarComponente("CPU", cpu, marcaCPU, 1, precioCPU)
            
            # RAM
            cantidadRAM = int(input("Ingrese la cantidad de memorias RAM: "))
            marcaRAM = input("Ingrese la marca de la RAM: ")
            ram = input("Ingrese la cantidad de RAM: ")
            precioRAM = float(input("Ingrese el precio de la RAM: "))
            compu.cargarComponente("RAM", ram, marcaRAM, cantidadRAM, precioRAM)

            # Placa Base
            marcaPB = input("Ingrese la marca de la Placa Base: ")
            pb = input("Ingrese el modelo de Placa Base: ")
            precioPB = float(input("Ingrese el precio de la Placa Base: "))
            compu.cargarComponente("PB", pb, marcaPB, 1, precioPB)

            compu.mostrarComputadora()

            seguir = input("Desea seguir? SI/NO ")
            seguir = seguir.lower()
            match seguir:
                case "si":
                    print("\nReiniciando...")
                case "no":
                    print("\nSaliendo...")
                    break
                case _:
                    print("Resupuesta invalida, saliendo...")