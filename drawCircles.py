"""
Draws six circles, centered on the origin, each a different color.
Assumption: the number of colors in the turtle colors list is at least
as long as the number of rings.
"""


import turtle
import math

scr = turtle.Screen()
turt = turtle.Turtle() #Turtle was spelled incorrectly

scr.bgcolor("seashell")

tColors = ["light salmon", "light sky blue", "pale green", "light coral", "pale turquoise", "plum"] #light spelled wrong

turt.width(5)
numRings = 6

for i in range(numRings):
    turt.color(tColors[i]) #changed from 0 to i
    radius = 40 * (i + 1)

    turt.up()
    turt.forward(radius)
    turt.down()
    
    turt.left(90)
    turt.circle(radius) #changed from i to radius
    turt.right(90) #changed from 60 to 90
    
    turt.up() #add parantheses
    turt.backward(radius)
    turt.down()

scr.exitonclick()
