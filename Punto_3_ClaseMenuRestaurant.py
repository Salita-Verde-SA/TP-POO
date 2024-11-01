from Punto_3_ClaseIngrediente import Ingredientes
from Punto_3_ClasePlato import Plato


class MenuRestaurant:
    def __init__(self):
        self.platosMenu = []

    def main(self):
        self.cargar_platos()
        self.mostrar_informacion()

    def cargar_platos(self):
        nPlatos = int(input("Ingrese la cantidad de platos a cargar: "))
        for _ in range(nPlatos):
            nombre = input("Ingrese el nombre del plato: ")
            precio = float(input("Ingrese el precio: "))
            esBebida = input("Es una bebida?: (1.SI / 2.NO)")
            while True:
                if esBebida == "1":
                    esBebida = True
                    break
                elif esBebida == "2":
                    esBebida = False
                    break
                else:
                    print("Ingrese una respuesta valida.")
            plato = Plato(nombre, precio, esBebida)
            if esBebida == False:
                self.cargar_ingredientes(plato)

            self.platosMenu.append(plato)

    def cargar_ingredientes(self, plato):
        nIngredientes = int(input("Ingrese la cantidad de ingredientes: "))
        if nIngredientes <= 0:
            print("Ingrese por lo menos un ingrediente.")
            self.cargar_ingredientes(plato)
            return
        for _ in range(nIngredientes):
            print(f"Plato: {plato.nombreCompleto}")
            if plato.esBebida == True:
                print("El plato es una bebida y no lleva ingredientes.")
            elif plato.esBebida == False:

                nombre = input("Ingrese el nombre del ingrediente: ")
                cantidad = float(input("Ingrese la cantidad: "))
                unidadDeMedida = input("Ingrese la unidad de medida: ")
                ingrediente = Ingredientes(nombre, cantidad, unidadDeMedida)
                plato.cargar_lista_ingredientes(ingrediente)

    def mostrar_informacion(self):
        print("-----------MENÚ-----------")
        for plato in self.platosMenu:
            print(f"Nombre: {plato.nombreCompleto}\nPrecio: ${plato.precio}")
            if plato.esBebida == True:
                print()
                print("-----------------------------------------")
            elif plato.esBebida == False:
                print("Ingredientes:")
                print(f"{'UNIDAD DE MEDIDA':<15}   {'CANTIDAD':<15}   NOMBRE ")
                for ingrediente in plato.listaIngredientes:

                    print(f"{ingrediente.unidadDeMedida:<15}    {ingrediente.cantidad:<15}   {ingrediente.nombre}"
                    )
                print()
                print("-----------------------------------------")


if __name__ == "__main__":
    menu = MenuRestaurant()
    menu.main()
