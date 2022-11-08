# arthur robin
# 2022-09-04
# Jeu_De_Devinette
import random


def initialisationdelapartie():
    # J'importe random et je mets le nombre d'essai a zero
    global chiffre1
    global chiffre2
    global nombreessai
    global demander
    global chiffrerandom
    nombreessai = 0
    # Je demande a 'utilisateur si il veut choisir ces chiffres ou non
    demander = input(
        'voulez vous choisir vos chiffres? (oui/non)'
        '\n Si vous ne mettez pas le bon resultat vos chiffres seront choisi automatiquement!')
    if demander == 'oui':
        # Si l'utilisateur veut choisir ses chiffres et lui demander quel sont les chiffres
        chiffre1 = int(input("Entrer le premier chiffre"))
        chiffre2 = int(input("Entrer le deuxieme chiffre"))
    else:
        # Si l'utiliseur ne repond pas a la premiere question ou mal je dit que le chiffre recherche est entre 0 et 100
        chiffre1 = 0
        chiffre2 = 100
        print('Le chiffre recherché est entre 0 et 100')
    # trouve un nombre entre les bornes misent en place aupravant
    chiffrerandom = random.randint(chiffre1, chiffre2)


def turn():
    global nombreessai
    global chiffrerentrer
    global chiffrerandom
    # choix de l'utilisateur
    chiffrerentrer = int(input("Trouver le nombre recherché\nQuel est votre réponse?"))
    if chiffrerentrer == chiffrerandom:
        # si le joueur reussi
        nombreessai = nombreessai + 1
        print("Bravo!\n", "Vous avez reussi en ", nombreessai, "essais")
        return True

    elif chiffrerentrer < chiffrerandom:
        # si le chiffre est trop petit
        print("Le chiffre est plus grand")
        nombreessai = nombreessai + 1
        return False
    elif chiffrerentrer > chiffrerandom:
        # si le chiffre est trop grand
        print("Le chiffre est plus petit")
        nombreessai += 1
        return False

def game():
    initialisationdelapartie()
    while not turn():
        continue


def recommencer():
    choix = input("Voulez vous jouer? (oui/non)")
    if choix == 'oui':
        return True
    elif choix == 'non':
        return False
def main():
    while recommencer():
        game()
main()
  
