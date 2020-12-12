#!/usr/bin/env python3

def count_occupied_adjacent_seats(x, y, seat_map):
    occupied = 0
    start_y = y - 1 if y - 1 >= 0 else 0
    end_y = y + 2 if y + 2 <= len(seat_map) else len(seat_map)
    for y_pos in range(start_y, end_y):
        start_x = x - 1 if x - 1 >= 0 else 0
        end_x = x + 2 if x + 2 <= len(seat_map[0]) else len(seat_map[0])
        for x_pos in range(start_x, end_x):
            if x_pos == x and y_pos == y:
                continue
            if seat_map[y_pos][x_pos] == '#':
                occupied += 1
    return occupied


def simulate_one_step(in_map):
    out_map = []
    for y, in_row in enumerate(in_map):
        out_row = ''
        for x, in_seat in enumerate(in_row):
            if in_seat == 'L':
                out_row += '#' if count_occupied_adjacent_seats(x, y, in_map) == 0 else 'L'
            elif in_seat == '#':
                out_row += 'L' if count_occupied_adjacent_seats(x, y, in_map) >= 4 else '#'
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
