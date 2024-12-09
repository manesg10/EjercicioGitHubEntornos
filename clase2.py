class Alumno:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__edad = edad

    def esMayor(self):
        return self.__edad >= 18

    def sumarEdad(self,suma):
        self.__edad = self.__edad + suma


    def toString(self):
        print(f"{self.nombre}, {self.apellidos}, {self.__edad}")



alumno = Alumno("Francisco","Alia",32)
print(alumno.esMayor())
alumno.sumarEdad(1)
alumno.toString()
alumno.__edad = 30
alumno.toString()
