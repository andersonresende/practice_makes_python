#! coding: utf-8


def transform_values(f, dic):
    return {key: f(value)
            for key, value in dic.items()}  # 1.1


print transform_values(lambda a: a+a, {'a': 1, 'b': 2})

# 1.1 Usar dict compressions