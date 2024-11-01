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
                ram = comp.ComponenteCPU("RAM", componente, marca, cantidad, precio)
                self.componentes.append(ram)
            case "CPU":
                cpu = comp.ComponenteCPU("CPU", componente, marca, cantidad, precio)
                self.componentes.append(cpu)
            case "PB":
                pb = comp.ComponenteCPU("PB", componente, marca, cantidad, precio)
                self.componentes.append(pb)

    def mostrarComputadora(self):
        print("-- Computadora --")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print("Componentes: \n")

        precioTotal = 0
        for i in self.componentes:
            precioTotal += i.precio * i.cantidad
        print(f"Precio total: {precioTotal}")

        print(
            f"{'Componente':<15} {'Marca':<15} {'Cantidad':<15} {'Precio':<15} {'Precio':<15}"
        )
        for i in self.componentes:
            print(
                f"{i.tipo:<15} {i.marca:<15} {i.cantidad:<15} ${i.precio:<15}${i.precio*i.cantidad:<15}"
            )
        print(f"\n{'Precio Total: ':>62}  ${precioTotal}")
        ganancia = precioTotal * 0.4 if precioTotal < 50000 else precioTotal * 0.3
        precioSugerido = precioTotal + ganancia
        print(
            f"\nEl precio sugerido de venta es {precioTotal} + {ganancia} = {precioSugerido}"
        )
