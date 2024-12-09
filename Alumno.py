class Alumno(Persona):
    def __init__(self, nombre, apellidos, edad, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.__dni = dni

    def esMayorEdad(self):
        return self.edad >= 18

    def devolverTodo(self):
        return print(f"{self.nombre}, {self.apellidos}, {self.edad}, {self.__dni}")
