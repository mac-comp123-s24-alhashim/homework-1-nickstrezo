
"This program is supposed to find the center point where a drone will leave from in a search and rescue mission.
"It will also calculate the number of circles and their diameters"
"@author: Nick Strezo nstrezo@macalester.edu"

import math

width = float(input("In meters, what is the width of the rescue area in meters?"))

height = float(input("In meters what is the height of the rescue area in meters?"))

Center_of_x = width/2

Center_of_y = height/2

Hypotenuse = math.sqrt(height**2 + width**2)

Radius = Hypotenuse/2


Circle_number = math.ceil(Radius/5)

print("the center point of the search and rescue is", (Center_of_x, Center_of_y))
print("The radius of the largest circle is;", Radius, "meters")
print("The number of circles for the search and rescue is: ", Circle_number)