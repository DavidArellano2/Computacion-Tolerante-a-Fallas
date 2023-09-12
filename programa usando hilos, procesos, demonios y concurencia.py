import tkinter as tk
from tkinter import ttk
import threading
import multiprocessing
import concurrent.futures

def tarea_larga_hilo():
    for i in range(5):
        print(f"Tarea en hilo - Iteración {i + 1}")
        time.sleep(0.5)

def tarea_larga_proceso():
    for i in range(5):
        print(f"Tarea en proceso - Iteración {i + 1}")
        time.sleep(0.5)

def iniciar_hilo():
    hilo = threading.Thread(target=tarea_larga_hilo)
    hilo.start()

def iniciar_proceso():
    proceso = multiprocessing.Process(target=tarea_larga_proceso)
    proceso.start()

def iniciar_concurrencia():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(tarea_larga_hilo)
        # Puedes agregar más tareas concurrentes aquí si lo deseas

app = tk.Tk()
app.title("Ejemplo de Hilos, Procesos y Concurrencia con GUI")

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10)

label = ttk.Label(frame, text="Presiona los botones para iniciar tareas:")
label.grid(column=0, row=0, padx=10, pady=10)

button_hilo = ttk.Button(frame, text="Iniciar Tarea en Hilo", command=iniciar_hilo)
button_hilo.grid(column=0, row=1, padx=10, pady=10)

button_proceso = ttk.Button(frame, text="Iniciar Tarea en Proceso", command=iniciar_proceso)
button_proceso.grid(column=0, row=2, padx=10, pady=10)

button_concurrencia = ttk.Button(frame, text="Iniciar Tarea con Concurrencia", command=iniciar_concurrencia)
button_concurrencia.grid(column=0, row=3, padx=10, pady=10)

app.mainloop()
