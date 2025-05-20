'''
write()
Escribe una cadena en el fichero. Si el fichero no existe, se crea. Si ya existe, se sobrescribe (si usas el modo "w").
'''
with open("nuevo_fichero.txt", "w") as f:
    f.write("Buenos días, a por el jueves.\n")


'''
writelines()
Escribe una lista de cadenas en el fichero.
'''
lineas = ["Primera línea\n", "Segunda línea\n", "Tercera línea\n"]

with open("nuevo_fichero.txt", "w") as f:
    f.writelines(lineas)

