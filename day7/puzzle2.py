#!/usr/bin/env python3

def parse_rule(rule_data):
    container_and_contained = rule_data.split('contain ')
    container = container_and_contained[0][:-6]
    contained = []
    if container_and_contained[1][:-1] != 'no other bags.':
        contains = container_and_contained[1][:-2].split(', ')
        for contained_bag in contains:
            bag_data = contained_bag.split(' ')
            bag_data_parsed = (int(bag_data[0]), bag_data[1] + ' ' + bag_data[2])
            contained.append(bag_data_parsed)
    return container, contained


def get_number_of_bags(bag, rules):
    contained = rules[bag]
    bags = 0
    for bag_data in contained:
        bags += bag_data[0] * (get_number_of_bags(bag_data[1], rules) + 1)
    return bags


file = open("./data/data1", "r")
rules_data = file.readlines()

rules = {}
for rule_data in rules_data:
    rule = parse_rule(rule_data)
    rules[rule[0]] = rule[1]

number_of_bags = get_number_of_bags('shiny gold', rules)

print(number_of_bags)
