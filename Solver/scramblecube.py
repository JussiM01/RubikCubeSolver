from pointsandrotations import *
from sidesandprinting import *
import random as rd

def scramble(cube):
    rot_sequence = [dir_rotations[rd.randrange(6)][0] for n in range(30)]
    return rotate(cube, rot_sequence)
