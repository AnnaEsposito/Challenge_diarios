
import random

logica_maquina = ["piedra", "papel", "tijera"]
max_turno = 5

def usuario():
    eleccion_usuario = input("Juguemos piedra, papel o tijera. Elige una opción: ")
    return eleccion_usuario

def maquina():
    eleccion_maquina = random.choice(logica_maquina)
    return eleccion_maquina

turno_maquina = True
turno = 0

while turno < max_turno:
    if turno_maquina:
        eleccion_maquina = maquina()
    else:
        eleccion_usuario = usuario()
        turno += 1
        
        # Comparamos las elecciones
        if eleccion_usuario == eleccion_maquina:
            print("Empate!")
        elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
            print("¡Ganaste!")
        else:
            print("Perdiste!")

    turno_maquina = not turno_maquina

