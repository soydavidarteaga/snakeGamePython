import random
import time
import turtle

posponer = 0.2

#Score
score = 0
high_score = 0

#Configurando ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#head snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.color("#00E43D")

#body snake
steps = []

#Text
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0     High Score: 0", align= "center", font= ("Courier", 24, "normal"))

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.penup()
food.goto(0,100)
food.color("red")

#Funciones
def reset():
    head.direction = "stop"
    global score
    score = 0
    steps.clear()
    reFood()

def gameOver():
    text = turtle.Turtle()
    text.color("red")
    text.penup()
    text.hideturtle()
    text.goto(0, 0)
    text.write("Game over", align="center", font=("Courier", 35, "bold"))
    time.sleep(1)
    text.clear()

def newStep():
    new = turtle.Turtle()
    new.speed(0)
    new.shape("square")
    new.penup()
    new.goto(0, 0)
    new.direction = "stop"
    new.color("#009F2A")
    steps.append(new)
    global score
    global high_score
    score += 10
    if score > high_score:
        high_score = score
    printScores()
def printScores():
    text.clear()
    text.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
def hiddenStep():
    for step in steps:
        step.goto(2000,2000)
    gameOver()
    reset()
    printScores()
def increaseBody():
    total = len(steps)
    for i in range(total - 1, 0, -1):
        x = steps[i - 1].xcor()
        y = steps[i - 1].ycor()
        steps[i].goto(x,y)
    if total > 0:
        x = head.xcor()
        y = head.ycor()
        steps[0].goto(x,y)
def reFood():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Teclado
wn.listen()
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")

#Cuando se crea un juego es necesario que la pantalla se este actualizando periodicamente, es por ello que se crea un bucle infinito
while True:
    wn.update()

    #Detectando colision con comida
    if head.distance(food) < 20:
        reFood()
        newStep()
    #Colisiones con el cuerpo
    for step in steps:
        if step.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            hiddenStep()
    #Colisiones bordes
    if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        hiddenStep()

    #Agregandole dificultad
    if(score > 50):
        posponer = 0.1

    #agregando cuerpo a la serpiente
    increaseBody()

    mov()
    time.sleep(posponer)


