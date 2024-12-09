from Alumno import Alumno

alumno = Alumno("Francisco", "Alia Hernandez", 32,"00100000R")


print(alumno.esMayorEdad())

alumno.apellidos = "Alias"
alumno.devolverTodo()
print(alumno.__str__())
alumno.__dni = "000000R"

alumno.devolverTodo()

