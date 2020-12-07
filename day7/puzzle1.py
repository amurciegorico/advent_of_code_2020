#!/usr/bin/env python3

def parse_rule(rule_data):
    container_and_contained = rule_data.split('contain ')
    container = container_and_contained[0][:-6]
    contained = []
    if container_and_contained[1][:-1] != 'no other bags.':
        contains = container_and_contained[1][:-2].split(', ')
        for contained_bag in contains:
            bag_data = contained_bag.split(' ')
            contained.append(bag_data[1] + ' ' + bag_data[2])
    return container, contained


def contains_bag(contained, container, rules):
    rule_contained = rules[container]
    if contained in rule_contained:
        return True
    for new_container in rule_contained:
        if contains_bag(contained, new_container, rules):
            return True
    return False


file = open("./data/data1", "r")
rules_data = file.readlines()

rules = {}
for rule_data in rules_data:
    rule = parse_rule(rule_data)
    rules[rule[0]] = rule[1]

number_of_bags = 0
for bag in rules:
    if contains_bag('shiny gold', bag, rules):
        number_of_bags += 1

print(number_of_bags)
