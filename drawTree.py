
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def draw_rectangle(width, height, color):
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

turtle.penup()
turtle.goto(-20, -200)
turtle.pendown()
draw_rectangle(40, 120, "saddlebrown")

turtle.left(90)
turtle.forward(120)

turtle.speed(0)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.right(120)
turtle.forward(260)
turtle.right(120)
turtle.forward(260)
turtle.right(120)
turtle.forward(120)
turtle.end_fill()


turtle.penup()
turtle.goto(-150, 250)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()


screen.exitonclick()


