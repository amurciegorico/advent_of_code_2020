#!/usr/bin/env python3

def count_yes_answers(group_data):
    intersection_answers = group_data[0]
    for person_data in group_data[1:]:
        intersection_answers &= person_data
    return len(intersection_answers)


file = open("./data/data1", "r")
customs_data = file.readlines()
customs_data.append('\n')

total_yes_answers = 0
current_group_data = []
for person_data in customs_data:
    if person_data == '\n':
        total_yes_answers += count_yes_answers(current_group_data)
        current_group_data = []
    else:
        current_group_data.append(set(person_data[:-1]))

print(total_yes_answers)
