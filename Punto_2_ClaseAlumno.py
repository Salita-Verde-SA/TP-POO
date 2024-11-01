class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def cargar_notas(self, nota):
        self.notas.append(nota)

    def obtener_promedio(self):
        suma = sum(nota.notaExamen for nota in self.notas)
        promedio = suma / len(self.notas)
        return promedio
