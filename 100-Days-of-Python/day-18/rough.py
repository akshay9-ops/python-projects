import random
from turtle import Turtle, Screen
screen = Screen()
# Set up the turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(5)
timmy.speed("fast")

shift = 1
for _ in range(10):
    print(shift)
    angle = 360 / shift
    shift += 1
    print(angle)
    print(shift)