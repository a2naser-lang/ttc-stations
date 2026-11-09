import math

def volume_square(radius):
    return math.pi * (4/3) * radius ** 3

def volume_cube(side):
    return side ** 3

def volume_cylinder(radius, length):
    return math.pi * length * radius ** 2 