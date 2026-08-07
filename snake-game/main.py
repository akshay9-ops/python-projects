from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#Turn off the tracer, i.e. don't update everytime
screen.tracer(0)

#creates snake
snake = Snake()
#creates food randomly
food = Food()
#Scoreboard show
scoreboard = Scoreboard()

#play buttons
screen.listen()
#They are configuration, not game logic.
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)



game_is_on = True
while game_is_on:
    #Update only when I call
    screen.update()
    time.sleep(0.1)
#moves snake
# This code will let snake follow object 1 where ever it goes
    snake.move()
    # Detect collision with food
    #to know distance from snake head to food
    if snake.head.distance(food) < 15:
        # print("nom nom nom nom nom") this is to check if code works
        food.refresh()
        #extend the snake
        snake.extend()
        # scoreboard
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail.
    #If head collides with any segment in the tail:
        #Trigger game_over sequence
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         scoreboard.game_over()
    #         game_is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False








screen.exitonclick()