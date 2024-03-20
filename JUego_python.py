import random

print("¡Bienvenido al juego de Piedra, Papel o Tijera!")

Y = int("¿Que elegiste?: ")

# processing

X = random.choice("piedra", "papel", "tijera")

if Y == X:
    print("Es un empate")
    print("Lo inetentamos otra vez")

elif (Y== "piedra" and X == "tijera") or \
     (Y== "papel" and X == "piedra") or \
     (Y== "tijera" and X == "papel"):
     print("Ganaste")
     print("¡Quiero la revancha!")

else: 
    print("Perdiste porque yo elegi" + str(X))