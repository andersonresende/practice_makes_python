#! coding: utf-8
from collections import Counter


def most_repeating_word(words):
    word_counts = {word: max(Counter(word).items(), key=lambda t: t[1]
                             ) for word in words}   # 1.1
    return max(word_counts, key=lambda w: word_counts[w][1])    # 1.2

print most_repeating_word(['juca', 'tatu', 'bola', 'absddde'])

## 1.1 Usar a classe Counter pra contar a quantidade de cada letra. E ter a inteligência de montar um novo dict
## com o valor de cada palavra.
## 1.2 A função max também pode receber uma key pra dizer por qual elemento vai retornar o maior valor. Massa!