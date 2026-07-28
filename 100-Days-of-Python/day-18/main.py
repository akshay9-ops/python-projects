import random
from turtle import Turtle, Screen
screen = Screen()
# Set up the turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
# To go the color from 0 to 255
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_of_gap)
    # angle += 5
draw_spirograph(5)
#radious 100


# Keeps the window open until you click it
screen.exitonclick()

