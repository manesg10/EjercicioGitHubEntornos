'''
Abrir un fichero
La función open() se utiliza para abrir un fichero en Python. Tiene dos parámetros importantes:
    El nombre del fichero que quieres abrir.
    El modo en que quieres abrir el fichero (lectura, escritura, etc.).
    f = open("nombre_fichero.txt", "modo")

    Los modos más comunes son:
        "r": Leer. El fichero debe existir.
        "w": Escribir. Si el fichero no existe, se crea; si existe, se sobrescribe.
        "a": Añadir. Escribe al final del fichero sin sobrescribir el contenido existente.
        "r+": Leer y escribir.
'''


'''
readline()
Lee una línea del fichero a la vez.
'''

with open("variasLineas.txt", "r") as f:
    print('LEER TODO')
    lineas = f.readlines()
    for linea in lineas:
        print(linea, "\n")
