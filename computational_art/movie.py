""" TODO: Put your header comment here """

import random
from math import sin, cos, pi
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    if max_depth == 1:
        tmp = random.randrange(0,3)
        if tmp == 0: return ['x']
        if tmp == 1: return ['y']
        if tmp == 2: return ['t']

    tmp = random.randrange(0,4)
    if min_depth < 0: tmp = random.randrange(0,7)

    if tmp == 0: # PRODUCT
        return ['prod',build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    elif tmp == 1: # AVERAGE
        return ['avg',build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
    elif tmp == 2: # COS_PI
        return ['cos_pi',build_random_function(min_depth-1,max_depth-1)]
    elif tmp == 3: # SIN_PI
        return ['sin_pi',build_random_function(min_depth-1,max_depth-1)]
    '''
    elif tmp == 4: # DIVIDE BY TWO
        return ['div2',build_random_function(min_depth-1,max_depth-1)]
    elif tmp == 5: # SQUARE
        return ['square',build_random_function(min_depth-1,max_depth-1)]
    '''
    if tmp == 4: # X
        return ['x']
    elif tmp == 5: # Y
        return ['y']
    elif tmp == 6: # t
        return ['t']


def avg(a,b):
    return (a+b)/2.0


def evaluate_random_function(f, x, y, t):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    if f[0] == 'prod':
        return evaluate_random_function(f[1],x,y,t)*evaluate_random_function(f[2],x,y,t)
    if f[0] == 'avg':
        return avg( evaluate_random_function(f[1],x,y,t), evaluate_random_function(f[2],x,y,t))
    if f[0] == 'cos_pi':
        return cos(pi * evaluate_random_function(f[1],x,y,t))
    if f[0] == 'sin_pi':
        return sin(pi * evaluate_random_function(f[1],x,y,t))
    if f[0] == 'div2':
        return evaluate_random_function(f[1],x,y,t)/2.0
    if f[0] == 'square':
        return evaluate_random_function(f[1],x,y,t)**2
    if f[0] == 'x':
        return x
    if f[0] == 'y':
        return y
    if f[0] == 't':
        return t

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this
    return (output_interval_end - output_interval_start)/float(input_interval_end - input_interval_start)*(val-input_interval_start) + output_interval_start


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=1800, y_size=750):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=300, y_size=300, time=1): #x_size=1600, y_size=900):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    '''
    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]
    '''
    maximum = 50
    minimum = 30
    red_function = build_random_function(random.randrange(0,minimum),random.randrange(0,maximum))
    green_function = build_random_function(random.randrange(0,minimum),random.randrange(0,maximum))
    blue_function = build_random_function(random.randrange(0,minimum),random.randrange(0,maximum))

    '''






    '''

    print red_function
    print green_function
    print blue_function

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for k in range(time):
        for i in range(x_size):
            for j in range(y_size):
                x = remap_interval(i, 0, x_size, -1, 1)
                y = remap_interval(j, 0, y_size, -1, 1)
                t = remap_interval(k, 0, time, -1, 1)
                pixels[i, j] = (
                        color_map(evaluate_random_function(red_function, x, y, t)),
                        color_map(evaluate_random_function(green_function, x, y, t)),
                        color_map(evaluate_random_function(blue_function, x, y, t))
                        )
        
        im.save(filename +  str("%03d" % k) + '.png')


if __name__ == '__main__':
    import doctest
    #doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("myart")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")
