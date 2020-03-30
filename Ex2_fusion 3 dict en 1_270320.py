# Exo 2 : Fusionne 3 dictionnaires en un seul

# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# Aurélie Berhault
# 27 mars 2020

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)