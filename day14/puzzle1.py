#!/usr/bin/env python3

def parse_mask(data):
    return data.split(' = ')[1][:-1]


def parse_mem(data):
    split_data = data.split(' = ')
    return int(split_data[0][4:-1]), int(split_data[1][:-1])


def apply_mask(value, mask):
    return (value & int(mask.replace('X', '1'), 2)) | int(mask.replace('X', '0'), 2)


with open("./data/data1") as file:
    file_data = file.readlines()
    memory = {}
    current_mask = ''
    for line in file_data:
        if line[1] == 'e':
            data = parse_mem(line)
            memory[data[0]] = apply_mask(data[1], current_mask)
        else:
            current_mask = parse_mask(line)
    import functools
    values_sum = functools.reduce(lambda a, b: a + b, memory.values())
    print(values_sum)
