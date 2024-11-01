class Matriz:
    def __init__(self):

        self.celdasMatriz = []

    def verificar_repeticion(self, fila, columna, valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    def agregar_celda(self, celda):
        self.celdasMatriz.append(celda)

    def mostrar_celda(self):
        i = 1
        for celda in self.celdasMatriz:
            print(
                f"Celda {i} (Fila: {celda.fila} / Columna: {celda.columna} / Valor: {celda.valor})"
            )
            print("----------------------------------------")
            i += 1

    def devolver_valor_celda(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        print("La fila y columna indicada no ha sido asignada en ninguna celda")
        return False
