#! coding: utf-8

sentence = raw_input("Put one sentece: ")
ping_sentence = ''
words_lst = sentence.split()
ping_lst = []
for word in words_lst:
    if word[0] in 'aeiou':
        ping_lst.append(word + 'way')
    else:
        sufix = word[0] + 'ay'
        ping_lst.append(word[1:] + sufix)
    ping_sentence = ' '.join(ping_lst)  # 1.1
print ping_sentence


## 1.1 Para concatenar uma lista de strings é bem melhor usar join do que ir somando as strings.

