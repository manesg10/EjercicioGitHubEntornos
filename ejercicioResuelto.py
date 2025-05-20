'''Empieza a hacerlo aquí'''

import os

try:
    os.mkdir("insertmasivos")
except FileExistsError:
    print("El fichero ya existe")
except:
    print("Otra cosa")

try:
    with open("usuarios.txt","r") as f:
        linea=f.readline()
        with open("insertmasivos/insertUsuarios.txt", "w") as fw:
            while linea:
                fw.write(("INSERT INTO USUARIOS (NOMBRE,APELLIDO,EDAD,CIUDAD,CALLE,CP,NUMERO,MOVIL) VALUES ("+linea.removesuffix("\n"))+"\n")
                linea=f.readline()
except FileNotFoundError:
    print("Fichero no encontrado")