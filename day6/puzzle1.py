#!/usr/bin/env python3

def count_yes_answers(group_data):
    return len(set(group_data))


file = open("./data/data1", "r")
customs_data = file.readlines()
customs_data.append('\n')

total_yes_answers = 0
current_group_data = ""
for person_data in customs_data:
    if person_data == '\n':
        total_yes_answers += count_yes_answers(current_group_data)
        current_group_data = ""
    else:
        current_group_data += person_data[:-1]

print(total_yes_answers)
