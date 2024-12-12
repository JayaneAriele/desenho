import turtle

#borboleta

turtle.title("Borboleta")
turtle.speed(2)
zoom=3

turtle.color("purple")
turtle.begin_fill()

input('Precione ENTER para começar')

#corpo da borboleta

def inferior_borboleta():
    inferior_borboleta=[
        (-20,0),
        (20,0),
        (30,5),
        (30,15),
        (20,20),
        (0,20),
        (-20,20),
        (-30,15),
        (-30,5),
        (-20,0),
        (0,0)
    ]
    for (x,y) in inferior_borboleta:
        turtle.goto(x*zoom,y*zoom)

inferior_borboleta()

turtle.penup()
turtle.goto(0*zoom,20*zoom)
turtle.pendown()

def superior_borboleta():
    superior_borboleta=[
        (30,35),
        (30,50),
        (20,60),
        (10,60),
        (0,50),
        (-10,60),
        (-20,60),
        (-30,50),
        (-30,35),
        (0,20)
    ]
    for (x,y) in superior_borboleta:
        turtle.goto(x*zoom,y*zoom)

superior_borboleta()

turtle.end_fill()

#anteninhas da borboleta

turtle.penup()
turtle.goto(0*zoom,50*zoom)
turtle.left(50)
turtle.pendown()

turtle.color("violet")
turtle.begin_fill()

turtle.fd(30*zoom)
turtle.right(90)
turtle.circle(2*zoom)

turtle.left(90)
turtle.back(30*zoom)

turtle.left(79)
turtle.fd(30*zoom)
turtle.right(90)
turtle.circle(2*zoom)

turtle.end_fill()


turtle.done()
