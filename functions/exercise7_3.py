#! coding: utf-8

import random


def create_password_generator(characters):
    def generate_by_number(number):
        rand_lst = (random.choice(characters) for _ in range(number))
        return ''.join(rand_lst)    # 1.1
    return generate_by_number

print create_password_generator("abc")(10)

# 1,1 usar o join com uma string vazia.