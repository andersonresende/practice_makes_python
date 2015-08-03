#! coding: utf-8

from strings.exercise3_1 import to_ping_latin

with open('teste.txt') as f:
    ping_words_lst = [to_ping_latin(word)
                      for line in f
                      for word in line.split()]
    print " ".join(ping_words_lst)

