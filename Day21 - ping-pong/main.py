from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

#Screen set-up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game!")

#disable updates
screen.tracer(0)

#create paddles
left_paddle = Paddle(- 350,0)
right_paddle = Paddle(350,0)

#create ball
ball = Ball()

#move paddle
screen.listen()

# Create scoreboard
scoreboard = Scoreboard()

screen.onkey(key="Up",fun=right_paddle.move_up)
screen.onkey(key="Down",fun=right_paddle.move_down)

screen.onkey(key="w",fun=left_paddle.move_up)
screen.onkey(key="s",fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()  # refresh screen
    time.sleep(ball.speed_move)
    ball.move_ball()
    #detect collision with top and bottom wall (y)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # Detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset_ball()
    # Detect when left paddle misses
    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset_ball()
    # detect collision with right paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()






screen.exitonclick()





