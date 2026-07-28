from turtle import Turtle, Screen
import random

in_race_on = False
screen = Screen()
screen.colormode(255)
# To setup the dimension of screen
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
y_axis = -40

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()

    new_turtle.goto(x = -230,y = y_axis)
    y_axis += 20
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() < 210:
            random_distance = random.randint(0,10)

            turtle.forward(random_distance)
            turtle.speed("fastest")

        elif turtle.xcor() >= 210:
            winning_color = turtle.fillcolor()
            if user_bet == winning_color:
                print(f"You win! The {winning_color} turtle is the winner!")
            elif user_bet != winning_color:
                print(f"You lost! The {winning_color} turtle is the winner!")
            is_race_on = False


screen.exitonclick()
