class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} ha arrancado.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_puertas(self):
        print(f"El coche tiene {self.puertas} puertas.")


mi_coche = Coche("Ford", "Fiesta", 4)
mi_coche.arrancar()
mi_coche.mostrar_puertas()