#! coding: utf-8

filename = raw_input("Enter a filename: ")
print(open(filename).readlines()[-1])
