#!/usr/bin/env python3

def validate_byr(passport):
    return 1920 <= int(passport['byr']) <= 2002


def validate_iyr(passport):
    return 2010 <= int(passport['iyr']) <= 2020


def validate_eyr(passport):
    return 2020 <= int(passport['eyr']) <= 2030


def validate_hgt(passport):
    if passport['hgt'][-2:] == 'cm':
        return 150 <= int(passport['hgt'][:-2]) <= 193
    elif passport['hgt'][-2:] == 'in':
        return 59 <= int(passport['hgt'][:-2]) <= 76
    return False


def validate_hcl(passport):
    if passport['hcl'][0] != '#':
        return False
    for digit in passport['hcl'][1:]:
        import string
        if digit not in string.hexdigits:
            return False
    return True


def validate_ecl(passport):
    return passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(passport):
    return len(passport['pid']) == 9 and passport['pid'].isdigit()


def is_valid_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport_fields = list(passport)
    for field in required_fields:
        if field not in passport_fields:
            return False
    if not validate_byr(passport):
        return False
    if not validate_iyr(passport):
        return False
    if not validate_eyr(passport):
        return False
    if not validate_hgt(passport):
        return False
    if not validate_hcl(passport):
        return False
    if not validate_ecl(passport):
        return False
    if not validate_pid(passport):
        return False
    return True


def build_passport(passport_data):
    passport = {}
    for line_data in passport_data:
        for field_data in line_data.split(" "):
            field = field_data.split(":")
            field[1] = field[1].replace('\n', '')
            passport[field[0]] = field[1]
    return passport


file = open("./data/data1", "r")
passports_data = file.readlines()
passports_data.append('\n')

valid_passports = 0
current_passport_data = []
for line_data in passports_data:
    if line_data == '\n':
        passport = build_passport(current_passport_data)
        if is_valid_passport(passport):
            valid_passports += 1
        current_passport_data = []
    else:
        current_passport_data.append(line_data)

print(valid_passports)
