from Punto_1_ClaseCelda import Celda
from Punto_1_ClaseMatriz import Matriz

matriz1 = Matriz()
while True:
    fila = int(input("Ingrese el valor de la fila: "))
    columna = int(input("Ingrese el valor de la columna: "))
    valor = input("Ingrese el valor de la celda: ")
    repeticion = matriz1.verificar_repeticion(fila, columna, valor)
    if repeticion:
        print(
            f"Celda ({fila},{columna})\nEsta celda ya esta cargada. Ingrese una nueva"
        )

    else:
        nueva_celda = Celda(fila, columna, valor)
        matriz1.agregar_celda(nueva_celda)
        respuesta = input("Desea continuar?: (1.SI / 2.NO)")
        if respuesta == "2":
            break
        elif respuesta != "1":
            print("Ingrese una respuesta valida")

print()
print("Valores cargados en la lista celdas:")
matriz1.mostrar_celda()
print("<<<PEDIR CELDA>>>")
print("Ingrese la posicion de la celda")
fila = int(input("Fila: "))
columna = int(input("Columna: "))
valor_celda = matriz1.devolver_valor_celda(fila, columna)
if valor_celda != False:
    print(f"El valor de la celda ({fila},{columna}) es {valor_celda}")
