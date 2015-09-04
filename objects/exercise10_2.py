#! coding: utf-8


class Scoop(object):

    def __init__(self, flavor):
        self.flavor = flavor


class Cone(object):

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoops):  # 1.1
        self.scoops.extend(scoops)

    def __repr__(self):
        return "\n".join([scoop.flavor for scoop in self.scoops])   # 1.2


s1 = Scoop('Chocolate')
s2 = Scoop('Morango')
s3 = Scoop('Baunilha')

cone = Cone()
cone.add_scoops(s1, s2)
cone.add_scoops(s3)

print cone


# 1.1 Você não precisa usar o nome args, basta usar o *
# 1.2 Você pode usar \n detro do join.

