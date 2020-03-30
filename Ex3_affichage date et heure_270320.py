# Exo 3 : Affiche la date et l'heure actuelle

# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# Aurélie Berhault
# 27 mars 2020

import datetime
import time
x=datetime.datetime.now()
print("Nous sommes le "+str(x.date())+" et il est "+str(x.strftime("%H:%M:%S")))