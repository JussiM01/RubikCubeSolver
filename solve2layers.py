from solvecorners import *

left_c_pairs = [('r', 'g'), ('g', 'o'), ('o', 'b'), ('b', 'r')]
right_c_pairs = [('g', 'o'), ('o', 'b'), ('b', 'r'), ('r', 'g')]
outer_colors = ['g', 'o', 'b', 'r']

middle_edges = {((10, 9, 0), (9, 10, 0)), ((-9, 10, 0), (-10, 9, 0)),
    ((-10, -9, 0), (-9, -10, 0,)), ((9, -10, 0), (10, -9, 0))}
outer_faces = {p for p in points if p[z] not in [-10, 10]}

upside_down = turn(start_cube, x, 180)

def outer_color_fits(cube, edge, order):
    return ({cube[face] for face in edge if face in outer_faces[order]}
        == {outer_colors[order]})

def correct_middle_edge(cube, edge, order):
    return {cube[face] == upside_down[face] for face in edge} == {True}

def edge_to_middle(cube, edge, order):
    rot_sequence1 = (['U'] + side_rot[order - 4] + ['Ui'] + side_inv[order - 4]
        + ['Ui'] + side_inv[order] + ['U'] + side_rot[order])
    rot_sequence2 = (['Ui'] + side_inv[order - 1] + ['U'] + side_rot[order - 1]
        + ['U'] + side_rot[order] + ['Ui'] side_inv[order])
    tmp1, tmp2 = rotate(cube, rot_sequence1), rotate(cube, rot_sequence2)
    if correct_middle_edge(tmp1, edge, order): return (tmp1, rot_sequence1)
    if correct_middle_edge(tmp2, edge, order): return (tmp2, rot_sequence2)

def middle_edge_up(cube, edge):
    n = middle_edges.index(edge)
    rot_sequence = (['U'] + side_rot[n - 4] + ['Ui'] + side_inv[n - 4]
        + ['Ui'] + side_inv[n] + ['U'] + side_rot[n])
    return (rotate(cube, rot_sequence), rot_sequence)

def place_middle_edges(cube, order):
    new_cube, rotations = cube, []
    for edge in top_edges:
        if outer_color_fits(new_cube, edge, order):
            res1 = edge_to_middle(new_cube, edge, order)
            new_cube = res1[0]
            rotations += res1[1]
    for edge in middle_edges:
        if outer_color_fits(new_cube, edge, order):
            if not correct_middle_edge(new_cube, edge):
                res2 = middle_edge_up(new_cube, edge, order)
                new_cube = res2[0]
                rotations += res2[1]
    for edge in top_edges:
        if outer_color_fits(new_cube, edge, order):
            res3 = edge_to_middle(new_cube, edge, order)
            new_cube = res3[0]
            rotations += res3[1]
    return (new_cube, rotations)

def make_a_2nd_layer(cube):
    new_cube, rotations1 = make_a_top_layer(cube)
    new_cube, rotations2 = turn(new_cube, x, 180), []
    for order in range(4):
        res = place_middle_edges(new_cube, order)
        new_cube = res[0]
        rotations2 += res[1]
    return (new_cube, rotations1, rotations2)

# TODO: Test and debug.
