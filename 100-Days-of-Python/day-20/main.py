from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()

color_list = [
    (251, 249, 245), (209, 165, 124), (249, 234, 236), (140, 49, 106),
    (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56),
    (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51),
    (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49),
    (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190)
]

for row in range(10):

    for dot in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

    # Move to next row
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.setheading(0)

screen.exitonclick()