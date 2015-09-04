#! coding: utf-8


class Scoop(object):

    def __init__(self, flavor):
        self.flavor = flavor


class Cone(object):

    max_scoops = 3  # 1.1

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scoop)
            else:
                break

    def __repr__(self):
        return "\n".join([scoop.flavor for scoop in self.scoops])


s1 = Scoop('Chocolate')
s2 = Scoop('Morango')
s3 = Scoop('Baunilha')
s4 = Scoop('Uva')
s5 = Scoop('Pessego')

cone = Cone()
cone.add_scoops(s1, s2)
cone.add_scoops(s3, s4)
cone.add_scoops(s5)

print cone

# 1.1 max_scoops é um atributo de classe por que ele vale pra todos os cones, se você pudesse decidir pra cada cone
# ele estaria no objeto.