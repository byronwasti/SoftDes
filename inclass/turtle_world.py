""" TURTLE WORLD """
from swampy.TurtleWorld import *
from math import pi, sin
import random

world = TurtleWorld()
beth = Turtle()
beth.x = 100
beth.y = -500
beth.set_pen_color('red')
beth.delay = 0

def draw_line(turtle, start_x, start_y, angle, line_length):
    ''' DRAWS A LINE
        turtle: turtle object
        start_x: start pos x
        start_y: start pos y
        angle: angle of line w/ respect to x-axis
        line_length: length of line
    '''
    turtle.x = start_x
    turtle.y = start_y
    turtle.heading = angle
    turtle.fd(line_length)

def my_square(turtle, x, y, length):
    my_regular_polygon(turtle,x,y,length,4)

def my_regular_polygon(turtle,x,y,length,sides):
    turtle.x = x
    turtle.y = y
    for i in xrange(sides):
        turtle.heading = i*360/sides
        turtle.fd(length)

def my_circle(turtle,x,y,radius):
    n = 50
    my_regular_polygon(turtle, x+radius, y+radius, 2*pi*radius/float(n), n)

def turtle_sin(turtle): 
    for i in range(100):
        turtle.heading = sin(i/5.0)*180.0/pi
        turtle.fd(10)

def snow_flake_side(turtle, length,level):
    ''' Draw side of snowflakkkkkkeee'''
    if level == 0:
        turtle.fd(length)
        turtle.rt(60)
        turtle.fd(length)
        turtle.rt(-120)
        turtle.fd(length)
        turtle.rt(60)
        turtle.fd(length)
        return

    snow_flake_side(turtle,length/3.0, level-1)
    turtle.rt(60)
    snow_flake_side(turtle,length/3.0, level-1)
    turtle.rt(-120)
    snow_flake_side(turtle,length/3.0, level-1)
    turtle.rt(60)
    snow_flake_side(turtle,length/3.0,level-1)
    
def snow_flake(turtle, length, level, sides):
    for i in xrange(sides):
        turtle.heading = i*360/sides
        snow_flake_side(turtle, length, level)

def tree ( turtle, length, level):
    ''' MAKE A TREE '''
    if level == 0:
        turtle.set_pen_color('green')
        turtle.fd(length)
        both = Turtle()

        both.x = turtle.x
        both.y = turtle.y
        both.heading = turtle.heading
        both.set_pen_color('green')

        both.rt(-random.randrange(20,50))
        both.fd(length)
        both.undraw()
        turtle.bk(length/3.0)
        both = Turtle()

        both.x = turtle.x
        both.y = turtle.y
        both.heading = turtle.heading
        both.set_pen_color('green')

        both.rt(random.randrange(20,50))
        both.fd(length)
        both.undraw()
        return

    turtle.set_pen_color('brown')
    turtle.fd(length)
    both = Turtle()

    both.x = turtle.x
    both.y = turtle.y
    both.heading = turtle.heading

    both.rt(-random.randrange(20,50))
    tree ( both, length*0.6, level-1)
    both.undraw()
    turtle.bk(length/3.0)
    both = Turtle()

    both.x = turtle.x
    both.y = turtle.y
    both.heading = turtle.heading

    both.rt(random.randrange(20,50))
    tree(both, length*0.64, level-1)
    both.undraw()


snow_flake(beth,22,5, 10)
#beth.heading = 90
#tree( beth, 100, 12)
wait_for_user()
