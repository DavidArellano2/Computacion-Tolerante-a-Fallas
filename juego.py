import pickle
import random

# Función para guardar el estado del juego
def guardar_estado(estado, archivo):
    with open(archivo, 'wb') as archivo_estado:
        pickle.dump(estado, archivo_estado)

# Función para restaurar el estado del juego
def restaurar_estado(archivo):
    with open(archivo, 'rb') as archivo_estado:
        estado = pickle.load(archivo_estado)
    return estado

# Función para jugar el juego de adivinanza de números
def jugar_juego():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Bienvenido al juego de adivinanza de números!")
    print("Trata de adivinar el número secreto entre 1 y 100.")

    while True:
        try:
            intento = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    archivo_estado = 'estado_juego.pkl'

    try:
        # Intentar restaurar el estado del juego desde el archivo
        estado = restaurar_estado(archivo_estado)
        print("Estado del juego restaurado.")
    except (FileNotFoundError, EOFError):
        # Si el archivo no existe o hay un error al cargar, comenzar un nuevo juego
        estado = None
        print("No se pudo restaurar el estado del juego. Comenzando un nuevo juego.")

    if estado is None:
        # Si no hay un estado previo, iniciar un nuevo juego
        jugar_juego()
        estado = {
            'numero_secreto': random.randint(1, 100),
            'intentos': 0
        }
    else:
        # Si se restauró el estado, continuar el juego desde donde se quedó
        numero_secreto = estado['numero_secreto']
        intentos = estado['intentos']
        print(f"Continuando el juego con el número secreto anterior. Intentos: {intentos}")
        jugar_juego()

    # Guardar el estado del juego al finalizar
    estado['intentos'] += 1
    guardar_estado(estado, archivo_estado)
