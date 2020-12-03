#!/usr/bin/env python3

def add(vec1, vec2):
    vec1[0] += vec2[0]
    vec1[1] += vec2[1]
    return vec1


def count_trees(slope, terrain):
    position = [0, 0]
    trees = 0

    position = add(position, slope)

    while position[1] < len(terrain):
        position[0] = position[0] % (len(terrain[0]) - 1)
        if terrain[position[1]][position[0]] == '#':
            trees += 1
        position = add(position, slope)

    return trees


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

file = open("./data/data1", "r")
terrain = file.readlines()

multiplied_trees = 1

for slope in slopes:
    multiplied_trees *= count_trees(slope, terrain)

print(multiplied_trees)
