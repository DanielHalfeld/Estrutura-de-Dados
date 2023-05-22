from ArvoreBB import ArvoreBuscaBinaria
from NoABB import No
from Elemento import Elemento

l = [15, 5, 4, 7, 11, 2]
a = ArvoreBuscaBinaria()
for i in l:
    a.insereNo(i)
#a.decrescente(a.getRaiz())
#print(a.qtd(a.getRaiz()))
#print(a.soma(a.getRaiz()))
#print(a.menor(a.getRaiz()))
print(a.maior(a.getRaiz()))
#a.emOrdem(a.getRaiz())