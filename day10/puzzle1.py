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
    adapters_1jolt_diff = 0
    adapters_3jolt_diff = 0
    for index, adapter_joltage in enumerate(adapters_joltage):
        if adapter_joltage != adapters_joltage[-1]:
            jolt_diff = adapters_joltage[index + 1] - adapter_joltage
            if jolt_diff == 1:
                adapters_1jolt_diff += 1
            elif jolt_diff == 3:
                adapters_3jolt_diff += 1
            else:
                assert jolt_diff == 2, "Impossible connection!"
    print(adapters_1jolt_diff * adapters_3jolt_diff)
