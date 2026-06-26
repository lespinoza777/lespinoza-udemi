import random

jugador = input("Piedra, papel o tijera: ")

opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

print("Computadora:", computadora)

if jugador == computadora:
    print("Empate")
else:
    print("La partida continúa...") 