#! coding: utf-8


def my_xml(tag1, tag2='', **kwargs):
    extra = ''
    if kwargs:
        extra = extra.join([" {}='{}'".format(key, value)
                            for key, value in kwargs.items()])

    xml_tag = "<{main}{extra}>{content}</{main}>"\
        .format(main=tag1, content=tag2, extra=extra)

    return xml_tag

print my_xml('div', 'h1', a=1, b=2)
print my_xml('div', my_xml('div', 'h1', a=1, b=2), a=1, b=2)
print my_xml('div', my_xml('div', my_xml('div', 'h1', a=1, b=2), a=1, b=2), a=1, b=2)   # 1.1

# 1.1 é preciso diferencia uma função que recebe uma função como arumento de uma que chama a função e gera um argumento.
# a função map recebe uma função como argumento, ja a função acima chama uma função e seu valor e passado como argumento.