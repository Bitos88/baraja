import random

numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["o", "c", "e", "b"]

def creaBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)
    return baraja

def barajar():
    baraja = creaBaraja()
    for i in range(40):
        if baraja[i] != baraja[i]:
            baraja = baraja.append(baraja[i])
        else:
            pass
    return baraja


prueba = barajar()
print(prueba)


'''        
    baraja = random.choices(baraja, k=40)

    return baraja


cartasBarajadas = barajar(creaBaraja)
print(cartasBarajadas)

    

cartasMovidas = barajar(creaBaraja)

print(cartasMovidas)'''



'''
def creaJugador():
    newPlayers = []
    for i in range(3):
        newPlayers.append("NewPlayer" + str(i))
    return newPlayers


jugadores = creaJugador()
baraja = creaBaraja()

print("El jugador {} tiene la carta: {}".format(random.choice(jugadores), random.choice(baraja)))'''