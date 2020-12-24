#!/usr/bin/env python3

def get_tile_coordinate(data):
    index = 0
    current_tile = (0, 0)
    while index < len(data):
        if data[index] == 'e':
            current_tile = (current_tile[0] - 1, current_tile[1])
        elif data[index] == 'w':
            current_tile = (current_tile[0] + 1, current_tile[1])
        elif data[index] == 's':
            index += 1
            if data[index] == 'e':
                if current_tile[1] % 2 == 0:
                    current_tile = (current_tile[0] - 1, current_tile[1] + 1)
                else:
                    current_tile = (current_tile[0], current_tile[1] + 1)
            elif data[index] == 'w':
                if current_tile[1] % 2 == 0:
                    current_tile = (current_tile[0], current_tile[1] + 1)
                else:
                    current_tile = (current_tile[0] + 1, current_tile[1] + 1)
        elif data[index] == 'n':
            index += 1
            if data[index] == 'e':
                if current_tile[1] % 2 == 0:
                    current_tile = (current_tile[0] - 1, current_tile[1] - 1)
                else:
                    current_tile = (current_tile[0], current_tile[1] - 1)
            elif data[index] == 'w':
                if current_tile[1] % 2 == 0:
                    current_tile = (current_tile[0], current_tile[1] - 1)
                else:
                    current_tile = (current_tile[0] + 1, current_tile[1] - 1)
        index += 1
    return current_tile


even_adjacent_tiles = [(-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)]
odd_adjacent_tiles = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (1, 1)]


def count_black_tiles(tile, floor):
    black_tiles = 0
    offsets = even_adjacent_tiles if tile[1] % 2 == 0 else odd_adjacent_tiles
    for offset in offsets:
        test_tile = (tile[0] + offset[0], tile[1] + offset[1])
        if test_tile in floor:
            black_tiles += 1
    return black_tiles


def flip_floor(floor):
    new_floor = []
    checked_tiles = []
    for tile in floor:
        black_tiles = count_black_tiles(tile, floor)
        if black_tiles == 1 or black_tiles == 2:
            new_floor.append(tile)
        offsets = even_adjacent_tiles if tile[1] % 2 == 0 else odd_adjacent_tiles
        for offset in offsets:
            test_tile = (tile[0] + offset[0], tile[1] + offset[1])
            if test_tile not in floor and test_tile not in checked_tiles:
                black_tiles = count_black_tiles(test_tile, floor)
                if black_tiles == 2:
                    new_floor.append(test_tile)
                    checked_tiles.append(test_tile)
    return new_floor


with open("./data/data1") as file:
    floor = []
    for line in file.readlines():
        tile = get_tile_coordinate(line[:-1])
        if tile in floor:
            floor.remove(tile)
        else:
            floor.append(tile)
    for _ in range(100):
        floor = flip_floor(floor)
    print(len(floor))
