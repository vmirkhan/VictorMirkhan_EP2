def remover_acentos(str):                          #função que remove acentos das palavras
    palavra = l2
    print(palavra.encode("utf-8"))
    palavra = unicodedata.normalize("NFKD", palavra)
    palavra_sem_acento = palavra.encode("ascii", "ignore")
    palavra_sem_acento = u"".join([ch for ch in palavra if not unicodedata.combining(ch)])
    return palavra_sem_acento
arquivo=open("entrada.txt", encoding="utf-8")       #sequencia que lê e limpa a lista
leitura=arquivo.readlines()
X=[]
for l in leitura:
    l2 =l.strip()
    if l2 !="":
        l3 = remover_acentos(l2)
    X.append(l3)
from random import choice
escolha = choice(X).upper()      #define palavra escolhida da lista para o jogo
print(escolha)        
print(len(escolha))