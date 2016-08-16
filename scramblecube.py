from pointsandrotations import *
from sidesandprinting import *
import random as rd

rotations = [(y, 0, 90), (x, 0, 90), (y, 3, 270), (x, 3, 270), (z, 0, 90),
    (z, 3, 270)]
# Axis, row and degree. Selected so, that in a sequence of randomly Selected
# rotations, any rotation can not reverse it's direct predecessor.

def scramble(cube):
    new_cube = cube
    for n in range(30):
        rot = rotations[rd.randrange(6)]
        new_cube = rotate(new_cube, rot[0], rot[1], rot[2])
    return new_cube
