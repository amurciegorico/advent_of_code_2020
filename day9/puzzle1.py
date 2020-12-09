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


file = open("./data/data1", "r")
numbers = file.readlines()

number_index = 25
for number in numbers[25:]:
    if not is_sum(int(number), numbers[number_index - 25:number_index]):
        print(number)
        break
    number_index += 1
