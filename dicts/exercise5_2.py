#! coding: utf-8

# Bad Solution
# peoples_dict = {'Anderson': 'Bonito', 'Renato': 'Feio'}
# new_dict = {}
# for people in peoples_dict.keys():
#     new_dict[peoples_dict[people]] = people
# print new_dict

# Good Solution
peoples_dict = {'Anderson': 'Bonito', 'Renato': 'Feio'}
print {value: key for key, value in peoples_dict.items()}   # 1.1

## 1.1 O método items retorna uma tupla com a chave e o valor e também é usado dict compressions.