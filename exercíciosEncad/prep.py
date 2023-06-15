class Elemento:
    def __init__(self,v):
        self._valor = v
        
    def getValor(self):
        return self._valor
    
    def setValor(self, v):
        self._valor = v

class No():
      def __init__(self, v):
            self._elemento = v
            self._proximo = None

      def getElemento(self):
            return self._elemento
      def setElemento(self, e):
            self._elemento = e
        
      def getProximo(self):
            return self._proximo
    
      def setProximo(self, p):
            self._proximo = p