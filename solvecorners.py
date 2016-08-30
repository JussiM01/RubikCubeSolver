from solvecross import *

top_corners = [((9, 9, 10), (10, 9, 9), (9, 10, 9)), ((-9, 9, 10), (-9, 10, 9),
    (-10, 9, 9)), ((-9, -9, 10), (-10, -9, 9), (-9, -10, 9)), ((9, -9, 10),
    (9, -10, 9), (10, -9, 9))]
bottom_corners = [((9, 9, -10), (10, 9, -9), (9, 10, -9)), ((-9, 9, -10),
    (-9, 10, -9), (-10, 9, -9)), ((-9, -9, -10), (-10, -9, -9), (-9, -10, -9)),
    ((9, -9, -10), (9, -10, -9), (10, -9, -9))]

color_triplets = [('w', 'r', 'b'), ('w', 'b', 'o'), ('w', 'o', 'g'),
    ('w', 'g', 'r')]

def color_in(color, c_triplet): return color in c_triplet

def colors_match(cube, corner, c_triplet):
    return {color_in(cube[face], c_triplet) for face in corner} == {True}

def corner_fits(cube, order):
    return (tuple([cube[top_corners[order][i]] for i in range(3)])
        == color_triplets[order])

def corner_to_below(cube, corner, order, sign):
    new_cube, rotations = cube, []
    if sign == '+': n = order - top_corners.index(corner)
    if sign == '-': n = order - bottom_corners.index(corner)
    if sign == '+':
        ind = top_corners.index(corner)
        rot_sequence = side_inv[ind] + ['Di'] + side_rot[ind] + ['D']
        new_cube = rotate(new_cube, rot_sequence)
        rotations += rot_sequence
    if n > 0:
        new_cube = rotate(new_cube, ['D'] * n)
        rotations += (['D'] * n)
    if n < 0:
        new_cube = rotate(new_cube, ['Di'] * -n)
        rotations += (['Di']  * -n)
    return (new_cube, rotations)

def place_corner(cube, order):
    new_cube, rotations = cube, []
    for corner in bottom_corners:
        if colors_match(new_cube, corner, color_triplets[order]):
            res = corner_to_below(new_cube, corner, order, '-')
            new_cube = res[0]
            rotations += res[1]
            return (new_cube, rotations)
    for corner in top_corners:
        if colors_match(new_cube, corner, color_triplets[order]):
            res = corner_to_below(new_cube, corner, order, '+')
            new_cube = res[0]
            rotations += res[1]
            return (new_cube, rotations)

def fit_top_corner(cube, order):
    new_cube, rotations = cube, []
    rot_sequence = side_inv[order] + ['Di'] + side_rot[order] + ['D']
    while not corner_fits(new_cube, order):
        new_cube = rotate(new_cube, rot_sequence)
        rotations += rot_sequence
    return (new_cube, rotations)

def make_a_top_layer(cube):
    new_cube, rotations = make_a_cross(cube)
    for order in range(4):
        res1 = place_corner(new_cube, order)
        new_cube = res1[0]
        rotations += res1[1]
        res2 = fit_top_corner(new_cube, order)
        new_cube = res2[0]
        rotations += res2[1]
    return (new_cube, rotations)

# TODO: Test and debug.
