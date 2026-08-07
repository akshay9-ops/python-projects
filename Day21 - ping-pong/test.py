import turtle

# Function to draw any size rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle color and speed
turtle.color("white")
turtle.speed(3)

# Call the function (Example: length/width = 200, height = 100)
draw_rectangle(200, 100)

# Keep the window open
screen.mainloop()