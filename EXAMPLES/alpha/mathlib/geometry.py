"""
General geometry-related functions

Syntax:

area = circle_area(diameter)
area = rectangle_area(length, width)
area = square_area(side)
"""
import math   # load math.py

PI = math.pi

ANIMALS = ['wombat', 'koala', 'wallaby']

def main():
    a = circle_area(22)
    print(f"a: {a}")

def circle_area(diameter):
    """
    Compute the area of a circle from a given diameter

    :param diameter: Diameter of circle
    :type: numeric
    :return: Area of circle
    :rtype: float
    """
    radius = diameter / 2
    return PI * (radius ** 2)

def rectangle_area(length, width):
    """
    Compute the area of a rectangle.

    :param length:  length of longer side
    :param width:   length of shorter side
    :return: Area of rectangle
    """
    return length * width

def square_area(side):
    """
    Compute area of a square.

    :param side: Length of one side
    :return: Area of square
    """
    return side ** 2

# "private" function
def _groot():
    print("I am Groot")

print(f"__name__: {__name__}")


if __name__ == "__main__":  # running as script
    main()
    
# (else)
#   imported as module
