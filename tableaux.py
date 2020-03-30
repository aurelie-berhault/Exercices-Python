# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# Aurélie Berhault
# 26 mars 2020

# Exemple 1 : Recherche séquentielle dans une liste non triée
import random
tableau_jeu=[]

# Initialisation d'une liste de 10 éléments
for i in range (0,10):
    tableau_jeu.append(random.randint (1,10))

# vérification de la saisie
joueur=0
while joueur<=0 or joueur>10:
    joueur=input("Entrer un nombre compris entre 0 et 9 : ")
    try:
        joueur=int(joueur)
    except TypeError:
        print("Vous n'avez pas saisi le bon format")
        continue
        joueur=0
    except ValueError:
        print("Vous n'avez pas saisi le bon nombre")
        continue
        joueur=0
    if joueur<0 or joueur>10:
        print("Vous devez saisir un nombre compris entre 0 et 9")

i=0
while i<len(tableau_jeu):
    if joueur==i:
        print("Gagné")
        i+=1
    else:
        print("Perdu")
        break


# Exemple 2 : Recherche séquentielle dans une liste triée
import random
tableau_jeu=[]

# Initialisation d'une liste de 10 éléments
for i in range (0,10):
    tableau_jeu.append(random.randint (1,10))
    tableau_jeu.sort()

joueur=0
while joueur<=0 or joueur>10:
    joueur=input("Entrer un nombre compris entre 0 et 9 : ")
    try:
        joueur=int(joueur)
    except TypeError:
        print("Vous n'avez pas saisi le bon format")
        continue
        joueur=0
    except ValueError:
        print("Vous n'avez pas saisi le bon nombre")
        continue
        joueur=0
    if joueur<0 or joueur>10:
        print("Vous devez saisir un nombre compris entre 0 et 9")

print("Le numéro tiré est le numéro "+str(tableau_jeu[i])+" et vous avez choisi le numéro "+str(joueur))

i=0
while i<len(tableau_jeu):
    if joueur==i:
        print("Gagné")
        i+=1
        break
    elif i>joueur:
        print("Perdu")
        i+=1
        break
    else:
        print("Perdu")
        break

