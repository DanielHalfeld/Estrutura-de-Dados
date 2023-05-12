from NoABB import No

class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self, n):
        self__raiz = n
    def arvoreVazia(self):
        return self.__raiz == None
    def criaNo(self, v):
        no = No()
        no.getElemento().setValor(v)
        return no
    def insereNo(self, v):
        if self.arvoreVazia():
            self.setRaiz(self.criaNo(v))
        else:
            self.insere(None, self.getRaiz(), v)
    def insere(self, pai, atual, v):
        if (atual != None):
            if (v < atual.getElemento().getValor()):
                self.insere(atual, atual.getFilhoEsquerda(), v)
            else:
                self.insere(atual, atual.getFilhoDireita(), v)
        else:
            x = self.criaNo(v)
            if (v < pai.getElemento().getValor()):
                pai.setFilhoEsquerda(x)
            else:
                pai.getFilhoDireita(x)
                
       
    