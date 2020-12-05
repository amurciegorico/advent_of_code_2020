#!/usr/bin/env python3

def get_seat_id(seat_data):
    binary_data = seat_data.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(binary_data, 2)


file = open("./data/data1", "r")
seats_data = file.readlines()

highest_seat_id = 0
for seat_data in seats_data:
    seat_id = get_seat_id(seat_data)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)
