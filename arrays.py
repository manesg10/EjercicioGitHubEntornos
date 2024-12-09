import numpy as np

mi_array = np.array([1, 2, 3, 4])
print(mi_array)
print(mi_array[0])
print(mi_array[-2])

print("longitud " + str(len(mi_array)))

mi_array[2] = 5

print(mi_array)

# Sumar 2 a cada elemento del array
mi_array = mi_array + 2

print(mi_array)

# Multiplicar cada elemento por 3
mi_array = mi_array * 3
print(mi_array)

# Obtener una porción del array (elementos del 2 al 4)
sub_array = mi_array[1:4]
print(sub_array)

'''
np.mean(array): Devuelve la media de los elementos.
np.max(array): Devuelve el valor máximo.
np.min(array): Devuelve el valor mínimo.
'''

mi_array[2] = 22
print(mi_array)
maximo = np.max(mi_array)
minimo = np.min(mi_array)
media = np.mean(mi_array)
maximo2 = mi_array.max()
print(mi_array)
print(f"{maximo}, {minimo}, {media}, {maximo2}")



'''
Ejercicios prácticos:
Crea un array de números enteros del 1 al 10 y multiplica cada elemento por 2.
Utilizando slicing, extrae una sublista que contenga los primeros 5 elementos.
Crea un array de números flotantes y calcula la media de sus valores. No está permitido utilizar el mean
'''
