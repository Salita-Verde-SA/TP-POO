from . import Computadora
from . import ComponenteCPU as comp


class CostoComputadora:
    def main():
        compu = Computadora.Computadora(modelo="IdeaPad 3", marca="Lenovo")
        print("<<<< Carga de componentes >>>>")

        compu.cargarComponente("RAM", "16 GB", "Kingston", 2, 23.2)
        compu.cargarComponente("CPU", "Ryzen 9", "AMD", 1, 23.2)
        compu.cargarComponente("PB", "A520M", "Asus", 1, 23.2)

        compu.mostrarComputadora()