'''
cont = 1
while cont <= 4:
    print(f'executou {cont} vez')
    cont += 1
'''

postagens = [
    'Hoje passeando pela avenida paulista',
    'Fazendo trilha na pedra do Gavião',
    'Estudei uma aula de programação',
    'Almoçando juntos na casa da mãe'
]

x = 0
while x < len(postagens):
    print(f'Post {x}: ' + postagens[x])
    x += 1
    '''if x != len(postagens):
        print('-----------')'''
    '''if x == 2:
        break'''
    if x == len(postagens):
        continue
    print('-----------')
