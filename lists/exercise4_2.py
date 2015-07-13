#! coding:utf-8


def replace_for_a(lst):
    lst[:] = len(lst) * ['a']   # 1.1
    return lst

print replace_for_a(range(5))


## Usando slice do lado direito é possível alterar a própria lista, sem ser necessário gerar uma nova lista.
