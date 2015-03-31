arquivo=open("entrada.txt", encoding="utf-8")       #sequencia que lê e limpa a lista
leitura=arquivo.readlines()
X=[]
for l in leitura:
    l2 =l.strip()
    if l2 !="":
        X.append(l2)
from random import choice      #define palavra escolhida da lista para o jogo

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Jogo da forca super hardcore")

lapis   = turtle.Turtle()  # Cria um objeto "desenhador"
turtle.setup (width = 1500)
lapis.width("8")
lapis.speed(20)  # define a velocidade

decisao = "Sim"

while decisao == "sim" or decisao == "Sim":
    escolha = choice(X).upper()
    l = list(escolha)
    Z = []
    for i in range(len(l)):
        if l[i] != ' ':
            Z.append(l[i])
    print(Z)
    print(len(Z))
    lapis.clear()
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
        lapis.forward(20)
        lapis.pendown()
    
    erros = 0
    acertos = 0
    
    lapis.penup()
    lapis.setpos(70,200)
    lapis.pendown()
    lapis.write("Palpites errados:", font = ("Arial", 20, "normal")) 
    lapis.penup()
    lapis.setpos(70,170)
    lapis.pendown()
    lapis.write("Número de erros:",font = ("Arial",20,"normal"))
    lapis.penup()
    lapis.setpos(70,140)
    lapis.pendown()
    lapis.write("Número de acertos:",font = ("Arial",20,"normal"))
    lapis.color("white")
    
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
            lapis.color("white")
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
            lapis.color("white")
    
    def desenhar_letra():
        for i in range(len(escolha)):
            if letra == escolha[i]:
                lapis.penup()
                lapis.setpos((-490+(i*50)),-250)
                lapis.pendown()
                lapis.write(letra , font = ('Arial',20,'normal'))
            if letra == "A" and escolha[i] == "Ã" or escolha[i]=="Â" :
                lapis.penup()
                lapis.setpos((-490+(i*50)),-250)
                lapis.pendown()
                lapis.write(escolha[i] , font = ('Arial',20,'normal'))
            if letra == "E" and escolha[i] == 'É' or escolha[i]=='Ê':
                lapis.penup()
                lapis.setpos((-490+(i*50)),-250)
                lapis.pendown()
                lapis.write(escolha[i] , font = ('Arial',20,'normal'))
            if letra == 'O' and escolha[i] == 'Ó' or escolha[i]=='Ô':
                lapis.penup()
                lapis.setpos((-490+(i*50)),-250)
                lapis.pendown()
                lapis.write(escolha[i] , font = ('Arial',20,'normal'))
            if letra == 'I' and escolha[i] == 'Í':
                lapis.penup()
                lapis.setpos((-490+(i*50)),-250)
                lapis.pendown()
                lapis.write(escolha[i] , font = ('Arial',20,'normal'))
                
                
               
    import tkinter 
        
    letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")
    letra = letra.upper()
    
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    x=300
    score = 0
    
    while erros < 6 or score < len(Z):
        n = escolha.count(letra)
        if n!=0 :
              n2=escolha.count(letra)  
              desenhar_letra()
              letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")
              letra = letra.upper()
              score += n2
        if n==0 :
            if len(letra) > 1 or letra not in alfabeto:
                tkinter.messagebox.showerror("INVALIDO", "LETRA INVALIDA")
                letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")
                letra = letra.upper()
            else:
                erros+=1
                lapis.penup()
                lapis.setpos(x,170)
                lapis.pendown()
                lapis.write(erros, font = ("Arial",20,"normal"))
                desenha_boneco()
                lapis.penup()
                lapis.setpos(x,200)
                lapis.pendown()
                lapis.write(letra, font = ("Arial",20,"normal"))
                x += 30
                letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")
                letra = letra.upper()
        if erros == 6 or score == len(Z):
            decisao = window.textinput("RESTART", "Deseja jogar novamente?(sim ou não?)")
            if decisao == "nao" or decisao == "Nao" or decisao == "Não" or decisao == "não":
                lapis.clear()
                lapis.penup()
                lapis.setpos(-550,0)
                lapis.pendown()
                lapis.color("white")
                lapis.write("OBRIGADO POR JOGAR!", font = ("Arial", 70 , "normal"))
                window.exitonclick()
                break
            if decisao=='sim' or decisao=='Sim':
                break
            
                
                
                
window.exitonclick()
    
                        
                
                