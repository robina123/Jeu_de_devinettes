# arthur robin
# 2022-09-04
# Jeu_De_Devinette_2.0

def Jeu_de_devinette():
    import random

    quit = False
    # programme principal

    #chiffreRandom = random.randint(0, 1000)
    # defenir les variables avant le programme
    nombreEssai = 0
    chiffre1 = int(input("Entrer le premier chiffre"))
    chiffre2 = int(input("Entrer le deuxieme chiffre"))
    demanderRecommencer = False
    partie = True
    # decider entre quel et quel chiffre le chiffre a deviner sera et choisir le chiffre que l'utilisateur doit trouver au hazard a partir de random


    chiffreRandom = random.randint(chiffre1,chiffre2)

        # choix de l'utilisateur

    chiffreRentrer = int(input("Trouver le nombre recherché"))
    if chiffreRentrer == chiffreRandom:
    # si le joueur reussi
    nombreEssai = nombreEssai + 1
    print("Bravo!\n", "Vous avez reussi en ", nombreEssai, "essais")
    chiffreTrouver = True
    demanderRecommencer = True
    elif chiffreRentrer < chiffreRandom:
    # si le chiffre est trop petit
    print("Le chiffre est plus grand")
    nombreEssai = nombreEssai + 1
    elif chiffreRentrer > chiffreRandom:
    # si le chiffre est trop grand
    print("Le chiffre est plus petit")
    nombreEssai = nombreEssai + 1

Jeu_de_devinette()

"""

def word_count(question):
    #
    return len(question.split())
# Demande a l'utilisateur quel est sa phrase.
question = input("Quel est votre phrase?")
#utilise la def pour compter le nombre de mots dans la phrase.
final = word_count(question)
print('Vous avez', final, 'mots')


"""
