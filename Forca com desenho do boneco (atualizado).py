import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Jogo da forca super hardcore")

lapis   = turtle.Turtle()  # Cria um objeto "desenhador"
turtle.setup (width = 1500)
lapis.width("8")
lapis.speed(20)  # define a velocidade
lapis.penup()       # Remova e veja o que acontece
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
    
erros = 0                     #estabelece erros iniciais como 0

lapis.width(3)

def desenha_boneco():                     #funçaõ completa do desenho do boneco
    if erros == 0:
        lapis.color("white")
        lapis.penup()
        lapis.setpos(-330,170)
        lapis.pendown()
        lapis.circle(30)
    if erros == 0:
        lapis.penup()
        lapis.setpos(-300, 140)
        lapis.pendown()
        lapis.right(0)
        lapis.forward(70)
    if erros == 0:
        lapis.penup()
        lapis.setpos(-300,70)
        lapis.pendown()
        lapis.right(30)
        lapis.forward(50)
    if erros == 0:
        lapis.penup()
        lapis.setpos(-300,70)
        lapis.pendown()
        lapis.left(60)
        lapis.forward(50)
    if erros == 0:
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
    if erros == 0:
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
        lapis.setpos(40, 150)
        lapis.pendown()
        lapis.color("blue")
        lapis.write("PARABÉNS! VOCÊ É BURRO!", font = ("Arial",30 , "normal"))
        

desenha_boneco()

window.exitonclick()