from Punto_2_ClaseAlumno import Alumno
from Punto_2_ClaseNota import Nota


class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def main(self):
        self.cargar_alumnos()
        self.mostrar_informacion()

    def cargar_alumnos(self):
        while True:
            
                
            nombre = input("Ingrese el nombre completo del alumno: ")
            legajo = int(input("Ingrese el legajo: "))
            alumno = Alumno(nombre, legajo)
            self.cargar_notas(alumno)
            self.alumnos.append(alumno)
            respuesta=input("Deseas cargar mas alumnos? (1.SI / 2.NO): ")
            if respuesta=="2":
                break
        
        
                
                
       

    def cargar_notas(self, alumno):
        while True:
            
            catedra = input("Ingrese la catedra: ")
            notaExamen = float(input(f"Ingrese la nota del alumno {alumno.nombreCompleto}: "))
            nota = Nota(catedra, notaExamen)
            alumno.cargar_notas(nota)
            respuesta=input("Deseas cargar mas notas? (1.SI / 2.NO): ")
            if respuesta=="2":
                break

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
