def crear_tarea(titulo, descripcion):
    return {"titulo": titulo, "descripcion": descripcion, "completada": False}

def marcar_completada(tarea):
    tarea["completada"] = True
    return tarea

if __name__ == "__main__":
    tarea = crear_tarea("Ejemplo", "Primera tarea")
    print("Tarea creada:", tarea)

    tarea = marcar_completada(tarea)
    print("Tarea actualizada:", tarea)
