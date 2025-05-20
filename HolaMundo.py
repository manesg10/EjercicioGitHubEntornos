class Evento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha


    def nombreEvento (self):
        return print(f"El nombre del evento es:{self.nombre}")


evento = Evento("nombreInventado","10/11/2024")
evento.nombreEvento()
print("hola")