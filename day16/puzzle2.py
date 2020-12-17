#!/usr/bin/env python3

def parse_rule(data):
    split_data = [tmp_data.split('-') for tmp_data in data.split(': ')[1].split(' or ')]
    return (int(split_data[0][0]), int(split_data[0][1])), (int(split_data[1][0]), int(split_data[1][1]))


def parse_ticket(data):
    return [int(num) for num in data.split(',')]


def validate_rule(value, rule):
    return rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]


def validate(value, rules):
    for rule in rules:
        if validate_rule(value, rule):
            return True
    return False


def validate_ticket(ticket, rules):
    for value in ticket:
        if not validate(value, rules):
            return False
    return True


def find_one_possible_rule_field(fields):
    for index, field in enumerate(fields):
        if len(field) == 1:
            return index


def remove_rule(fields, rule):
    for field in fields:
        if rule in field:
            field.remove(rule)


def parse_file_data(file_data):
    departure_indices = []
    rules = []
    my_ticket = []
    tickets = []
    state = 0
    rules_index = 0
    for line in file_data:
        if line == 'your ticket:\n' or line == 'nearby tickets:\n':
            continue
        if line == '\n':
            state += 1
            continue
        if state == 0:
            if line.split(' ')[0] == 'departure':
                departure_indices.append(rules_index)
            rules.append(parse_rule(line))
            rules_index += 1
        elif state == 1:
            my_ticket = parse_ticket(line)
        else:
            tickets.append(parse_ticket(line))
    return rules, my_ticket, tickets, departure_indices


with open("./data/data1") as file:
    file_data = file.readlines()
    rules, my_ticket, tickets, departure_indices = parse_file_data(file_data)
    valid_tickets = [my_ticket]
    for ticket in tickets:
        if validate_ticket(ticket, rules):
            valid_tickets.append(ticket)
    fields = []
    for field in range(len(my_ticket)):
        fields.append(list(range(len(rules))))
    for ticket in valid_tickets:
        for field_index, field in enumerate(ticket):
            for rule_index, rule in enumerate(rules):
                if not validate_rule(field, rule):
                    if rule_index in fields[field_index]:
                        fields[field_index].remove(rule_index)
    fields_width_rules = {}
    final_value = 1
    while len(fields_width_rules) < len(fields):
        field = find_one_possible_rule_field(fields)
        rule = fields[field][0]
        fields_width_rules[rule] = field
        remove_rule(fields, rule)
        if rule in departure_indices:
            final_value *= my_ticket[field]
    print(final_value)
