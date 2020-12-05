#!/usr/bin/env python3

def get_seat_id(seat_data):
    binary_data = seat_data.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(binary_data, 2)


def find_seat(seat_ids):
    seat_ids.sort()
    previous_seat_id = seat_ids[0] - 1
    for seat_id in seat_ids:
        if seat_id != (previous_seat_id + 1):
            return seat_id - 1
        previous_seat_id = seat_id
    return -1


file = open("./data/data1", "r")
seats_data = file.readlines()

seat_ids = []
for seat_data in seats_data:
    seat_ids.append(get_seat_id(seat_data))
seat = find_seat(seat_ids)

print(seat)
