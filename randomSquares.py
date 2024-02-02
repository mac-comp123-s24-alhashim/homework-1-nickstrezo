
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light gray")

my_turtle = turtle.Turtle()
my_turtle.speed(0)

colors = ["red", "green", "blue", "yellow"]

num_squares = 25

for _ in range(num_squares):
    square_color = random.choices(colors)
    x_coord = random.randint(-250, 250)
    y_coord = random.randint(-250, 250)
    my_turtle.color(square_color)
    my_turtle.penup()
    my_turtle.goto(x_coord, y_coord)
    my_turtle.pendown()
    my_turtle.begin_fill()
    for _ in range(4):
        my_turtle.forward(20)
        my_turtle.left(90)
    my_turtle.end_fill()
screen.exitonclick()
