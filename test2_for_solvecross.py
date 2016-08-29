from scramblecube import *
from solvecross import *

def cross_solved(cube):
    if not white_cross_up(cube): return False
    if not blue_pieces(cube): return False
    if not orange_pieces(cube): return False
    if not green_pieces(cube): return False
    if not red_pieces(cube): return False
    return True

up_cross = {(0, 0, 10), (0, 9, 10), (-9, 0, 10), (0, -9, 10), (9, 0, 10)}
segment_R = {(0, 10, 9), (0, 10, 0)}
segment_B = {(-10, 0, 9), (-10, 0, 0)}
segment_L = {(0, -10, 9), (0, -10, 0)}
segment_F = {(10, 0, 9), (10, 0, 0)}

def white_cross_up(cube): return {cube[p] for p in up_cross} == {'w'}
def blue_pieces(cube): return {cube[p] for p in segment_R} == {'b'}
def orange_pieces(cube): return {cube[p] for p in segment_B} == {'o'}
def green_pieces(cube): return {cube[p] for p in segment_L} == {'g'}
def red_pieces(cube): return {cube[p] for p in segment_F} == {'r'}

def test_make_a_cross(num_iterations):
    results = []
    for n in range(num_iterations):
        cube = scramble(start_cube)
        new_cube = make_a_cross(cube)[0]
        res = cross_solved(new_cube)
        results.append(res)
    return set(results) == {True}
