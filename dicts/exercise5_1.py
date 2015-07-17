#! coding: utf-8
from collections import Counter

# My bad Solution
# numbers_lst = [1, 2, 1, 3, 4, 4, 5]
# print len(Counter(numbers_lst))

numbers_lst = [1, 2, 3, 1, 2, 3, 4, 1]
unique_numbers = set(numbers_lst)   # 1.1
print(len(unique_numbers))


## Set é mais indicado por que vc não precisa dos valores retornados pelo counter.