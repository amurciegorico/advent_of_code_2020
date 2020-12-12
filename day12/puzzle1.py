#!/usr/bin/env python3

class Boat:
    x = 0
    y = 0
    valid_degrees = [90, 180, 270]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 0

    def __forward(self, value):
        self.x += self.directions[self.direction_index][0] * value
        self.y += self.directions[self.direction_index][1] * value

    def move(self, instruction):
        if instruction[0] == 'N':
            self.y -= instruction[1]
        elif instruction[0] == 'S':
            self.y += instruction[1]
        elif instruction[0] == 'W':
            self.x -= instruction[1]
        elif instruction[0] == 'E':
            self.x += instruction[1]
        elif instruction[0] == 'F':
            self.__forward(instruction[1])
        elif instruction[0] == 'R':
            assert instruction[1] in self.valid_degrees, "Invalid degrees value"
            self.direction_index = int((self.direction_index + instruction[1] / 90) % 4)
        elif instruction[0] == 'L':
            assert instruction[1] in self.valid_degrees, "Invalid degrees value"
            self.direction_index = int((self.direction_index - instruction[1] / 90) % 4)


with open("./data/data1") as file:
    instructions = [(row[0], int(row[1:])) for row in file]
    boat = Boat()
    for instruction in instructions:
        boat.move(instruction)
    print(abs(boat.x) + abs(boat.y))
