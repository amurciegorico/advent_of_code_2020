#!/usr/bin/env python3

import math

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

monster = [(1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11), (1, 12), (2, 13), (2, 16), (1, 17), (1, 18), (0, 18), (1, 19)]


def reverse_string(data):
    reversed_list = list(data)
    reversed_list.reverse()
    return ''.join(reversed_list)


def rotate(data):
    rotated_data = []
    for x in range(len(data[0])):
        new_line = []
        for y in range(len(data) - 1, -1, -1):
            new_line.append(data[y][x])
        rotated_data.append(new_line)
    return rotated_data


def flip(data, type):
    oriented_data = data.copy()
    if type == 1 or type == 3:
        for line in oriented_data:
            line.reverse()
    if type == 2 or type == 3:
        oriented_data.reverse()
    return oriented_data


class Tile:
    borders = []
    border_options = []
    id = 0
    orientation = 0
    flip = 0
    data = []

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def parse_data(self, data):
        self.id = data[0]
        self.data = data[1]
        self.borders = [[], [], [], []]
        top_border = data[1][0].replace('#', '1').replace('.', '0')
        bottom_border = data[1][-1].replace('#', '1').replace('.', '0')
        left_border = ''.join([line[0] for line in data[1]]).replace('#', '1').replace('.', '0')
        right_border = ''.join([line[-1] for line in data[1]]).replace('#', '1').replace('.', '0')
        reversed_top_border = reverse_string(top_border)
        reversed_bottom_border = reverse_string(bottom_border)
        reversed_left_border = reverse_string(left_border)
        reversed_right_border = reverse_string(right_border)
        self.border_options = [top_border, bottom_border, left_border, right_border, reversed_top_border, reversed_bottom_border, reversed_left_border, reversed_right_border]
        self.borders[0].append([int(top_border, 2), int(right_border, 2), int(bottom_border, 2), int(left_border, 2)])
        self.borders[0].append([int(reversed_top_border, 2), int(left_border, 2), int(reversed_bottom_border, 2), int(right_border, 2)])
        self.borders[0].append([int(bottom_border, 2), int(reversed_right_border, 2), int(top_border, 2), int(reversed_left_border, 2)])
        self.borders[0].append([int(reversed_bottom_border, 2), int(reversed_left_border, 2), int(reversed_top_border, 2), int(reversed_right_border, 2)])

        self.borders[1].append([int(reversed_left_border, 2), int(top_border, 2), int(reversed_right_border, 2), int(bottom_border, 2)])
        self.borders[1].append([int(reversed_right_border, 2), int(reversed_top_border, 2), int(reversed_left_border, 2), int(reversed_bottom_border, 2)])
        self.borders[1].append([int(left_border, 2), int(bottom_border, 2), int(right_border, 2), int(top_border, 2)])
        self.borders[1].append([int(right_border, 2), int(reversed_bottom_border, 2), int(left_border, 2), int(reversed_top_border, 2)])

        self.borders[2].append([int(reversed_bottom_border, 2), int(reversed_left_border, 2), int(reversed_top_border, 2), int(reversed_right_border, 2)])
        self.borders[2].append([int(bottom_border, 2), int(reversed_right_border, 2), int(top_border, 2), int(reversed_left_border, 2)])
        self.borders[2].append([int(reversed_top_border, 2), int(left_border, 2), int(reversed_bottom_border, 2), int(right_border, 2)])
        self.borders[2].append([int(top_border, 2), int(right_border, 2), int(bottom_border, 2), int(left_border, 2)])

        self.borders[3].append([int(right_border, 2), int(reversed_bottom_border, 2), int(left_border, 2), int(reversed_top_border, 2)])
        self.borders[3].append([int(left_border, 2), int(bottom_border, 2), int(right_border, 2), int(top_border, 2)])
        self.borders[3].append([int(reversed_right_border, 2), int(reversed_top_border, 2), int(reversed_left_border, 2), int(reversed_bottom_border, 2)])
        self.borders[3].append([int(reversed_left_border, 2), int(top_border, 2), int(reversed_right_border, 2), int(bottom_border, 2)])

    def set_configuration(self, orientation, flip):
        self.orientation = orientation
        self.flip = flip

    def get_border(self, border_id):
        return self.borders[self.orientation][self.flip][border_id]

    def __remove_borders(self, data):
        new_data = []
        for y in range(1, len(data) - 1):
            new_line = []
            for x in range(1, len(data[0]) - 1):
                new_line.append(data[y][x])
            new_data.append(new_line)
        return new_data

    def get_oriented_data(self):
        oriented_data = [list(line) for line in self.data]
        oriented_data = flip(oriented_data, self.flip)
        for rotate_rounds in range(self.orientation):
            oriented_data = rotate(oriented_data)
        return self.__remove_borders(oriented_data)


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


def is_corner(position, size_length):
    return position == (0, 0) or \
            position == (0, size_length - 1) or \
            position == (size_length - 1, 0) or \
            position == (size_length - 1, size_length - 1)


def is_side(position, size_length):
    return position[0] == 0 or \
            position[1] == 0 or \
            position[0] == size_length - 1 or \
            position[1] == size_length - 1


def copy_and_remove(tiles, tile):
    new_tiles = tiles.copy()
    new_tiles.remove(tile)
    return new_tiles


def build_tile_picture(position, board, corner_tiles, side_tiles, center_tiles, size_length):
    if is_corner(position, size_length):
        for corner_tile in corner_tiles:
            for orientation in range(4):
                for flip in range(4):
                    corner_tile.set_configuration(orientation, flip)
                    if position == (0, 0):
                        board[position] = corner_tile
                        unused_tiles_copy = copy_and_remove(corner_tiles, corner_tile)
                        if build_tile_picture((0, 1), board, unused_tiles_copy, side_tiles, center_tiles, size_length):
                            return True
                    elif position == (0, size_length - 1):
                        if board[(0, size_length - 2)].get_border(RIGHT) == corner_tile.get_border(LEFT):
                            board[position] = corner_tile
                            unused_tiles_copy = copy_and_remove(corner_tiles, corner_tile)
                            if build_tile_picture((1, 0), board, unused_tiles_copy, side_tiles, center_tiles, size_length):
                                return True
                    elif position == (size_length - 1, 0):
                        if board[(size_length - 2, 0)].get_border(BOTTOM) == corner_tile.get_border(TOP):
                            board[position] = corner_tile
                            unused_tiles_copy = copy_and_remove(corner_tiles, corner_tile)
                            if build_tile_picture((size_length - 1, 1), board, unused_tiles_copy, side_tiles, center_tiles, size_length):
                                return True
                    else:
                        if board[(size_length - 1, size_length - 2)].get_border(RIGHT) == corner_tile.get_border(LEFT) and \
                                board[(size_length - 2, size_length - 1)].get_border(BOTTOM) == corner_tile.get_border(TOP):
                            board[position] = corner_tile
                            return True
    elif is_side(position, size_length):
        for side_tile in side_tiles:
            for orientation in range(4):
                for flip in range(4):
                    side_tile.set_configuration(orientation, flip)
                    if position[0] == 0:
                        if board[(0, position[1] - 1)].get_border(RIGHT) == side_tile.get_border(LEFT):
                            board[position] = side_tile
                            unused_tiles_copy = copy_and_remove(side_tiles, side_tile)
                            next_position = (0, position[1] + 1) if (position[1] + 1) < size_length else (1, 0)
                            if build_tile_picture(next_position, board, corner_tiles, unused_tiles_copy, center_tiles, size_length):
                                return True
                    elif position[1] == 0:
                        if board[(position[0] - 1, 0)].get_border(BOTTOM) == side_tile.get_border(TOP):
                            board[position] = side_tile
                            unused_tiles_copy = copy_and_remove(side_tiles, side_tile)
                            if build_tile_picture((position[0], 1), board, corner_tiles, unused_tiles_copy, center_tiles, size_length):
                                return True
                    else:
                        if board[(position[0], position[1] - 1)].get_border(RIGHT) == side_tile.get_border(LEFT) and \
                                board[(position[0] - 1, position[1])].get_border(BOTTOM) == side_tile.get_border(TOP):
                            board[position] = side_tile
                            unused_tiles_copy = copy_and_remove(side_tiles, side_tile)
                            next_position = (position[0], position[1] + 1) if (position[1] + 1) < size_length else (position[0] + 1, 0)
                            if build_tile_picture(next_position, board, corner_tiles, unused_tiles_copy, center_tiles, size_length):
                                return True
    else:
        for center_tile in center_tiles:
            for orientation in range(4):
                for flip in range(4):
                    center_tile.set_configuration(orientation, flip)
                    if board[(position[0], position[1] - 1)].get_border(RIGHT) == center_tile.get_border(LEFT) and \
                            board[(position[0] - 1, position[1])].get_border(BOTTOM) == center_tile.get_border(TOP):
                        board[position] = center_tile
                        unused_tiles_copy = copy_and_remove(center_tiles, center_tile)
                        next_position = (position[0], position[1] + 1) if (position[1] + 1) < size_length else (position[0] + 1, 0)
                        if build_tile_picture(next_position, board, corner_tiles, side_tiles, unused_tiles_copy, size_length):
                            return True
    return False


def build_picture(tile_picture, size_length):
    tile_data = tile_picture[(0, 0)].get_oriented_data()
    raw_picture = [[] for i in range(len(tile_data) * size_length)]
    for tile_y in range(size_length):
        for tile_x in range(size_length):
            tile_data = tile_picture[(tile_y, tile_x)].get_oriented_data()
            for y in range(len(tile_data)):
                for x in range(len(tile_data[0])):
                    raw_picture[y + tile_y * len(tile_data)].append(tile_data[y][x])
    return raw_picture


def check_monster_in_area(x, y, raw_picture):
    for monster_part in monster:
        if raw_picture[y + monster_part[0]][x + monster_part[1]] != '#':
            return False
    for monster_part in monster:
        raw_picture[y + monster_part[0]][x + monster_part[1]] = '.'
    return True


def look_for_monsters(raw_picture):
    picture = raw_picture.copy()
    monster_width = 20
    monster_height = 3
    monsters = 0
    y = 0
    while y < len(picture) - monster_height:
        x = 0
        while x < len(picture[0]) - monster_width:
            if check_monster_in_area(x, y, picture):
                monsters += 1
            x += 1
        y += 1
    return monsters, picture


def look_for_monsters_in_all_orientations(raw_picture):
    for flips in range(4):
        picture_to_test = flip(raw_picture, flips)
        for _ in range(4):
            picture_to_test = rotate(picture_to_test)
            monsters, picture = look_for_monsters(picture_to_test)
            if monsters > 0:
                return picture


def determine_water_roughness(picture):
    tiles = 0
    for line in picture:
        tiles += line.count('#')
    return tiles


with open("./data/data1") as file:
    tiles = parse_data(file.readlines())
    size_length = int(math.sqrt(len(tiles)))
    corner_tiles = []
    side_tiles = []
    center_tiles = []
    for tile in tiles:
        found_borders = set()
        for tile_to_check in tiles:
            if tile.id == tile_to_check.id:
                continue
            for border in tile.border_options:
                if border in tile_to_check.border_options:
                    found_borders.add(border)
        if len(found_borders) == 4:
            corner_tiles.append(tile)
        elif len(found_borders) == 6:
            side_tiles.append(tile)
        else:
            center_tiles.append(tile)
    tile_picture = {}
    found = build_tile_picture((0, 0), tile_picture, corner_tiles, side_tiles, center_tiles, size_length)
    raw_picture = build_picture(tile_picture, size_length)
    edited_picture = look_for_monsters_in_all_orientations(raw_picture)
    print(determine_water_roughness(edited_picture))
