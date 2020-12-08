#!/usr/bin/env python3

class Cpu:
    pc = 0
    acc = 0

    def execute(self, line):
        instruction = line.split(' ')
        if instruction[0] == 'nop':
            self.pc += 1
        elif instruction[0] == 'acc':
            self.acc += int(instruction[1])
            self.pc += 1
        elif instruction[0] == 'jmp':
            self.pc += int(instruction[1])
        else:
            assert False, "Unknown instruction"


file = open("./data/data1", "r")
instructions = file.readlines()

cpu = Cpu()
executed_lines = set()
while cpu.pc not in executed_lines:
    executed_lines.add(cpu.pc)
    cpu.execute(instructions[cpu.pc])

print(cpu.acc)
