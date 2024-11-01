class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, fila, columna, valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                print("La celda ya existe en la matriz.")
                return
        nueva_celda = Celda(fila, columna, valor)
        self.celdasMatriz.append(nueva_celda)

    def obtener_valor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

    def mostrar_celdas(self):
        for celda in self.celdasMatriz:
            print(f"Fila: {celda.fila}, Columna: {celda.columna}, Valor: {celda.valor}")

def main():
    matriz = Matriz()

    while True:
        valor = input("Ingrese el valor para la celda (o 'FIN' para terminar): ")
        if valor == "FIN":
            break
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        matriz.agregar_celda(fila, columna, valor)

    print("\nValores cargados en la matriz:")
    matriz.mostrar_celdas()

    fila = int(input("\nIngrese la fila para buscar el valor: "))
    columna = int(input("Ingrese la columna para buscar el valor: "))
    valor_encontrado = matriz.obtener_valor(fila, columna)
    print(f"Valor en la celda ({fila}, {columna}): {valor_encontrado}")

if __name__ == "__main__":
    main()
