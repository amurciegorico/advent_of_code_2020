#!/usr/bin/env python3

class Cpu:
    pc = 0
    acc = 0

    def run(self, instructions):
        executed_lines = set()
        while self.pc not in executed_lines:
            if self.pc >= len(instructions):
                return True
            executed_lines.add(self.pc)
            self.execute(instructions[self.pc])
        return False

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

for index in range(len(instructions)):
    instruction = instructions[index].split(' ')
    new_instruction = ''
    if instruction[0] == 'nop':
        new_instruction = 'jmp ' + instruction[1]
    elif instruction[0] == 'jmp':
        new_instruction = 'nop ' + instruction[1]
    else:
        continue
    new_instructions = instructions.copy()
    new_instructions[index] = new_instruction
    cpu = Cpu()
    if cpu.run(new_instructions):
        print(cpu.acc)
        break
