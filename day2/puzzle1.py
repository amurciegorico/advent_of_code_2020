#!/usr/bin/env python3

def valid_password(min_num, max_num, character, password):
    times = password.count(character)
    return min_num <= times <= max_num


file = open("./data/data1", "r")
content = file.readlines()

valid_passwords = 0
for data_to_check in content:
    data = data_to_check.split(" ")
    times_range = data[0].split("-")
    if valid_password(int(times_range[0]), int(times_range[1]), data[1][:-1], data[2]):
        valid_passwords += 1

print(valid_passwords)
