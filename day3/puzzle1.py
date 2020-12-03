#!/usr/bin/env python3

def add(vec1, vec2):
    vec1[0] += vec2[0]
    vec1[1] += vec2[1]
    return vec1


slope = [3, 1]

file = open("./data/data1", "r")
terrain = file.readlines()

position = [0, 0]
trees = 0

position = add(position, slope)

while position[1] < len(terrain):
    position[0] = position[0] % (len(terrain[0]) - 1)
    if terrain[position[1]][position[0]] == '#':
        trees += 1
    position = add(position, slope)

print(trees)
