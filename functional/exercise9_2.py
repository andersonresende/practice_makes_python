#! coding: utf-8

numbers = raw_input("Insira os números: ")
numbers_lst = numbers.split()
total = sum((int(number) for number in numbers_lst))    # 1.1
print "Sum: {}".format(total)

# 1.1 Usar generator compression no lugar de list compressions.

