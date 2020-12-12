#!/usr/bin/env python3

def inside_map(x, y, seat_map):
    return 0 <= x < len(seat_map[0]) and 0 <= y < len(seat_map)


def occupied_visible_seat(x, y, seat_map, direction):
    x += direction[0]
    y += direction[1]
    while inside_map(x, y, seat_map):
        if seat_map[y][x] == '#':
            return True
        elif seat_map[y][x] == 'L':
            return False
        x += direction[0]
        y += direction[1]
    return False


def count_occupied_visible_seats(x, y, seat_map):
    occupied = 0
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for direction in directions:
        occupied += 1 if occupied_visible_seat(x, y, seat_map, direction) else 0
    return occupied


def simulate_one_step(in_map):
    out_map = []
    for y, in_row in enumerate(in_map):
        out_row = ''
        for x, in_seat in enumerate(in_row):
            if in_seat == 'L':
                out_row += '#' if count_occupied_visible_seats(x, y, in_map) == 0 else 'L'
            elif in_seat == '#':
                out_row += 'L' if count_occupied_visible_seats(x, y, in_map) >= 5 else '#'
            else:
                out_row += in_seat
        out_map.append(out_row)
    return out_map


with open("./data/data1") as file:
    seat_map = [row[:-1] for row in file]
    old_seat_map = []
    while seat_map != old_seat_map:
        old_seat_map = seat_map
        seat_map = simulate_one_step(old_seat_map)
    print(''.join(seat_map).count('#'))
