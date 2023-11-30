#!/bin/python3

import math
import time

print('-'*60+'TP:1'+'-'*60+"\n\n\n")

# Calcul d'entropie
# Initialisation des paramètres

while True:
    L = ("a", "b", "c", "d")  # Les symboles
    P = list()  # Probabilités
    I = list()  # Quantité d'information
    H = list()  # Entropie
    Px = 0

    # Test
    for i in range(4):
        P.append(float(input(f"Entrez la probabilité de {L[i]}: ")))
        while P[i] < 0 or P[i] > 1:
            P.pop(i)
            print("Erreur! La probabilité doit être positive et inférieure ou égale à 1\n")
            P.append(float(input("Entrer une probabilité valable: ")))
        Px += P[i]

    print('\n\n')

    while Px != 1:
        Px = 0
        P = list()
        print("Veuillez entrer des probabilités valables!!!!!(La somme doit être égale à 1)")
        for i in range(4):
            P.append(float(input(f"Entrez la probabilité de {L[i]}: ")))
            Px += P[i]
        print('\n\n')

    for i in range(4):
        if P[i] == 0:
            I.append(0)
        else:
            I.append(math.log2(1/P[i]))
        H.append(P[i]*I[i])

    # Somme
    Hx = 0
    for i in range(4):
        Hx += H[i]

    print("\n\n")
    # Affichage des résultats
    for i in range(4):
        print(f" +La quantité d'information dans {L[i]}: {I[i]} shanon\n")
    print(f"    ----> L'entropie est : {Hx} shannon/symbole\n\n")
    print("\n\n\n")

    char = input('Voulez-vous continuer ?: ')
    if char.lower() in ("no", "close"):
        print('*'*200)
        time.sleep(1)
        print("Fin du programme")
        time.sleep(1)
        print('*'*200)
        break

print('test if it works!!!!!!)
