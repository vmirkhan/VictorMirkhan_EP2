arquivo=open("entrada.txt", encoding="utf-8")       #sequencia que lê e limpa a lista
leitura=arquivo.readlines()
X=[]
for l in leitura:
    l2 =l.strip()
    if l2 !="":
        X.append(l2)
from random import choice      #define palavra escolhida da lista para o jogo
import tkinter
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Jogo da forca super hardcore")

lapis   = turtle.Turtle()  # Cria um objeto "desenhador"
turtle.setup (width = 1500)
lapis.width("8")
lapis.speed(10)  # define a velocidade

decisao = "Sim"

while decisao == "sim" or decisao == "Sim":
    score = 0
    opção = window.textinput("Modo de jogo", "Escreva 'A' para jogar contra o cpu ou 'B' para escolher a palavra manualmente.")
    if opção == 'A' or opção == 'a':    
        escolha = choice(X)
        escolha = escolha.upper()
    if opção == 'B' or opção == 'b':
        escolha = window.textinput("Escolha manual", "Jogador 2, escolha uma palavra para o jogo!")
        escolha = escolha.upper()
    if opção != 'a' and opção!='A' and opção!='B' and opção!='b':
        tkinter.messagebox.showerror("INVÁLIDO", "Escolha novamente, por favor")
        opção = window.textinput("Modo de jogo", "Escreva 'A' para jogar contra o cpu ou 'B' para escolher a palavra manualmente.")
    
    
    l = list(escolha)
    Z = []
    for i in range(len(l)):
        if l[i] != ' ':
            Z.append(l[i])
    modo = window.textinput("DIFICULDADE", 'Clique 1 para modo fácil (10 erros), 2 para médio (7 erros) e 3 para díficil (4 erros)')
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
            lapis.forward(30)
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
    
    
    if modo == '1':
        lapis.penup()
        lapis.setpos(0,-100)
        lapis.pendown()
        lapis.color('pink')
        lapis.write("Modo Florzinha s2",font = ('Comic sans', 50 ,'normal' ))
        lapis.color('white')
        def desenha_boneco_1():                     #funçaõ completa do desenho do boneco
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
            if erros == 6:
                lapis.penup()
                lapis.color("green")
                lapis.setpos(-330,95)
                lapis.pendown()
                lapis.circle(5)
                lapis.color("white")
            if erros == 7:
                lapis.penup()
                lapis.setpos(-300,120)
                lapis.pendown()
                lapis.color("white")
                lapis.left(80)
                lapis.forward(35)
            if erros == 8:
                lapis.penup()
                lapis.setpos(-280,87)
                lapis.pendown()
                lapis.color("green")
                lapis.circle(5)
                lapis.color('white')
            if erros == 9:
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
                lapis.color('white')
            if erros == 10:
                lapis.color('red')
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
                
    if modo == '2':
        lapis.penup()
        lapis.setpos(-100,-100)
        lapis.pendown()
        lapis.color('orange')
        lapis.write("Modo café com leite :)",font = ('Comic sans', 50 ,'normal' ))
        lapis.color('white')
        def desenha_boneco_2():                     #funçaõ completa do desenho do boneco
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
            if erros == 7:
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
            
    if modo == '3':
        lapis.penup()
        lapis.setpos(-280,-100)
        lapis.pendown()
        lapis.color('dark red')
        lapis.write("MODO ULTRA HARDCORE >:(",font = ('Comic sans', 50 ,'normal' ))
        lapis.color('white')
        def desenha_boneco_3():                     #funçaõ completa do desenho do boneco
            if erros == 1:
                lapis.color("white")
                lapis.penup()
                lapis.setpos(-300,140)
                lapis.pendown()
                lapis.circle(30)
                lapis.penup()
                lapis.setpos(-300, 140)
                lapis.pendown()
                lapis.right(90)
                lapis.forward(70)
            if erros == 2:
                lapis.penup()
                lapis.setpos(-300,70)
                lapis.pendown()
                lapis.right(30)
                lapis.forward(50)
                lapis.penup()
                lapis.setpos(-300,70)
                lapis.pendown()
                lapis.left(60)
                lapis.forward(50)
            if erros == 3:
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
                lapis.color('white')
            if erros == 4:
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
       
    lista_chutes=[]
    
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
            if letra=='U' and escolha[i] == 'Ú':
                lapis.penup()
                lapis.setpos((-490+(i*50)),-250)
                lapis.pendown()
                lapis.write(escolha[i] , font = ('Arial',20,'normal'))
                
    import tkinter 
        
    letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")
    letra = letra.upper()
    chutes = []

    alfabeto = ['A','B','C','Ç','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    x=300
    y=310
    
    erro_max = 0
    
    if modo == "1":
        erro_max = 10
    if modo == "2":
        erro_max = 6
    if modo == '3':
        erro_max = 4
    
    def conta_variantes(escolha, letra):
        if letra in "AEIOU":
            if letra == 'A':
                return escolha.count(letra) + escolha.count("Ã") + escolha.count('Á') + escolha.count('Â')
            if letra == 'E':
                return escolha.count(letra) + escolha.count('É') + escolha.count('Ê')
            if letra == 'I':
                return escolha.count(letra) + escolha.count('Í')
            if letra == 'O':
                return escolha.count(letra) + escolha.count('Ó') + escolha.count('Ô')
            if letra == 'U':
                return escolha.count(letra) + escolha.count('Ú')
                
        else:
            return escolha.count(letra)
        
    
    while erros < erro_max or score < len(Z):
        n = conta_variantes(escolha,letra)
        if len(letra) > 1 or letra not in alfabeto or letra=='' or letra==' ' or letra=='  ' or letra==',' or letra=='.':
            tkinter.messagebox.showerror("INVALIDO", "LETRA INVALIDA")
        if n!=0 :
            if letra in chutes:
                tkinter.messagebox.showerror("INVALIDO", "LETRA INVALIDA")
            else:
                n1 = conta_variantes(escolha,letra)
                desenhar_letra()
                score += n1
                lapis.penup()
                lapis.setpos(y,140)
                lapis.pendown()
                lapis.write(score,font = ("Arial",20,'normal'))
                chutes.append(letra)
                y+=30
        if n==0 :
            if letra in chutes or letra not in alfabeto:
                tkinter.messagebox.showerror("INVALIDO", "LETRA INVALIDA")
            else:
                erros+=1
                lapis.penup()
                lapis.setpos(x,170)
                lapis.pendown()
                lapis.write(erros, font = ("Arial",20,"normal"))
                if modo == '1':
                    desenha_boneco_1()
                if modo == '2':
                    desenha_boneco_2()
                if modo == '3':
                    desenha_boneco_3()
                lapis.penup()
                lapis.setpos(x,200)
                lapis.pendown()
                lapis.write(letra, font = ("Arial",20,"normal"))
                x += 30
                chutes.append(letra)
                    
        if erros == erro_max or score == len(Z):
            if score >= len(Z):
                lapis.clear()
                lapis.penup()
                lapis.setpos(-550,0)
                lapis.pendown()
                lapis.write("PARABÉNS! VOCÊ VENCEU!",'green', font = ('Arial',70,'normal'))
            decisao = window.textinput("RESTART", "Deseja jogar novamente?(sim ou não?)")
            if decisao == "nao" or decisao == "Nao" or decisao == "Não" or decisao == "não":
                lapis.clear()
                lapis.penup()
                lapis.setpos(-590,0)
                lapis.pendown()
                lapis.color("white")
                lapis.write("OBRIGADO POR JOGAR!", font = ("Arial", 70 , "normal"))
                window.exitonclick()
                break
            if decisao=='sim' or decisao=='Sim':
                lapis.reset()
                lapis.width(8)
                lapis.speed(10)
                break
        else:
            letra = window.textinput("FAÇA SUA ESCOLHA", "Escolha uma letra:")
            letra = letra.upper()         
           
    
                
                
                
window.exitonclick()
    
                        
                
                