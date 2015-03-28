# -*- coding: utf-8 -*-
arquivo=open("entrada.txt", encoding="utf-8")
leitura=arquivo.readlines()
X=[]
for l in leitura:
    l2 =l.strip()
    if l2!="":
        X.append(l2)
print(X)
from random import choice
escolha = choice(X).upper()
X.remove(escolha)
print(escolha)
