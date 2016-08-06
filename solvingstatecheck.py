from rotationtest import *
from rubiksolver import *

def all_same(cube, coordinate_set):
    return len({cube[p] for p in coordinate_set}) == 1

def check_top_state(cube, state):
    return {all_same(cube, coord_set) for coord_set in state} == {True}

top_cross = [{(i, 0, 10) for i in ps } | {(0, j, 10) for j in ps},
    {(10, 0, 9), (10, 0, 0)}, {(-10, 0, 9), (-10, 0, 0)},
    {(0, -9, 9), (0, -9, 0)},  {(0, 9, 9), (0, 9, 0)}]

top_layer = [set(top_side), {(10, j, 9) for j in ps}, {(-10, j, 9) for j in ps},
    {(i, -10, 9) for i in ps}, {(i, 10, 9) for i in ps}]

top_2_layers = [set(top_side), {(10, j, k) for j in ps for k in [0, 9]},
    {(-10, j, k) for j in ps for k in [0, 9]},
    {(i, -10, k) for i in ps for k in [0, 9]},
    {(i, 10, k) for i in ps for k in [0, 9]}]

solved_cube = [set(s) for s in sides]

top_states = [top_cross, top_layer, top_2_layers, solved_cube]
