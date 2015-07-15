#! coding: utf-8

peoples_lst = [
    ('Barack', 'Obama', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]

#  My Bad Solution
# for people in peoples_lst:
#     first_name = "{}{}".format(people[0], ' ' * (10 - len(people[0])))
#     last_name = "{}{}".format(people[1], (' ' * (10 - len(people[1]))))
#     time_txt = "{:.2f}".format(people[2])
#     time = "{}{}".format(time_txt, (' ' * (5 - len(time_txt))))
#     print "{} {} {}".format(last_name, first_name, time)

for person in sorted(peoples_lst, key=lambda person: (person[1], person[0])):
    print("{1:10} {0:10} {2:5.2f}".format(*person)) # 1.1


## Usar o format pra determinar o tamanho da string e usar o * pra abrir uma lista passando os parametros.
