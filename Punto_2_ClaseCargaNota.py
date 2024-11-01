from Punto_2_ClaseAlumno import Alumno
from Punto_2_ClaseNota import Nota


class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def main(self):
        self.cargar_alumnos()
        self.mostrar_informacion()

    def cargar_alumnos(self):
        nAlumnos = int(input("Ingrese la cantidad de alumnos: "))
        for _ in range(nAlumnos):
            nombre = input("Ingrese el nombre completo del alumno: ")
            legajo = int(input("Ingrese el legajo: "))
            alumno = Alumno(nombre, legajo)
            self.cargar_notas(alumno)
            self.alumnos.append(alumno)

    def cargar_notas(self, alumno):
        nNotas = int(input("Ingrese la cantidad de notas: "))
        if nNotas < 0:
            print("Debe ingresar al menos una nota")
            self.cargar_notas(alumno)
            return
        for _ in range(nNotas):
            catedra = input("Ingrese la catedra: ")
            notaExamen = float(
                input(f"Ingrese la nota del alumno {alumno.nombreCompleto}: ")
            )
            nota = Nota(catedra, notaExamen)
            alumno.cargar_notas(nota)

    def mostrar_informacion(self):

        for alumno in self.alumnos:
            print()
            print(f"Alumno: {alumno.nombreCompleto} / Legajo: {alumno.legajo}")
            for nota in alumno.notas:
                print(f"_Catedra: {nota.catedra} / Nota: {nota.notaExamen}")
                print()

            promedio = alumno.obtener_promedio()
            print(f"Promedio: {promedio:.2f}")
            print("---------------------------------")


if __name__ == "__main__":
    carga_notas = CargaNotas()
    carga_notas.main()
