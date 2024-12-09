#Declaro las listas
tareas_pendientes = []
tareas_completadas = []
def agregar_tarea(tarea):
    if tarea in tareas_pendientes:
        print(f"La tarea '{tarea}' ya está en la lista.")
    else:
        tareas_pendientes.append(tarea)
        print(f"Tarea '{tarea}' agregada.")
def eliminar_tarea(tarea):
    if tarea in tareas_pendientes:
        tareas_pendientes.remove(tarea)
        print(f"La tarea '{tarea}' ha sido eliminada.")
    else:
        print(f"La tarea '{tarea}' no está")

def mostrar_tareas_pendientes():
    if not tareas_pendientes:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for tarea in tareas_pendientes:
            print(f"- {tarea}")

def completar_tarea(tarea):
    if tarea in tareas_pendientes:
        tareas_pendientes.remove(tarea)
        tareas_completadas.append(tarea)
        print(f"Tarea '{tarea}' completada.")
    else:
        print(f"La tarea '{tarea}' no se encuentra en la lista.")

def mostrar_tareas_completadas():
    if not tareas_completadas:
        print("No hay tareas completadas.")
    else:
        print("Tareas completadas:")
        for tarea in tareas_completadas:
            print(f"- {tarea}")

while True:
    print("\nGestor de Tareas:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Marcar tarea como completada")
    print("5. Mostrar tareas completadas")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Introduce el nombre de la tarea: ")
        agregar_tarea(tarea)

    elif opcion == "2":
        tarea = input("Introduce el nombre de la tarea a eliminar: ")
        eliminar_tarea(tarea)

    elif opcion == "3":
        mostrar_tareas_pendientes()

    elif opcion == "4":
        tarea = input("Introduce el nombre de la tarea a completar: ")
        completar_tarea(tarea)

    elif opcion == "5":
        mostrar_tareas_completadas()

    elif opcion == "6":
        print("Saliendo del gestor de tareas.")
        break

    else:
        print("Opción no válida, por favor intenta de nuevo.")