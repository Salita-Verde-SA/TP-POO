class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0
        total = sum(nota.notaExamen for nota in self.notas)
        return total / len(self.notas)


class Nota:
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra
        self.notaExamen = notaExamen


class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def cargar_alumnos(self):
        n_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        for _ in range(n_alumnos):
            nombre = input("Ingrese el nombre completo del alumno: ")
            legajo = int(input("Ingrese el legajo del alumno: "))
            alumno = Alumno(nombre, legajo)
            self.cargar_notas(alumno)
            self.alumnos.append(alumno)

    def cargar_notas(self, alumno):
        n_notas = int(
            input(f"Ingrese la cantidad de notas para {alumno.nombreCompleto}: ")
        )
        if n_notas < 1:
            print("Debe ingresar al menos una nota.")
            self.cargar_notas(alumno)
            return
        for _ in range(n_notas):
            catedra = input("Ingrese la cátedra: ")
            notaExamen = float(input("Ingrese la nota del examen: "))
            nota = Nota(catedra, notaExamen)
            alumno.agregar_nota(nota)

    def mostrar_informacion(self):
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombreCompleto}, Legajo: {alumno.legajo}")
            for nota in alumno.notas:
                print(f"  Cátedra: {nota.catedra}, Nota: {nota.notaExamen}")
            promedio = alumno.calcular_promedio()
            print(f"  Promedio: {promedio:.2f}")

    def main(self):
        self.cargar_alumnos()
        self.mostrar_informacion()


if __name__ == "__main__":
    carga_notas = CargaNotas()
    carga_notas.main()
