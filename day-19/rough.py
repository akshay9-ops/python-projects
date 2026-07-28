import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
# To setup the dimension of screen
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)
tim.penup()
tim.goto(-240,0)
all_turtle = []
def multiple_turtles(turtles):
    for _ in range(4):
        all_turtle.append(a.turtle)
    return all_turtle


screen.exitonclick()