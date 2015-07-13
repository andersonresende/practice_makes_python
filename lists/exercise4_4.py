#! coding: utf-8

peoples_lst = [
    {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
    {'first': 'Barack', 'last': 'Obama', 'email': 'president@whitehouse.gov'},
    {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'},
    ]

for people in sorted(peoples_lst, key=lambda a: [a['last'], a['first']]):   # 1.1
    # print '{0}, {1}:{2}'.format(people['last'], people['first'], people['email'])
    print '{last}, {first}:{email}'.format(**people)    # 1.2


## É possível usar a função sorted em python para retornar uma nova lista ordenada, pelo argunmento da função lambda.
## Usar o format definindo keywords quando trabalhar com dicionarios é muito interessante.

