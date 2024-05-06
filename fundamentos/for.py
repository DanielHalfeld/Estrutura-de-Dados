postagens = [
    'Hoje passeando pela avenida paulista',
    'Fazendo trilha na pedra do Gavião',
    'Estudei uma aula de programação',
    'Almoçando juntos na casa da mãe'
]

""" for postagem in postagens:
    print(postagem) """
""" for indice, postagem in enumerate(postagens):
    print(f'{indice} - {postagem}') """

totalPost = len(postagens)
for indice in range(totalPost):
    print(postagens[indice])

#Percorrendo textos, tuplas e set

p = 'Daniel'
for letra in p:
    print(f'- {letra} -')

meses = ('Janeiro' , 'Fevereiro', 'Março')
for mes in meses:
    print(f'- {mes} -')

frutas = {'banana', 'maçã', 'abacaxi', 'melancia'}
for fruta in frutas:
    print(f'- {fruta} -')