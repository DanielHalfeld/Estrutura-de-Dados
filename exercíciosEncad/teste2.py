from ListaEncadeada import ListaEncadeada
from prep import Elemento, No
l = [4,2,6,8,0,7,5,3]
a = ListaEncadeada()
for i in l:
    n = Elemento(i)
    no = No(n)
    a.insereNoFim(no)
a.contElem()