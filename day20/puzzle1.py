#!/usr/bin/env python3

def reverse_string(data):
    reversed_list = list(data)
    reversed_list.reverse()
    return ''.join(reversed_list)


class Tile:
    borders = []
    id = 0

    def parse_data(self, data):
        self.id = data[0]
        top_border = data[1][0].replace('#', '1').replace('.', '0')
        bottom_border = data[1][-1].replace('#', '1').replace('.', '0')
        left_border = ''.join([line[0] for line in data[1]]).replace('#', '1').replace('.', '0')
        right_border = ''.join([line[-1] for line in data[1]]).replace('#', '1').replace('.', '0')
        reversed_top_border = reverse_string(top_border)
        reversed_bottom_border = reverse_string(bottom_border)
        reversed_left_border = reverse_string(left_border)
        reversed_right_border = reverse_string(right_border)
        self.borders = [top_border, bottom_border, left_border, right_border, reversed_top_border, reversed_bottom_border, reversed_left_border, reversed_right_border]


def parse_data(data):
    tiles = []
    current_tile = ()
    for line in data:
        if line[0] == 'T':
            current_tile = (int(line[5:-2]), [])
        elif line == '\n':
            tile_object = Tile()
            tile_object.parse_data(current_tile)
            tiles.append(tile_object)
        else:
            current_tile[1].append(line[:-1])
    return tiles


with open("./data/data1") as file:
    tiles = parse_data(file.readlines())
    corners = []
    for tile in tiles:
        found_borders = set()
        for tile_to_check in tiles:
            if tile.id == tile_to_check.id:
                continue
            for border in tile.borders:
                if border in tile_to_check.borders:
                    found_borders.add(border)
        if len(found_borders) == 4:
            corners.append(tile.id)
    import functools
    print(functools.reduce(lambda a, b: a * b, corners))
