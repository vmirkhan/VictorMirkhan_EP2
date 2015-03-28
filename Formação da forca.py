import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Jogo da forca super hardcore")

lapis   = turtle.Turtle()  # Cria um objeto "desenhador"
turtle.setup (width = 1500)
lapis.width("8")
lapis.speed(10)  # define a velocidade
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
    
erros = 0

lapis.width(3)

def desenha_boneco():
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

desenha_boneco()

window.exitonclick()