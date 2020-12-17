#!/usr/bin/env python3

def parse_rule(data):
    split_data = [tmp_data.split('-') for tmp_data in data.split(': ')[1].split(' or ')]
    return (int(split_data[0][0]), int(split_data[0][1])), (int(split_data[1][0]), int(split_data[1][1]))


def parse_ticket(data):
    return [int(num) for num in data.split(',')]


def validate(value, rules):
    for rule in rules:
        if rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]:
            return True
    return False


with open("./data/data1") as file:
    file_data = file.readlines()
    rules = []
    my_ticket = []
    tickets = []
    state = 0
    for line in file_data:
        if line == 'your ticket:\n' or line == 'nearby tickets:\n':
            continue
        if line == '\n':
            state += 1
            continue
        if state == 0:
            rules.append(parse_rule(line))
        elif state == 1:
            my_ticket = parse_ticket(line)
        else:
            tickets.append(parse_ticket(line))
    ticket_scanning_error_rate = 0
    for ticket in tickets:
        for value in ticket:
            if not validate(value, rules):
                ticket_scanning_error_rate += value

    print(ticket_scanning_error_rate)
