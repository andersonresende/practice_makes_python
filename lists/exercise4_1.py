#! coding: utf-8


def first_last(sequence):
    return sequence[:1] + sequence[-1:]  # 1.1
print first_last((1, 2, 4, 5))
print first_last([1, 2, 4, 5])


## Quando se usa slice pra retornar os itens eles sao retornados com o tipo que estão inseridos, quando se retorna
## sem slice, apenas o valor e retornado.