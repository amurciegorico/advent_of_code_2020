#!/usr/bin/env python3

def is_sum(number, options):
    option2_start_index = 1
    for option1 in options:
        option1_value = int(option1)
        for option2 in options[option2_start_index:]:
            if number == (option1_value + int(option2)):
                return True
        option2_start_index += 1
    return False


def find_set_range(number, options):
    for option1_index, option1 in enumerate(options):
        for option2_index, option2 in enumerate(options[option1_index + 1:]):
            numbers_range = options[option1_index:option2_index + 1]
            if len(numbers_range) > 1:
                import functools
                if number == functools.reduce(lambda num1, num2: int(num1) + int(num2), numbers_range):
                    return numbers_range
    return []


def string_list_to_int(string_list):
    int_list = []
    for item in string_list:
        int_list.append(int(item))
    return int_list


file = open("./data/data1", "r")
numbers = file.readlines()

number_index = 25
for number in numbers[25:]:
    if not is_sum(int(number), numbers[number_index - 25:number_index]):
        numbers_range = find_set_range(int(number), numbers)
        if len(numbers_range) > 1:
            ints_range = string_list_to_int(numbers_range)
            ints_range.sort()
            print(ints_range[0] + ints_range[-1])
        break
    number_index += 1
