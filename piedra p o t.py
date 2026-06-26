import random

# Lista de opciones
opciones = ["piedra", "papel", "tijera"]

# Variables para el marcador
jugador_puntos = 0
computadora_puntos = 0

# Variable para controlar el juego
jugar = "si"

print("=== PIEDRA, PAPEL O TIJERA ===")

while jugar == "si":

    # El jugador elige una opción
    jugador = input("\nEscribe piedra, papel o tijera: ").lower()

    # Revisar que la opción exista
    if jugador not in opciones:
        print("Opción incorrecta.")
        continue

    # La computadora elige una opción al azar
    computadora = random.choice(opciones)

    print("Jugador:", jugador)
    print("Computadora:", computadora)

    # Comparar resultados
    if jugador == computadora:

        print("Empate")

    elif jugador == "piedra" and computadora == "tijera":

        print("Ganaste")
        jugador_puntos = jugador_puntos + 1

    elif jugador == "papel" and computadora == "piedra":

        print("Ganaste")
        jugador_puntos = jugador_puntos + 1

    elif jugador == "tijera" and computadora == "papel":

        print("Ganaste")
        jugador_puntos = jugador_puntos + 1

    else:

        print("Gana la computadora")
        computadora_puntos = computadora_puntos + 1

    # Mostrar marcador
    print("\nMarcador")
    print("Jugador:", jugador_puntos)
    print("Computadora:", computadora_puntos)

    # Preguntar si desea seguir jugando
    jugar = input("\n¿Desea jugar otra vez? (si/no): ").lower()

# Resultado final
print("\nJuego terminado")
print("Puntos del jugador:", jugador_puntos)
print("Puntos de la computadora:", computadora_puntos)

if jugador_puntos > computadora_puntos:
    print("Ganaste la partida.")

elif computadora_puntos > jugador_puntos:
    print("La computadora ganó la partida.")

else:
    print("La partida terminó en empate.")