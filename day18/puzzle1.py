#!/usr/bin/env python3

import string


def solve_expression(expression):
    if expression[-1] in string.digits:
        sum_sign_index = expression.rfind('+')
        multiplication_sign_index = expression.rfind('*')
        if sum_sign_index == -1 and multiplication_sign_index == -1:
            return int(expression)
        elif sum_sign_index == -1:
            return int(expression[multiplication_sign_index + 1:]) * solve_expression(expression[:multiplication_sign_index])
        elif multiplication_sign_index == -1:
            return int(expression[sum_sign_index + 1:]) + solve_expression(expression[:sum_sign_index])
        else:
            if multiplication_sign_index > sum_sign_index:
                return int(expression[multiplication_sign_index + 1:]) * solve_expression(expression[:multiplication_sign_index])
            else:
                return int(expression[sum_sign_index + 1:]) + solve_expression(expression[:sum_sign_index])
    else:
        parenthesis = 1
        index = len(expression) - 1
        while parenthesis > 0:
            index -= 1
            if expression[index] == ')':
                parenthesis += 1
            elif expression[index] == '(':
                parenthesis -= 1
        if index == 0:
            return solve_expression(expression[1:-1])
        elif expression[index - 1] == '+':
            return solve_expression(expression[index + 1:-1]) + solve_expression(expression[:index - 1])
        else:
            assert expression[index - 1] == '*', 'Unknown option...'
            return solve_expression(expression[index + 1:-1]) * solve_expression(expression[:index - 1])


with open("./data/data1") as file:
    result = 0
    for line in file.readlines():
        result += solve_expression(line[:-1].replace(' ', ''))
    print(result)
