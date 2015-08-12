#! coding: utf-8

letters_dict = {chr(n+96): n for n in range(1, 27)}  # 1.1
print letters_dict

letters_dict = {chr(n): index for index, n in enumerate(range(97, 97+26), 1)}   # 1.2
print letters_dict

#  1.1 letra a corresponde ao valor 96 na tabela asc
#  1.2 você pode definir index incial do enumerate
