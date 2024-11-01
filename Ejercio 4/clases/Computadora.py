from . import ComponenteCPU as comp


class Computadora:

    def __init__(self, marca: str, modelo: str):
        self.componentes: list = []
        self.modelo: str = modelo
        self.marca: str = marca
        print("Computadora creada")

    def cargarComponente(self, tipo, componente, marca, cantidad: int, precio: float):
        match tipo:
            case "RAM":
                ram = comp.ComponenteCPU(componente, marca, cantidad, precio)
                self.componentes.append(ram)
            case "CPU":
                cpu = comp.ComponenteCPU(componente, marca, cantidad, precio)
                self.componentes.append(cpu)
            case "PB":
                pb = comp.ComponenteCPU(componente, marca, cantidad, precio)
                self.componentes.append(pb)
    def mostrarComputadora(self):
        print("-- Computadora --")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes: \n")

        for i in self.componentes:
            print(i.marca)