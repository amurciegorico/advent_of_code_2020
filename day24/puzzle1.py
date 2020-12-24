#!/usr/bin/env python3

with open("./data/data1") as file:
    used_tiles = {}
    for line in file.readlines():
        index = 0
        current_tile = (0, 0)
        while index < len(line[:-1]):
            if line[index] == 'e':
                current_tile = (current_tile[0] - 1, current_tile[1])
            elif line[index] == 'w':
                current_tile = (current_tile[0] + 1, current_tile[1])
            elif line[index] == 's':
                index += 1
                if line[index] == 'e':
                    if current_tile[1] % 2 == 0:
                        current_tile = (current_tile[0] - 1, current_tile[1] + 1)
                    else:
                        current_tile = (current_tile[0], current_tile[1] + 1)
                elif line[index] == 'w':
                    if current_tile[1] % 2 == 0:
                        current_tile = (current_tile[0], current_tile[1] + 1)
                    else:
                        current_tile = (current_tile[0] + 1, current_tile[1] + 1)
            elif line[index] == 'n':
                index += 1
                if line[index] == 'e':
                    if current_tile[1] % 2 == 0:
                        current_tile = (current_tile[0] - 1, current_tile[1] - 1)
                    else:
                        current_tile = (current_tile[0], current_tile[1] - 1)
                elif line[index] == 'w':
                    if current_tile[1] % 2 == 0:
                        current_tile = (current_tile[0], current_tile[1] - 1)
                    else:
                        current_tile = (current_tile[0] + 1, current_tile[1] - 1)
            index += 1
        if current_tile in used_tiles:
            used_tiles[current_tile] = 0 if used_tiles[current_tile] == 1 else 1
        else:
            used_tiles[current_tile] = 1
    import functools
    import operator
    print(functools.reduce(operator.add, used_tiles.values()))
