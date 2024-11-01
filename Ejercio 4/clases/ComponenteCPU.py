class ComponenteCPU:
    def __init__(self, tipo, componente="", marca="", cantidad: int = 0, precio: float = 0.0):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.tipo = tipo
        if self.tipo == "PB":
            self.tipo = "Placa Base"
    
