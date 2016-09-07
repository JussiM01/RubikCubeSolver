from scramblecube import *
from solve2layers import *

def twolayers_solved(cube):
    if not white_side_down(cube): return False
    if not green_2layers(cube): return False
    if not orange_2layers(cube): return False
    if not blue_2layers(cube): return False
    if not red_2layers(cube): return False
    return True

twolayers_R = {p for p in points if p[y] == 10 and p[z] < 9}
twolayers_B = {p for p in points if p[x] == -10 and p[z] < 9}
twolayers_L = {p for p in points if p[y] == -10 and p[z] < 9}
twolayers_F = {p for p in points if p[x] == 10 and p[z] < 9}

def white_side_down(cube): return {cube[p] for p in down} == {'w'}
def green_2layers(cube): return {cube[p] for p in twolayers_R} == {'g'}
def orange_2layers(cube): return {cube[p] for p in twolayers_B} == {'o'}
def blue_2layers(cube): return {cube[p] for p in twolayers_L} == {'b'}
def red_2layers(cube): return {cube[p] for p in twolayers_F} == {'r'}

def test_make_a_2nd_layer(num_iter):
    count = 0
    for n in range(num_iter):
        cube = scramble(start_cube)
        new_cube = make_a_2nd_layer(cube)[0]
        solved = twolayers_solved(new_cube)
        if solved: count += 1
    print('Solved correctly ' + str(count) + ' out of ' + str(num_iter) + '.')
