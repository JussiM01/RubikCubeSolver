ps = [-0.9, 0.0, 0.9]
x, y, z = 0, 1, 2
degrees = [0, 90, 180, 270]
top_side = [(p0, p1, 1.0) for p0 in ps for p1 in ps]

def rotate(cube, axis, row, deg):
    return {rotation_on_row(p, axis, row, deg): cube[p] for p in points}

def rotation_on_row(p, axis, row, deg):
    if abs(p[axis] + row - 1) < 0.2: return rotate_vector(p, axis, deg)
    return p

def rotate_vector(vector, axis, deg):
    if deg == 0: return vector
    if deg == 90: return tuple(sum([rotation_matrix(axis)[i][j] * vector[j]
                         for j in range(3)]) for i in range(3))
    return rotate_vector(rotate_vector(vector, axis, 90), axis, deg - 90)

def rotation_matrix(axis):
    if axis == x: return [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
    if axis == y: return [[0, 0, -1], [0, 1, 0], [1, 0, 0]]
    if axis == z: return [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]

points = {rotate_vector(p, axis, deg) for p in top_side for axis in (x, y)
          for deg in degrees}
