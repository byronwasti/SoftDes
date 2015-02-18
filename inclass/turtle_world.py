""" TURTLE WORLD """
from swampy.TurtleWorld import *
from math import pi, sin

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

world = TurtleWorld()
beth = Turtle()
beth.set_pen_color('red')
#draw_line(beth,100,100,33,50)
#my_square(beth,50,50,100)
#my_regular_polygon(beth,0,0,100,6)
#my_circle(beth,10,10,50)
turtle_sin(beth)
wait_for_user()
