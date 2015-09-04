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


class BigCone(Cone):
    max_scoops = 5  # 1.1


# 1.1 Devido a voce ter encapsulado o valor maximo da quantidade de bolas em uma variavel de classe e não dentro
# da propria função, fica muito mais simples herdar a classe e modificar o comportamento.
# 1.2 Outro ponto é que vc precisa saber que colocando um atributo de classe ele vale pra todos os objetos, e criando
# um atributo no objeto ele vale apenas para aquele objeto. No entanto, decidir se o atributo vai ser de classe ou objeto
# é algo abastrato, você vai ter que decidir de acordo com a evolução do código ou semantica, o que faz mais sentido.
# Por que voce pode conseguir o mesmo comportamento muitas vezes usando as duas opções, apenas modificando algumas coisas.

