#!/usr/bin/env python3

with open("./data/data1") as file:
    file_data = file.readlines()
    earliest_time = int(file_data[0])
    bus_ids = set(file_data[1][:-1].split(','))
    bus_ids.remove('x')
    bus_ids = [int(num) for num in bus_ids]
    earliest_bus = ()
    for bus_id in bus_ids:
        time_to_wait = bus_id - (earliest_time % bus_id)
        if earliest_bus == () or earliest_bus[1] > time_to_wait:
            earliest_bus = (bus_id, time_to_wait)
    print(earliest_bus[0] * earliest_bus[1])
