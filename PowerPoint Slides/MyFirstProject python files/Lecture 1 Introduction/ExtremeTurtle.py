# turtle graphics for drawing lines
import turtle
# a module that helps generate random numbers
import random


# get a window
window = turtle.Screen()
# set background color
window.bgcolor("black")

# get a turtle
my_turtle = turtle.Turtle()
# set turtle speed to fastest
my_turtle.speed(0)

# counter variable for loop
x = 1

# while x is less than 400, draw lines of random colors in ordered direction

while x < 600:

    # make a random color using RGB hex values
    red_val = random.randint(0,255)
    green_val = random.randint(0,255)
    blue_val = random.randint(0,255)

    # set turtle color mode to hex values
    turtle.colormode(255)
    # set turtle pen color
    my_turtle.pencolor(red_val, green_val, blue_val)

    # move turtle
    my_turtle.forward(50 + x)
    my_turtle.right(90.911)

    # increment x value
    x += 1

turtle.done()
