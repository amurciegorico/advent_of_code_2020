#!/usr/bin/env python3

def parse_data(data):
    rules = {}
    messages = []
    for index, line in enumerate(data):
        if line == '\n':
            messages = [message[:-1] for message in data[index + 1:]]
            break
        split_line = line[:-1].split(': ')
        rules[split_line[0]] = [sub_rule.split(' ') for sub_rule in split_line[1].split(' | ')]
    return rules, messages


def merge_messages(messages1, messages2):
    messages = []
    for message1 in messages1:
        for message2 in messages2:
            messages.append(message1 + message2)
    return messages


def generate_all_messages(rule_index, rules):
    messages = []
    for sub_rule in rules[rule_index]:
        sub_messages = ['']
        for rule_part in sub_rule:
            if rule_part.isdecimal():
                sub_messages = merge_messages(sub_messages, generate_all_messages(rule_part, rules))
            else:
                sub_messages = merge_messages(sub_messages, [rule_part[1]])
        for sub_message in sub_messages:
            messages.append(sub_message)
    return messages


with open("./data/data1") as file:
    rules, messages = parse_data(file.readlines())
    rule_messages = generate_all_messages('0', rules)
    number_messages = 0
    for message in messages:
        if message in rule_messages:
            number_messages += 1
    print(number_messages)
