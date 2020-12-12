#!/usr/bin/env python3

class Boat:
    x = 0
    y = 0
    waypoint = [10, -1]
    valid_degrees = [90, 180, 270]

    def __turn_left(self):
        self.waypoint = [self.waypoint[1], -self.waypoint[0]]

    def __turn_right(self):
        self.waypoint = [-self.waypoint[1], self.waypoint[0]]

    def __forward(self, value):
        self.x += self.waypoint[0] * value
        self.y += self.waypoint[1] * value

    def move(self, instruction):
        if instruction[0] == 'N':
            self.waypoint[1] -= instruction[1]
        elif instruction[0] == 'S':
            self.waypoint[1] += instruction[1]
        elif instruction[0] == 'W':
            self.waypoint[0] -= instruction[1]
        elif instruction[0] == 'E':
            self.waypoint[0] += instruction[1]
        elif instruction[0] == 'F':
            self.__forward(instruction[1])
        elif instruction[0] == 'R':
            assert instruction[1] in self.valid_degrees, "Invalid degrees value"
            steps = int((instruction[1] / 90) % 4)
            for step in range(steps):
                self.__turn_right()
        elif instruction[0] == 'L':
            assert instruction[1] in self.valid_degrees, "Invalid degrees value"
            steps = int((instruction[1] / 90) % 4)
            for step in range(steps):
                self.__turn_left()


with open("./data/data1") as file:
    instructions = [(row[0], int(row[1:])) for row in file]
    boat = Boat()
    for instruction in instructions:
        boat.move(instruction)
    print(abs(boat.x) + abs(boat.y))
