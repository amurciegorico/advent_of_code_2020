#!/usr/bin/env python3

def is_valid_passport(passport_fields):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport_fields:
            return False
    return True


def extract_passport_fields(passport_data):
    passport_fields = []
    for line_data in passport_data:
        for field_data in line_data.split(" "):
            field = field_data.split(":")
            passport_fields.append(field[0])
    return passport_fields


file = open("./data/data1", "r")
passports_data = file.readlines()
passports_data.append('\n')

valid_passports = 0
current_passport_data = []
for line_data in passports_data:
    if line_data == '\n':
        passport_fields = extract_passport_fields(current_passport_data)
        if is_valid_passport(passport_fields):
            valid_passports += 1
        current_passport_data = []
    else:
        current_passport_data.append(line_data)

print(valid_passports)
