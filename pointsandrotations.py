ps = [-9, 0, 9]
x, y, z = 0, 1, 2
degrees = [-90, 0, 90]

front = [(10, i, -j) for j in ps for i in ps]
left = [(i, -10, -j) for j in ps for i in ps]
back = [(-10, i, -j) for j in ps for i in ps]
right = [(-i, 10, -j) for j in ps for i in ps]
up = [(k, n, 10) for k in ps for n in ps]
down = [(-k, n, -10) for k in ps for n in ps]

sides = [front, left, back, right, up, down]
side_labels = ['front', 'left', 'back', 'right', 'up', 'down']

points = {p for s in sides for p in s}

layer_R = {p for p in points if p[y] > 0}
layer_F = {p for p in points if p[x] > 0}
layer_L = {p for p in points if p[y] < 0}
layer_B = {p for p in points if p[x] < 0}
layer_U = {p for p in points if p[z] > 0}
layer_D = {p for p in points if p[z] < 0}

side_layers = [layer_R, layer_F, layer_L, layer_B, layer_U, layer_D]

dir_rotations = [['R'], ['F'], ['L'], ['B'], ['U'], ['D']]
inv_rotations = [['Ri'], ['Fi'], ['Li'], ['Bi'], ['Ui'], ['Di']]

def turn(cube, axis, deg):
    if deg in degrees:
        return {rotate_vector(p, axis, deg): cube[p] for p in points}
    if deg > 90: return turn(turn(cube, axis, 90), axis, deg - 90)
    if deg < -90: return turn(turn(cube, axis, -90), axis, deg + 90)

def rotate(cube, rotations):
    if rotations in dir_rotations: return dir_rotate(cube, rotations)
    if rotations in inv_rotations: return inv_rotate(cube, rotations)
    return rotate(rotate(cube, rotations[0:1]), rotations[1:])

def dir_rotate(cube, rotation):
    if rotation == ['R']: return rot_R(cube)
    if rotation == ['F']: return rot_F(cube)
    if rotation == ['L']: return rot_L(cube)
    if rotation == ['B']: return rot_B(cube)
    if rotation == ['U']: return rot_U(cube)
    if rotation == ['D']: return rot_D(cube)

def inv_rotate(cube, rotation):
    if rotation == ['Ri']: return rot_Ri(cube)
    if rotation == ['Fi']: return rot_Fi(cube)
    if rotation == ['Li']: return rot_Li(cube)
    if rotation == ['Bi']: return rot_Bi(cube)
    if rotation == ['Ui']: return rot_Ui(cube)
    if rotation == ['Di']: return rot_Di(cube)

def rot_R(cube):
    new_cube = {}
    for p in layer_R: new_cube[rotate_vector(p, y, 90)] = cube[p]
    for p in [p for p in points if p not in layer_R]: new_cube[p] = cube[p]
    return new_cube

def rot_F(cube):
    new_cube = {}
    for p in layer_F: new_cube[rotate_vector(p, x, 90)] = cube[p]
    for p in [p for p in points if p not in layer_F]: new_cube[p] = cube[p]
    return new_cube

def rot_L(cube):
    new_cube = {}
    for p in layer_L: new_cube[rotate_vector(p, y, -90)] = cube[p]
    for p in [p for p in points if p not in layer_L]: new_cube[p] = cube[p]
    return new_cube

def rot_B(cube):
    new_cube = {}
    for p in layer_B: new_cube[rotate_vector(p, x, -90)] = cube[p]
    for p in [p for p in points if p not in layer_B]: new_cube[p] = cube[p]
    return new_cube

def rot_U(cube):
    new_cube = {}
    for p in layer_U: new_cube[rotate_vector(p, z, 90)] = cube[p]
    for p in [p for p in points if p not in layer_U]: new_cube[p] = cube[p]
    return new_cube

def rot_D(cube):
    new_cube = {}
    for p in layer_D: new_cube[rotate_vector(p, z, -90)] = cube[p]
    for p in [p for p in points if p not in layer_D]: new_cube[p] = cube[p]
    return new_cube

def rot_Ri(cube):
    new_cube = {}
    for p in layer_R: new_cube[rotate_vector(p, y, -90)] = cube[p]
    for p in [p for p in points if p not in layer_R]: new_cube[p] = cube[p]
    return new_cube

def rot_Fi(cube):
    new_cube = {}
    for p in layer_F: new_cube[rotate_vector(p, x, -90)] = cube[p]
    for p in [p for p in points if p not in layer_F]: new_cube[p] = cube[p]
    return new_cube

def rot_Li(cube):
    new_cube = {}
    for p in layer_L: new_cube[rotate_vector(p, y, 90)] = cube[p]
    for p in [p for p in points if p not in layer_L]: new_cube[p] = cube[p]
    return new_cube

def rot_Bi(cube):
    new_cube = {}
    for p in layer_B: new_cube[rotate_vector(p, x, 90)] = cube[p]
    for p in [p for p in points if p not in layer_B]: new_cube[p] = cube[p]
    return new_cube

def rot_Ui(cube):
    new_cube = {}
    for p in layer_U: new_cube[rotate_vector(p, z, -90)] = cube[p]
    for p in [p for p in points if p not in layer_U]: new_cube[p] = cube[p]
    return new_cube

def rot_Di(cube):
    new_cube = {}
    for p in layer_D: new_cube[rotate_vector(p, z, 90)] = cube[p]
    for p in [p for p in points if p not in layer_D]: new_cube[p] = cube[p]
    return new_cube

def rotate_vector(vector, axis, deg):
    if deg == 0: return vector
    if deg == 90: return tuple(sum([rotation_matrix(axis)[i][j] * vector[j]
                         for j in range(3)]) for i in range(3))
    if deg == -90: return tuple(sum([inv_rot_matrix(axis)[i][j] * vector[j]
                         for j in range(3)]) for i in range(3))

def rotation_matrix(axis):
    if axis == x: return [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
    if axis == y: return [[0, 0, -1], [0, 1, 0], [1, 0, 0]]
    if axis == z: return [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]

def inv_rot_matrix(axis):
    if axis == x: return [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    if axis == y: return [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
    if axis == z: return [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
