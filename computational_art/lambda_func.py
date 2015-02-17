""" TODO: Put your header comment here """

import random
import inspect
from math import sin, cos, pi
from PIL import Image


def build_ran_func(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    if max_depth < 2:
        if random.randrange(0,2) == 0:
            return lambda x,y: x  
        else: return lambda x,y: y

    tmp = 0
    #tmp = random.randrange(0,1)
    #if min_depth < 0: tmp = random.randrange(0,8)     

    if tmp == 0: # PRODUCT
        func1 = build_ran_func(min_depth-1,max_depth-1)
        func2 = build_ran_func(min_depth-1,max_depth-1)
        return (lambda x,y:  x * y)(func1,func2)
    elif tmp == 1: # AVERAGE
        return lambda x,y: ((build_ran_func(min_depth-1,max_depth-1))(x,y) + (build_ran_func(min_depth-1,max_depth-1)(x,y)))/2.0
    elif tmp == 2: # COS_PI
        return lambda x,y: cos(pi*(build_ran_func(min_depth-1,max_depth-1))(x,y))
    elif tmp == 3: # SIN_PI
        return lambda x,y: sin(pi*(build_ran_func(min_depth-1,max_depth-1))(x,y))
    elif tmp == 4: # Divide by two
        return lambda x,y: (build_ran_func(min_depth-1,max_depth-1))(x,y)/2.0
    elif tmp == 5: # square
        return lambda x,y: (build_ran_func(min_depth-1,max_depth-1))(x,y)**2
    elif tmp == 6: # X
        return lambda x,y: x
    elif tmp == 7: # Y
        return lambda x,y: y

#print inspect.getsource(build_ran_func(0,5))

def brf(f,n):
    if n == 0:
        return f

    tmp = random.randrange(0,4)

    if tmp == 0:
        return brf((lambda x,y: f(x,y)) * (lambda x: f(x,y),n-1))
    elif tmp == 1:
        return brf( ((lambda x,y: f(x,y)) + (lambda x: f(x,y)))/2.0, n-1)
    elif tmp == 2:
        return brf( lambda x,y: cos( pi * f(x,y) ), n-1)
    elif tmp == 3:
        return brf( lambda x,y: sin(pi * f(x,y) ), n-1)

f = brf(lambda x,y: x, 3)
print f(3)
print f(3)
print f(3)


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


def generate_art(filename, x_size=300, y_size=300): #x_size=1600, y_size=900):
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
    maximum = 10
    minimum = 3
    #red_function = build_ran_func(random.randrange(0,minimum),random.randrange(0,maximum))
    #green_function = build_ran_func(random.randrange(0,minimum),random.randrange(0,maximum))
    #blue_function = build_ran_func(random.randrange(0,minimum),random.randrange(0,maximum))
    red_function = build_ran_func(0,9)
    blue_function = build_ran_func(0,9)
    green_function = build_ran_func(0,9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(red_function (x, y)),
                    color_map(green_function (x, y)),
                    color_map(blue_function (x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    #doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    #generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")
