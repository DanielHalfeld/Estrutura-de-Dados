from NoABB import No
class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self, n):
        self.__raiz = n
    def arvoreVazia(self):
        return self.__raiz == None
    def criaNo(self, v):
        no = No()
        no.getDados().setChave(v)
        return no
    def insereNo(self, v):
        if self.arvoreVazia():
            self.setRaiz(self.criaNo(v))
        else:
            self.insere(None, self.getRaiz(), v)
    def insere(self, pai, atual, v):
        if atual != None:
            if v < atual.getDados().getChave(): # Alteração do elemento
                self.insere(atual, atual.getFilhoEsquerda(), v)
            else:
                self.insere(atual, atual.getFilhoDireita(), v)
        else:
            x = self.criaNo(v)
            if v < pai.getDados().getChave():
                pai.setFilhoEsquerda(x)
            else:
                pai.setFilhoDireita(x)
                
    def emOrdem(self, n):
        if n != None:
            self.emOrdem(n.getFilhoEsquerda())
            print(n.getDados().getChave())
            self.emOrdem(n.getFilhoDireita())
    
    def preOrdem(self, n):
        if n != None:
            print(n.getDados().getChave())
            self.preOrdem(n.getFilhoEsquerda())
            self.preOrdem(n.getFilhoDireita())

    def posOrdem(self, n):
        if n != None:
            self.posOrdem(n.getFilhoEsquerda())
            self.posOrdem(n.getFilhoDireita())
            print(n.getDados().getChave())

    # Exercício 1
    def decrescente(self, n):
        if n != None:
            self.decrescente(n.getFilhoDireita())
            print(n.getDados().getChave())
            self.decrescente(n.getFilhoEsquerda())
    
    def pesquisa(self, n, v):
        if n != None:
            if v == n.getDados().getChave():
                return True
            elif v < n.getDados().getChave():
                return self.pesquisa(n.getFilhoEsquerda(), v)
            else:
                return self.pesquisa(n.getFilhoDireita(), v)
        return False        
    
    def qtd(self, n):
        if n != None:
            return 1 + self.qtd(n.getFilhoEsquerda()) + self.qtd(n.getFilhoDireita())
        return 0
    
    def soma(self, n):
        if n != None:
            return n.getDados().getChave() + self.soma(n.getFilhoEsquerda()) + self.soma(n.getFilhoDireita())
        return 0
    
    def menor(self, n):
        if n != None:
            if n.getFilhoEsquerda() != None:
                return self.menor(n.getFilhoEsquerda())
            else:
                return n.getDados().getChave()
        return None
    
    def maior(self, n):
        if n != None:
            if n.getFilhoDireita() != None:
                return self.maior(n.getFilhoDireita())
            else:
                return n.getDados().getChave()
        return None