

# arthur robin
# 2022-09-04
# Jeu_De_Devinette_2.0
#J'importe random et je mets le nombre d'essai a zero
import random
nombreEssai = 0
#Je demande a 'utilisateur si il veut choisir ces chiffres ou non
demander = input('voulez vous choisir vos chiffres? (oui/non)\n Si vous ne mettez pas le bon resultat vos chiffres seront choisi automatiquement!')

if demander == 'oui':
#Si l'utilisateur
    nombreEssai = 0
    chiffre1 = int(input("Entrer le premier chiffre"))
    chiffre2 = int(input("Entrer le deuxieme chiffre"))
else:
    chiffre1 = 0
    chiffre2 = 100
    print('Le chiffre recherché est entre 0 et 100')
chiffreRandom = random.randint(chiffre1, chiffre2)
def Jeu_de_devinette():
    global nombreEssai
    fin = True
    while fin:
        demanderRecommencer = False
        # choix de l'utilisateur
        chiffreRentrer = int(input("Trouver le nombre recherché\nQuel est votre réponse?"))
        if chiffreRentrer == chiffreRandom:
            # si le joueur reussi
            nombreEssai = nombreEssai + 1
            print("Bravo!\n", "Vous avez reussi en ", nombreEssai, "essais")
            demanderRecommencer = True
        elif chiffreRentrer < chiffreRandom:
            # si le chiffre est trop petitimport random
            print("Le chiffre est plus grand")
            nombreEssai = nombreEssai + 1
        elif chiffreRentrer > chiffreRandom:
            # si le chiffre est trop grand
            print("Le chiffre est plus petit")
            nombreEssai = nombreEssai + 1
        if demanderRecommencer == True:
            recommencer = input("voulez vous recommencez?")
            if recommencer == "non":
                print("Merci d'avoir joué")
                exit()
            elif recommencer == "oui":
                break

Jeu_de_devinette()


