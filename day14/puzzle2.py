#!/usr/bin/env python3

def parse_mask(data):
    return data.split(' = ')[1][:-1]


def parse_mem(data):
    split_data = data.split(' = ')
    return int(split_data[0][4:-1]), int(split_data[1][:-1])


def apply_mask(value, mask):
    value_str = '{0:036b}'.format(value)
    results = ['']
    for bit_position, mask_value in enumerate(mask):
        value = value_str[bit_position] if mask_value == '0' else mask_value
        new_results = []
        for result in results:
            if value == 'X':
                new_results.append(result + '0')
                new_results.append(result + '1')
            else:
                new_results.append(result + value)
        results = new_results
    return results


with open("./data/data1") as file:
    file_data = file.readlines()
    memory = {}
    current_mask = ''
    for line in file_data:
        if line[1] == 'e':
            data = parse_mem(line)
            addresses = apply_mask(data[0], current_mask)
            for address in addresses:
                memory[int(address, 2)] = data[1]
        else:
            current_mask = parse_mask(line)
    import functools
    values_sum = functools.reduce(lambda a, b: a + b, memory.values())
    print(values_sum)
