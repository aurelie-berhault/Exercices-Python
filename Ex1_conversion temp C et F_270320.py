# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# Aurélie Berhault
# 27 mars 2020

# Exo 1 : Conversion d'une temperature Fahrenheit/Celsius
temp=input("Entrer la temperature : ") # on entre d'abord la temperature
temp=int(temp)
unite=input("Préciser l'unité en tapant la lettre c ou f ")  # on entre ensuite l'unite par la lettre f ou c
unite=str(unite)

if unite=="f" or unite=="F":
    tempC=(temp-32)*(5/9)
    print(str(temp)+"°F vaut "+str(tempC)+" en Celsius")
if unite=="c" or unite=="C":
    tempF=(temp*(9/5))+32
    print(str(temp)+"°C vaut "+str(tempF)+" en Fahrenheit")
