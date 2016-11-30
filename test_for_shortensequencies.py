from solvefinalstage import *
from shortensequencies import *

all_rotations = [['R'], ['F'], ['L'], ['B'], ['U'], ['D'], ['Ri'], ['Fi'],
    ['Li'], ['Bi'], ['Ui'], ['Di']]

def test_shorten():
    sequence = [all_rotations[rd.random()] for i in range(10)]
    shortened = shorten(sequence)
    print('SEQUENCE: ', sequence)
    print('SHORTENED SEQUENCE: ', shortened)
    cube1 = rotate(start_cube, sequence)
    cube2 = rotate(start_cube, shortened)
    cubes_same = cube1 == cube2
    print('CUBES ARE THE SAME: ', cubes_same)
