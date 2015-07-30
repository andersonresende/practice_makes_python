#! coding: utf-8


def flatten1(lst):
    return reduce(lambda a, b: a+b, lst)


def flatten2(lst):
    if not lst:
        return []
    return lst[0] + flatten2(lst[1:])

print flatten1([[1], [2], [3,4]])
print flatten2([[1], [2], [3,4]])