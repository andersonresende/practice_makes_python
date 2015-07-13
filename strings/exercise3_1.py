#! coding: utf-8

word = raw_input('Put the word: ')
ping_word = ''
if word[0] in 'aeiou':  # 1.1, 1.2, 1.3
    ping_word = word + 'way'
else:
    sufix = word[0] + 'ay'
    ping_word = word[1:] + sufix
print ping_word


## 1.1 Usar apenas uma string ao invés de uma lista com as vogais
## 1.2 Já que a string só vai ser usada uma vez, não precisa estar em uma variável.
## 1.3 Usar operador in é big one, ou seja uma busca rápida.