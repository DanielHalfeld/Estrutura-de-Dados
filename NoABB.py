from Elemento import Elemento
class No:
    def __init__(self, elemento = Elemento()):
        self.__elemento = elemento
        self.__filhoEsquerda = None
        self.__filhoDireita = None
    def getFilhoEsquerda(self):
        return self.__filhoEsquerda
    def setFilhoEsquerda(self, n):
        self.__filhoEsquerda = n
    def getFilhoDireta(self):
        return self.__filhoDireita
    def setFilhoDireita(self, n):
        self.__filhoDireita = n
    def getElemento(self):
        return self.__elemento
    def setElemento(self, e):
        self.__elemento = e