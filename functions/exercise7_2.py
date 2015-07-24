#! coding: utf-8

import operator  # 1,1

operations = {
    '+': operator.add,  # 1.2
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
    '**':operator.pow,
    '%': operator.mod}

to_solve = raw_input("Enter a two-operand math problem, with prefix notation: ")
operator, first_s, second_s = to_solve.split()
first = int(first_s)
second = int(second_s)
print(operations[operator](first, second))

# 1.1 Modulo python operator contem as funções matemáticas
# 1.2 Dispatch table, tecnica que evita que vc use vários ifs, vimos ela no coursera interactive python.

