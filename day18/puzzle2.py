#!/usr/bin/env python3

def find_inner_parentheses(expression):
    depth = 0
    max_depth = 0
    max_depth_in_index = -1
    max_depth_out_index = -1
    for index, character in enumerate(expression):
        if character == '(':
            depth += 1
            if depth >= max_depth:
                max_depth = depth
                max_depth_in_index = index
        elif character == ')':
            if depth == max_depth:
                max_depth_out_index = index
            depth -= 1
    return max_depth_in_index, max_depth_out_index


def solve_expression(expression):
    if '(' in expression:
        indices = find_inner_parentheses(expression)
        return solve_expression(expression[:indices[0]] + str(solve_expression(expression[indices[0] + 1: indices[1]])) + expression[indices[1] + 1:])
    if '*' in expression:
        index = expression.find('*')
        return solve_expression(expression[:index]) * solve_expression(expression[index + 1:])
    if '+' in expression:
        index = expression.find('+')
        return solve_expression(expression[:index]) + solve_expression(expression[index + 1:])
    return int(expression)


with open("./data/data1") as file:
    result = 0
    for line in file.readlines():
        result += solve_expression(line[:-1].replace(' ', ''))
    print(result)
