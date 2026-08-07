PADDLE_MOVE = 20
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def move_up(self):
        new_y = self.ycor() + PADDLE_MOVE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_MOVE
        self.goto(self.xcor(), new_y)
