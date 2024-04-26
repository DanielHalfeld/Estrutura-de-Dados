dicionario = {
    'correr': 'Deslocar-se ou mover rapidamente',
    'ligar': 'Estabelecer uma comunicação',
    'dia': [26,'Uma data']
}

dicionario['andar'] = 'Se mover'
dicionario.update({'ano': 2024, 'cidade': 'Volta Redonda'})

del dicionario['andar']
subs = dicionario.pop('ligar')
# print(subs)
#print(dicionario['andar'])
#dicionario.keys / dicionario.values / dicionario.items / dicionario.get / len(dicionario) / dicionario.clear
print(dicionario)
