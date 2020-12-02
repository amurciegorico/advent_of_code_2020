#!/usr/bin/env python3

def valid_password(first_position, second_position, character, password):
    if password[first_position - 1] == character:
        return password[second_position - 1] != character
    else:
        return password[second_position - 1] == character


file = open("./data/data1", "r")
content = file.readlines()

valid_passwords = 0
for data_to_check in content:
    data = data_to_check.split(" ")
    times_range = data[0].split("-")
    if valid_password(int(times_range[0]), int(times_range[1]), data[1][:-1], data[2]):
        valid_passwords += 1

print(valid_passwords)
