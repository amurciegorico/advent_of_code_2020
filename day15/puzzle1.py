#!/usr/bin/env python3

input_data = '5,1,9,18,13,8,0'

starting_numbers = [int(number) for number in input_data.split(',')]
numbers_said = {}
for index, starting_number in enumerate(starting_numbers[:-1]):
    numbers_said[starting_number] = index

last_number = starting_numbers[-1]
for turn in range(len(starting_numbers), 2020):
    if last_number in numbers_said:
        next_number = turn - 1 - numbers_said[last_number]
    else:
        next_number = 0
    numbers_said[last_number] = turn - 1
    last_number = next_number

print(last_number)
