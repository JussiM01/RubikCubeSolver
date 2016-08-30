from scramblecube import *
from solvecross import *

def corners_solved(cube):
    if not white_side_up(cube): return False
    if not blue_triangle(cube): return False
    if not orange_triangle(cube): return False
    if not green_triangle(cube): return False
    if not red_triangle(cube): return False
    return True

triangle_R = {(9, 10, 9), (0, 10, 9), (-9, 10, 9), (0, 10, 0)}
triangle_B = {(-10, 9, 9), (-10, 0, 9), (-10, -9, 9), (-10, 0, 0)}
triangle_L = {(-9, -10, 9), (0, -10, 9), (9, -10, 9), (0, -10, 0)}
triangle_F = {(10, -9, 9), (10, 0, 9), (10, 9, 9), (10, 0, 0)}

def white_side_up(cube): return {cube[p] for p in up} == {'w'}
def blue_triangle(cube): return {cube[p] for p in triangle_R} == {'b'}
def orange_triangle(cube): return {cube[p] for p in triangle_B} == {'o'}
def green_triangle(cube): return {cube[p] for p in triangle_L} == {'g'}
def red_triangle(cube): return {cube[p] for p in triangle_F} == {'r'}

def test_make_a_cross(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        new_cube = make_a_top_layer(cube)[0]
        solved = corners_solved(new_cube)
        if solved: count += 1
    print('Solved correctly ' + str(count) + ' out of ' + str(num_iter) + '.')
