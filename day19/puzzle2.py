#!/usr/bin/env python3

def parse_data(data):
    rules = {}
    messages = []
    for index, line in enumerate(data):
        if line == '\n':
            messages = [message[:-1] for message in data[index + 1:]]
            break
        line = '8: 42 ###' if line[:-1] == '8: 42' else line[:-1]
        line = '11: 42 %%% 31' if line == '11: 42 31' else line
        split_line = line.split(': ')
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


def check_8(submessage, rule_messages_42, start):
    if submessage == '':
        return True
    for rule in rule_messages_42:
        new_rule = start + rule
        if submessage == new_rule:
            return True
        if submessage.startswith(new_rule):
            if len(new_rule) < len(submessage):
                if check_8(submessage, rule_messages_42, new_rule):
                    return True
    return False


def check_11(submessage, rule_messages_31, rule_messages_42, center):
    if submessage == '':
        return True
    for rule42 in rule_messages_42:
        for rule31 in rule_messages_31:
            new_rule = rule42 + center + rule31
            if submessage == new_rule:
                return True
            if new_rule in submessage:
                if len(new_rule) < len(submessage):
                    if check_11(submessage, rule_messages_31, rule_messages_42, new_rule):
                        return True
    return False


def check_message(message, rule_message, rule_messages_42, rule_messages_31):
    index_8 = rule_message.find('#')
    index_11 = rule_message.find('%')
    assert index_8 != -1, "Unexpected behaviour"
    assert index_11 != -1, "Unexpected behaviour"
    assert index_8 < index_11, "Unexpected behaviour"
    if message.startswith(rule_message[:index_8]) \
            and message.endswith(rule_message[index_11 + 1:]) \
            and rule_message[index_8 + 1: index_11] in message[index_8:-len(rule_message[index_11 + 1:])]:
        middle_index = message[index_8:-len(rule_message[index_11 + 1:])].find(rule_message[index_8 + 1: index_11])
        while middle_index != -1:
            if check_8(message[index_8:middle_index + index_8], rule_messages_42, '') \
                    and check_11(message[middle_index + index_8 + len(rule_message[index_8 + 1: index_11]):-len(rule_message[index_11 + 1:])], rule_messages_31, rule_messages_42, ''):
                return True
            middle_index = message[index_8:-len(rule_message[index_11 + 1:])].find(rule_message[index_8 + 1: index_11], middle_index + 1)
    return False


with open("./data/data1") as file:
    rules, messages = parse_data(file.readlines())
    rule_messages = generate_all_messages('0', rules)
    rule_messages_42 = generate_all_messages('42', rules)
    rule_messages_31 = generate_all_messages('31', rules)
    number_messages = 0
    for index, message in enumerate(messages):
        for rule_message in rule_messages:
            if check_message(message, rule_message, rule_messages_42, rule_messages_31):
                number_messages += 1
                break
    print(number_messages)
