from pointsandrotations import *

front = [(10, i, -j) for j in ps for i in ps]
left = [(i, -10, -j) for j in ps for i in ps]
back = [(-10, i, -j) for j in ps for i in ps]
right = [(-i, 10, -j) for j in ps for i in ps]
up = [(k, n, 10) for k in ps for n in ps]
down = [(-k, n, -10) for k in ps for n in ps]

sides = [front, left, back, right, up, down]
side_labels = ['front', 'left', 'back', 'right', 'up', 'down']

def intialize_cube():
    cube = {}
    for p in front: cube[p] = 'r'   # Front side is red.
    for p in left: cube[p] = 'g'    # Left side is green.
    for p in back: cube[p] = 'o'    # Back side is orange.
    for p in right: cube[p] = 'b'   # Right side is blue.
    for p in up: cube[p] = 'w'      # Up side is white.
    for p in down: cube[p] = 'y'    # Down side is yellow.
    return cube

def print_cube(cube):
    for i in range(6):
        print(side_labels[i] + ':' + '\n')
        print_side(cube, sides[i])
        print('')

def print_side(cube, side):
    rows = ['', '', '']
    for i in range(3):
        for p in side[0 + i*3: 3 + i*3]:
            rows[i] += cube[p]
    for r in rows: print(r)

start_cube = intialize_cube()
