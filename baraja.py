numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["o", "c", "e", "b"]

def creaBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)
    return baraja


def creaJugador():
    newPlayers = []
    for i in range(3):
        newPlayers.append("NewPlayer" + str(i))
    return newPlayers


jugadores = creaJugador()
print(jugadores)

