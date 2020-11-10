numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["o", "c", "e", "b"]

baraja = []

def creaBaraja():

    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)
    return baraja

print(baraja)
