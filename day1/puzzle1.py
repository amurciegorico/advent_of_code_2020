#!/usr/bin/env python3

file = open("./data/data1", "r")
content = file.readlines()

firstNumberIndex = 0
for firstNumberString in content:
    firstNumber = int(firstNumberString)
    firstNumberIndex += 1
    for secondNumberString in content[firstNumberIndex:]:
        secondNumber = int(secondNumberString)
        if firstNumber + secondNumber == 2020:
            print(firstNumber * secondNumber)
