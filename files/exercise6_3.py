#! coding: utf-8

# Bad solution
# char_number = 0
# words_number = 0
# words_lst = []
# cont = 0
# with open('test-file.txt') as f:
#     for line in f:
#         char_number += len(line)
#         words_lst += [word for word in line.split()]
#         cont += 1
#
# print char_number, len(words_lst), len(set(words_lst)), cont


number_of_characters = 0
number_of_words = 0
unique_words = set()

for number_of_lines, line in enumerate(open('test-file.txt'), 1):   # 1.1
    number_of_characters += len(line)
    number_of_words += len(line.split())
    unique_words.update(line.split())   # 1.2

print("Number lines: {}".format(number_of_lines))
print("Number characters: {}".format(number_of_characters))
print("Number words: {}".format(number_of_words))
print("Number unique words: {}".format(len(unique_words)))


# 1.1 Usar enumerate com um arquivo pra pegar a quantidade de linhas
# 1.2 Usar o extende do set, ao inves de dar um set no final, e bem legal.