from solvefinalstage import *
from shortensequencies import *
import random as rd

all_rotations = ['R', 'F', 'L', 'B', 'U', 'D',
    'Ri', 'Fi', 'Li', 'Bi', 'Ui', 'Di']

def test_n_times_shorten(num_iter):
    count = 0
    for n in range(num_iter):
        sequence = [all_rotations[rd.randrange(12)] for i in range(30)]
        shortened = shorten(sequence)
        cube1 = rotate(start_cube, sequence)
        cube2 = rotate(start_cube, shortened)
        cubes_same = cube1 == cube2
        if cubes_same: count += 1
    print('Solved correctly ' + str(count) + ' out of ' + str(num_iter) + '.')
