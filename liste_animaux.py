#!/usr/bin/env python3
# Fichier : liste_animaux
# Aurélie Berhault
# 27 Mars 2020

#création et affichage de la liste
liste_a=["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
for i in liste_a:
    print(i)

#  liste inversée
liste_a=["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
liste_a.reverse()
for i in liste_a:
    print(i)

# affiche la liste triée
liste_a=["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
liste_a.sort()
for i in liste_a:
    print(i)

# ajout de "troll" dans la liste
liste_a=["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
liste_a.append("troll")
for i in liste_a:
    print(i)

# On supprime les animaux domestiques
liste_a=["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
liste_b=["chat", "chien", "chiot"]
for x in liste_b:
    liste_a.remove(x)
print(liste_a)

