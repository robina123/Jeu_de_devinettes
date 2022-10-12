# arthur robin
# 2022-09-04
# Jeu_De_Devinette_2.0
import random


nombreEssai = 0
chiffre1 = int(input("Entrer le premier chiffre"))
chiffre2 = int(input("Entrer le deuxieme chiffre"))
chiffreRandom = random.randint(chiffre1, chiffre2)
def Jeu_de_devinette():
    global nombreEssai
    fin = True
    while fin:

        # choix de l'utilisateur
        chiffreRentrer = int(input("Trouver le nombre recherché"))
        if chiffreRentrer == chiffreRandom:
            # si le joueur reussi
            nombreEssai = nombreEssai + 1
            print("Bravo!\n", "Vous avez reussi en ", nombreEssai, "essais")
            fin = False
        elif chiffreRentrer < chiffreRandom:
            # si le chiffre est trop petitimport random
            print("Le chiffre est plus grand")
            nombreEssai = nombreEssai + 1
        elif chiffreRentrer > chiffreRandom:
            # si le chiffre est trop grand
            print("Le chiffre est plus petit")
            nombreEssai = nombreEssai + 1

Jeu_de_devinette()
