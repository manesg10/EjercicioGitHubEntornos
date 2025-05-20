lineas = ["Primera linea", "Segunda linea", "Tercera linea\n"]

with open("nuevo_fichero.txt", "w") as f:
    f.writelines(lineas)



with open("nuevo_fichero.txt", "a") as f:
    f.write("ffffffffffffffffff.\n")