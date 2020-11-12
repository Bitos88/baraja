import random

numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["o", "c", "e", "b"]

def creaBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)
    return baraja

def intercambio(a,b):
    aux = a
    a = b
    b = aux

def barajar(lista_de_naipes):
    for i in range(len(lista_de_naipes)):
        nueva_pos: random.randrange(len(lista_de_naipes))
        aux = lista_de_naipes[nueva_pos]
        lista_de_naipes[nueva_pos] = lista_de_naipes[i]
        lista_de_naipes[i] = aux