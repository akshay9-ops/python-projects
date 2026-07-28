# """We are getting a variable from another file within the same project"""
# from another_module import another_variable
# print(another_variable)
#
# """We are importing  a library and getting a class - Turtle"""
# """Capital T is class"""
# """Stored the Turtle class in timmy variable"""
# import turtle
# timmy = turtle.Turtle()

# """How to contruct a new object"""
# """Simple way of doing above"""
# from turtle import Turtle, Screen
# jimmy=Turtle()
# print(jimmy)
# """By passing turtle we can actually see turtle"""
# jimmy.shape("turtle")
# jimmy.color("red")
# jimmy.forward(100)
#
# # Creating an object from screen blueprint
# my_screen = Screen()
# # Tap into one of screen properties
# # Which is canvas height and canvas width
# # Object.attribute
# # We want to access canvheight attribute from object
# # This object.attribute will show up a screen and quickly disappear
# print(my_screen.canvheight)
# # This function exitonclick() will allow program to continue running until we click on screen
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
print(table.align)
table.align = "l"
print(table)
