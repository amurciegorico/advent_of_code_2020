#!/usr/bin/env python3

def get_key_step(subject_number, value):
    value *= subject_number
    value %= 20201227
    return value


def get_key(subject_number, loop_size):
    key = 1
    for _ in range(loop_size):
        key = get_key_step(subject_number, key)
    return key


def get_encryption_key(public_keys):
    # Assuming that the subject number to get the public key is always 7...
    card_loop_size = 0
    card_key = 1
    while card_key != public_keys[0]:
        card_loop_size += 1
        card_key = get_key_step(7, card_key)
    # Assuming that is only needed to calculate the key for one device because the other must be the same...
    return get_key(public_keys[1], card_loop_size)


with open("./data/data1") as file:
    public_keys = [int(key) for key in file.readlines()]
    encryption_key = get_encryption_key(public_keys)
    print(encryption_key)
