# arthur robin
# 2022-09-04
# Jeu_De_Devinette
import random
def nombrerandom():
    #J'importe random et je mets le nombre d'essai a zero
global chiffre1
global chiffre2 
global nombreessai
global demander 
global chiffrerandom
nombreEssai = 0
#Je demande a 'utilisateur si il veut choisir ces chiffres ou non
demander = input('voulez vous choisir vos chiffres? (oui/non)\n Si vous ne mettez pas le bon resultat vos chiffres seront choisi automatiquement!')
if demander == 'oui':
#Si l'utilisateur veut choisir ses chiffres et lui demander quel sont les chiffres
    nombreessai = 0
    chiffre1 = int(input("Entrer le premier chiffre"))
    chiffre2 = int(input("Entrer le deuxieme chiffre"))
else:
# Si l'utiliseur ne repond pas a la premiere question ou mal je dit que le chiffre recherche est entre 0 et 100
    chiffre1 = 0
    chiffre2 = 100
    print('Le chiffre recherché est entre 0 et 100')
# trouve un nombre entre les bornes misent en place aupravant 
chiffrerandom = random.randint(chiffre1, chiffre2)


def essai():
    global nombreessai
    global chiffrerentrer
    global chiffrerandom
        # choix de l'utilisateur
        chiffrerentrer = int(input("Trouver le nombre recherché\nQuel est votre réponse?"))
        if chiffrerentrer == chiffreRandom:
            # si le joueur reussi
            nombreEssai = nombreEssai + 1
            print("Bravo!\n", "Vous avez reussi en ", nombreEssai, "essais")
          
        elif chiffrerentrer < chiffrerandom:
            # si le chiffre est trop petit
            print("Le chiffre est plus grand")
            nombreEssai = nombreEssai + 1
        elif chiffrerentrer > chiffrerandom:
            # si le chiffre est trop grand
            print("Le chiffre est plus petit")
            nombreessai = nombreessai + 1
        

def main():
    while != a
