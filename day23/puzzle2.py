#!/usr/bin/env python3

input_data = '487912365'
moves = 10000000


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.destination_node = None


def build_linked_list(cups_list, max_cup, min_cup):
    first_data = cups_list[0]
    first_node = Node(first_data)
    nodes_dictionary = {first_data: first_node}
    previous_node = first_node
    current_node = None
    for current_data in cups_list[1:]:
        current_node = Node(current_data)
        nodes_dictionary[current_data] = current_node
        previous_node.next = current_node
        previous_node = current_node
    current_node.next = first_node
    current_node = first_node.next
    while current_node != first_node:
        destination_index = current_node.data - 1 if current_node.data - 1 >= min_cup else max_cup
        current_node.destination_node = nodes_dictionary[destination_index]
        current_node = current_node.next
    destination_index = first_node.data - 1 if first_node.data - 1 >= min_cup else max_cup
    first_node.destination_node = nodes_dictionary[destination_index]
    return first_node


def simulate_one_step(first_node):
    first_to_move = first_node.next
    nodes_to_move = [first_to_move, first_to_move.next, first_to_move.next.next]
    destination_node = first_node.destination_node
    while destination_node in nodes_to_move:
        destination_node = destination_node.destination_node
    first_node.next = first_to_move.next.next.next
    first_to_move.next.next.next = destination_node.next
    destination_node.next = first_to_move
    return first_node.next


cups = [int(cup) for cup in list(input_data)]
cups.extend([num for num in range(len(cups) + 1, 1000001)])
max_cup = max(cups)
min_cup = min(cups)
cups_first_node = build_linked_list(cups, max_cup, min_cup)
for index in range(moves):
    cups_first_node = simulate_one_step(cups_first_node)
while cups_first_node.data != 1:
    cups_first_node = cups_first_node.next
print(cups_first_node.next.data * cups_first_node.next.next.data)
