import math

def calcular_raiz(num):
    if num < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(num)

try:
    numero = float(input("Introduce un número: "))
    print(f"La raíz cuadrada de {numero} es {calcular_raiz(numero)}")
except ValueError as e:
    print(f"Error: {e}")