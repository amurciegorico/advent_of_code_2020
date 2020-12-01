#!/usr/bin/env python3

file = open("./data/data1", "r")
content = file.readlines()

firstNumberIndex = 0
for firstNumberString in content:
    firstNumber = int(firstNumberString)
    firstNumberIndex += 1
    secondNumberIndex = firstNumberIndex
    for secondNumberString in content[firstNumberIndex:]:
        secondNumber = int(secondNumberString)
        secondNumberIndex += 1
        for thirdNumberString in content[secondNumberIndex:]:
            thirdNumber = int(thirdNumberString)
            if firstNumber + secondNumber + thirdNumber == 2020:
                print(firstNumber * secondNumber * thirdNumber)
