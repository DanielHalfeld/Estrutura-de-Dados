from ArvoreBB import ArvoreBuscaBinaria
from NoABB import No
from Elemento import Elemento

l = [4,2,5,10,3,6,7,11,9]
a = ArvoreBuscaBinaria()
for i in l:
    a.insereNo(i)

print(a.qtd(a.getRaiz()))