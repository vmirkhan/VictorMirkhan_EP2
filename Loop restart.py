import unicodedata

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


import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Jogo da forca super hardcore")

lapis   = turtle.Turtle()  # Cria um objeto "desenhador"
turtle.setup (width = 1500)
lapis.width("8")
lapis.speed(5)  # define a velocidade

decisao = "Sim"

while decisao == "sim" or decisao == "Sim":
    lapis.penup()       
    lapis.setpos(700,-300)
    lapis.pendown()
    lapis.color("red")
    for i in range(1):
        lapis.left(90)  # Vira o angulo pedido
        lapis.forward(600)# Avança a distancia pedida
        lapis.left(90)
        lapis.forward(1000)
    for i in range(1):
        lapis.left(90)
        lapis.forward(100)
        
    lapis.penup()
    lapis.setpos(-500,-250)
    lapis.pendown()
    lapis.left(90)
    lapis.color("yellow")
    
    for i in escolha:
        if i !=" ":
            lapis.forward(30)
        else:
            lapis.penup()
            lapis.forward(40)
            lapis.pendown()
        lapis.penup()
        lapis.forward(18)
        lapis.pendown()
            
    erros = 0              #estabelece erros iniciais como 0
    lapis.width(5)
    
    def desenha_boneco():                     #funçaõ completa do desenho do boneco
        if erros == 1:
            lapis.color("white")
            lapis.penup()
            lapis.setpos(-300,140)
            lapis.pendown()
            lapis.circle(30)
        if erros == 2:
            lapis.penup()
            lapis.setpos(-300, 140)
            lapis.pendown()
            lapis.right(90)
            lapis.forward(70)
        if erros == 3:
            lapis.penup()
            lapis.setpos(-300,70)
            lapis.pendown()
            lapis.right(30)
            lapis.forward(50)
        if erros == 4:
            lapis.penup()
            lapis.setpos(-300,70)
            lapis.pendown()
            lapis.left(60)
            lapis.forward(50)
        if erros == 5:
            lapis.penup()
            lapis.setpos(-300,120)
            lapis.pendown()
            lapis.right(70)
            lapis.forward(35)
            lapis.penup()
            lapis.color("green")
            lapis.setpos(-330,95)
            lapis.pendown()
            lapis.circle(5)
        if erros == 6:
            lapis.penup()
            lapis.setpos(-300,120)
            lapis.pendown()
            lapis.color("white")
            lapis.left(80)
            lapis.forward(35)
            lapis.penup()
            lapis.setpos(-280,87)
            lapis.pendown()
            lapis.color("green")
            lapis.circle(5)
            lapis.penup()
            lapis.color("red")
            lapis.setpos(-310,180)
            lapis.pendown()
            lapis.right(70)
            lapis.forward(15)
            lapis.penup()
            lapis.setpos(-320,180)
            lapis.pendown()
            lapis.left(70)
            lapis.forward(17)
            lapis.penup()
            lapis.setpos(-285,180)
            lapis.pendown()
            lapis.right(70)
            lapis.forward(15)
            lapis.penup()
            lapis.setpos(-295,180)
            lapis.pendown()
            lapis.left(70)
            lapis.forward(17)
            lapis.penup()
            lapis.setpos(-650, 150)
            lapis.pendown()
            lapis.color("pink")
            lapis.write("""PERDEDOR!""", font = ("Arial",30 , "normal"))
    
    
    letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:").upper()
    x=300
    
    while True:
         if letra not in escolha:
             while erros in range(0,6):
                erros+=1
                desenha_boneco()
                lapis.penup()
                lapis.setpos(x,200)
                lapis.pendown()
                lapis.write(letra, font = ("Arial",20,"normal"))
                x+=30
                letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")  
             if erros == 6:
                decisao = window.textinput("RESTART", "Deseja jogar novamente?")
                if decisao == "nao" or decisao == "Nao" or decisao == "Não" or decisao == "não":
                    lapis.clear()
                    lapis.penup()
                    lapis.setpos(-550,0)
                    lapis.pendown()
                    lapis.color("white")
                    lapis.write("OBRIGADO POR JOGAR!", font = ("Arial", 70 , "normal"))
                    break
                if decisao == "sim":
                    lapis.clear()
                    lapis.reset()
                    lapis.width(8)
                    lapis.speed(5)
                    break
                
                            
                
                        
            
window.exitonclick()