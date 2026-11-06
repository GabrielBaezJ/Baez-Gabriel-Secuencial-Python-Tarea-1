import time

def preparar_tarea(tarea, segundos):
    print(f"Preparando la tarea: {tarea}")
    time.sleep(segundos)
    print(f"Terminado: {tarea} ({segundos} segundos)")

inicio = time.perf_counter()

preparar_tarea("Hervir agua para el café", 3)
preparar_tarea("Tostar pan", 2)
preparar_tarea("Freír huevos", 3)

fin = time.perf_counter()
print(f"Tiempo total de preparación: {fin - inicio:.2f} segundos")