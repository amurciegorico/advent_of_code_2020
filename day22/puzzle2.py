#!/usr/bin/env python3

import copy


def parse_decks(data):
    decks = []
    current_deck = []
    for line in data:
        if line[0] == 'P':
            current_deck = []
        elif line == '\n':
            decks.append(current_deck)
        else:
            current_deck.append(int(line))
    decks.append(current_deck)
    return decks


def simulate_game(decks):
    configurations = []
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        if decks in configurations:
            return 0
        configurations.append(copy.deepcopy(decks))
        card0 = decks[0].pop(0)
        card1 = decks[1].pop(0)
        if card0 <= len(decks[0]) and card1 <= len(decks[1]):
            new_decks = [decks[0][0:card0], decks[1][0:card1]]
            if simulate_game(new_decks) == 0:
                decks[0].extend([card0, card1])
            else:
                decks[1].extend([card1, card0])
        else:
            if card0 > card1:
                decks[0].extend([card0, card1])
            else:
                decks[1].extend([card1, card0])
    return 1 if len(decks[1]) > len(decks[0]) else 0


def calculate_score(deck):
    points = 0
    for index, card in enumerate(deck):
        points += (len(deck) - index) * card
    return points


with open("./data/data1") as file:
    decks = parse_decks(file.readlines())
    winner = simulate_game(decks)
    print(calculate_score(decks[winner]))
