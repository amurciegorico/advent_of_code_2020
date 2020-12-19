#!/usr/bin/env python3

def load_dimension(data):
    dimension = []
    for y, line in enumerate(data):
        for x, cube in enumerate(line[:-1]):
            if cube == '#':
                dimension.append((x, y, 0, 0))
    return dimension


def simulate_cube(cube, dimension):
    active_neighbors = 0
    for x in range(cube[0] - 1, cube[0] + 2):
        for y in range(cube[1] - 1, cube[1] + 2):
            for z in range(cube[2] - 1, cube[2] + 2):
                for w in range(cube[3] - 1, cube[3] + 2):
                    test_cube = (x, y, z, w)
                    if test_cube == cube:
                        continue
                    if test_cube in dimension:
                        active_neighbors += 1
    if cube in dimension:
        return active_neighbors == 2 or active_neighbors == 3
    else:
        return active_neighbors == 3


def simulate(dimension):
    new_dimension = []
    visited = []
    for cube in dimension:
        for x in range(cube[0] - 1, cube[0] + 2):
            for y in range(cube[1] - 1, cube[1] + 2):
                for z in range(cube[2] - 1, cube[2] + 2):
                    for w in range(cube[3] - 1, cube[3] + 2):
                        test_cube = (x, y, z, w)
                        if test_cube not in visited:
                            if simulate_cube(test_cube, dimension):
                                new_dimension.append(test_cube)
                            visited.append(test_cube)
    return new_dimension


with open("./data/data1") as file:
    dimension = load_dimension(file.readlines())
    for index in range(6):
        new_dimension = simulate(dimension)
        dimension = new_dimension
    print(len(dimension))
