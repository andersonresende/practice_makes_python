#! coding: utf-8

# Bad Solution
# pass_file = open('password.txt', 'r')
# users_dict = {}
# for line in pass_file:
#     content = line.split(':')
#     users_dict[content[0]] = content[2]
#
# for key, value in users_dict.items():
#     print key, value

users = {}
with open('password.txt') as f:  # 1.1
     users_dict = {line.split(':')[0]: line.split(':')[2]
                  for line in f if not line.startswith('#')}    # 1.2 1.3

for username in sorted(users):
    print("{}:{}".format(username, users[username]))

# 1,1 Abrir arquivos usando o with se desejar percorre-los é a melhor forma pois ele fecha o arquivo automaticamente.
# 1.2 Ao iterar um arquivo as linhas são strings.
# 1.4 Dict compressions pra gerar dicionário.