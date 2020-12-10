#!/usr/bin/env python3

def string_list_to_int(string_list):
    int_list = []
    for item in string_list:
        int_list.append(int(item))
    return int_list


with open("./data/data1") as file:
    adapters_joltage = string_list_to_int(file.readlines())
    adapters_joltage.append(0)
    adapters_joltage.sort()
    adapters_joltage.append(adapters_joltage[-1] + 3)
    adapters_joltage.reverse()
    leaves_map = {adapters_joltage[0]: 1}
    for index, adapter_joltage in enumerate(adapters_joltage[1:]):
        leaves = 0
        start_index = index - 2
        if start_index < 0:
            start_index = 0
        for next_adapter_joltage in adapters_joltage[start_index:index + 1]:
            if 1 <= (next_adapter_joltage - adapter_joltage) <= 3:
                assert next_adapter_joltage in leaves_map.keys(), "Key not found"
                leaves += leaves_map[next_adapter_joltage]
        leaves_map[adapter_joltage] = leaves
    print(leaves_map[0])
