'''
set -> conjuntos
'''

itens = {'Jamilton', 'José', 'Ana'} #não aceita itens repetidos (como 'Ana' por exemplo)
#print(type(itens))

carros = {'Fusca', 'Gol', 'Fiat 147'}
carros2 = {'BMW', 'Fusca', 'Passat'}
#novo = carros.union(carros2)
novo = carros.intersection(carros2)
print(novo)
#carros.add('Fusca') -> não adiciona, apenas traz o elemento para ultima posição
carros.remove('Gol')
print(carros)