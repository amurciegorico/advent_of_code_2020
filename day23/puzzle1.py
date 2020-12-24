#!/usr/bin/env python3

input_data = '487912365'
moves = 100


def simulate_one_step(cups, max_cup, min_cup):
    current_cup = cups.pop(0)
    next_three_cups = [cups.pop(0), cups.pop(0), cups.pop(0)]
    destination_cup = current_cup - 1
    destination_cup_index = -1
    while destination_cup != current_cup:
        if destination_cup < min_cup:
            destination_cup = max_cup
        if destination_cup in cups:
            destination_cup_index = cups.index(destination_cup)
            break
        destination_cup -= 1
    next_three_cups.reverse()
    for next_cup in next_three_cups:
        cups.insert(destination_cup_index + 1, next_cup)
    cups.append(current_cup)


cups = [int(cup) for cup in list(input_data)]
max_cup = max(cups)
min_cup = min(cups)
for _ in range(moves):
    simulate_one_step(cups, max_cup, min_cup)
next_cups = cups[:cups.index(1)]
cups = cups[cups.index(1) + 1:]
cups.extend(next_cups)
print(''.join([str(cup) for cup in cups]))
