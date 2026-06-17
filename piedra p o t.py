import random

def obtener_jugada_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(jugador, cpu):
    if jugador == cpu:
        return "empate"

    if (
        (jugador == "piedra" and cpu == "tijera") or
        (jugador == "papel" and cpu == "piedra") or
        (jugador == "tijera" and cpu == "papel")
    ):
        return "jugador"

    return "cpu"

def jugar():
    puntos_jugador = 0
    puntos_cpu = 0

    while True:
        jugador = input("Piedra, papel o tijera: ").lower()

        if jugador not in ["piedra", "papel", "tijera"]:
            print("Opción inválida")
            continue

        cpu = obtener_jugada_computadora()

        print("Computadora:", cpu)

        resultado = determinar_ganador(jugador, cpu)

        if resultado == "jugador":
            puntos_jugador += 1
            print("Ganaste")
        elif resultado == "cpu":
            puntos_cpu += 1
            print("Perdiste")
        else:
            print("Empate")

        print(f"Marcador: {puntos_jugador} - {puntos_cpu}")

        continuar = input("¿Jugar otra vez? (s/n): ").lower()

        if continuar != "s":
            break

jugar()