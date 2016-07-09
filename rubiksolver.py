import numpy as np

""" Encoding:
    cube = np.array([front, left_side, back, right_side, bottom, top]),
where
    side = [first_row, second_row, third_row],
    row = 'abc'
 and
    'a', 'b' and 'c' are one of 'r', 'g' or 'b' (red, green or blue).

 The rows are encoded as follows: If the side is front, left, back or right; the
 first row is the top most row. If it is the top side, the first row is the back
 most row. For the bottom side the first row is the front most row. The labels
 'r', 'g', and 'b' are encoded in the order in which they apper as seen from
 outside the cube (when looked at the angle in which the first row is the top
 most row)."""

def rotate(cube, axis, row, deg):
    reverse_flipped = flip_axis(axis, flip_axis(axis, flip_axis(axis, cube)))
    return  flip_axis(axis, rotate_around_z(reverse_flipped))

def rotate_around_z(cube, row, deg):
    return ...

def flip_axis(axis, cube):
    if axis == z: return cube
    if axis == x: return ...
    if axis == y: return ...
