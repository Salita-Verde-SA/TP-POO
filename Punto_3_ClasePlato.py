class Plato:
    def __init__(
        self,
        nombreCompleto,
        precio,
        esBebida,
    ):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.listaIngredientes = []

    def cargar_lista_ingredientes(self, ingredientes):
        self.listaIngredientes.append(ingredientes)
