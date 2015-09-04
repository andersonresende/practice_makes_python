#! coding: utf-8


class Scoop(object):

    def __init__(self, flavor):
        self.flavor = flavor


scoops = [Scoop('Chocolate'), Scoop('Morango'), Scoop('Baunilha')]

for scoop in scoops:
    print scoop.flavor

