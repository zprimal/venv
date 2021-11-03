from turtle import Turtle, Screen, colormode
from random import uniform, randint, choice

def getColorNum():
    # print(round(uniform(0, 255), 2))
    # return round(uniform(0, 255), 2)
    return randint(0, 255)

def randHirst():
    rgbColors = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]
    return choice(rgbColors)

turtle = Turtle()
turtle.shape("arrow")
turtle.color("red")
turtle.speed("fastest")

colormode(255)
# turtle.pencolor(getColorNum(), getColorNum(), getColorNum())

# Make a square
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# Make a dashed line
turtle.pensize(20)
for i in range(10):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

# Make an overlay of poly-3 to poly-10
turtle.pensize(5)
for i in range(3, 11):
    angle = 360 / i
    turtle.pencolor(getColorNum(), getColorNum(), getColorNum())
    for j in range(i):
        turtle.forward(100)
        turtle.right(angle)

# Draw spirogram
turtle.pensize(1)
for i in range(0, 361, 5):
    turtle.circle(100)
    turtle.pencolor(getColorNum(), getColorNum(), getColorNum())
    turtle.right(5)

turnLeft = True
turtle.penup()
for i in range(10):
    for j in range(9):
        turtle.dot(20, randHirst())
        turtle.forward(50)
    turtle.dot(20, randHirst())
    if turnLeft:
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turnLeft = False
    else:
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turnLeft = True


screen = Screen()
screen.exitonclick()
