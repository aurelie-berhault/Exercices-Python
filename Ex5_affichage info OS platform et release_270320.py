# Exo 5 : Affiche les informations OS, plateforme et release

# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# Aurélie Berhault
# 27 mars 2020

import os
import platform
print("Le nom du systeme d'exploitation est "+str(os.name))
print("Plateforme : "+str(platform.system()))
print("Version : "+str(platform.release()))
