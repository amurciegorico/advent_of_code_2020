#!/usr/bin/env python3

import functools


def chinese_reminder_theorem(pairs):
    n = functools.reduce(lambda a, b: a * b, [pair[0] for pair in pairs])
    x = 0
    for pair in pairs:
        bi = pair[1]
        ni = int(n / pair[0])
        num = ni % pair[0]
        xi = 1
        while (xi * num) % pair[0] != 1:
            xi += 1
        x += bi * ni * xi
    return n, x % n


with open("./data/data1") as file:
    file_data = file.readlines()
    bus_ids = file_data[1][:-1].split(',')
    bus_and_minutes = []
    for index, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            bus_and_minutes.append((int(bus_id), index))
    result = chinese_reminder_theorem(bus_and_minutes)
    print(result[0] - result[1])
