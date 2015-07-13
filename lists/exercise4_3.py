#! coding: utf-8


def my_sum(*items):
    output = type(items[0])()   # 1.1
    for item in items:
        output += item  # 1.2
    return output

print my_sum(1, 2, 3)
print my_sum([1], [2], [3])
print my_sum((1,), (2,), (3,))


##  1.1 Desta forma você consegue pegar exatamente o tipo do item que esta sendo usado e coloca-lo em uma
## variável.
## 1.2 É possível somar listas e tuplas retornando listas e tuplas extendidas.