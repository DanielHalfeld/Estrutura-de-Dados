from prep import No, Elemento

class ListaEncadeada(No, Elemento):
      def __init__(self):
            e = Elemento(None)
            self._cabeca = No(e)

      def getCabeca(self):
            return self._cabeca
      
      def setCabeca(self, c):
            self._cabeca = c
      
      def listaVazia(self):
            return self.getCabeca().getProximo() == None
      
      def insereNoInicio(self, n):
            n.setProximo(self.getCabeca().getProximo())
            self.getCabeca().setProximo(n)

      def retiraNoInicio(self):
            if not self.listaVazia():
                  atual = self.getCabeca().getProximo()
                  self._cabeca.setProximo(atual.getProximo())
                  return atual
      
      def mostraLista(self):
            at = self.getCabeca().getProximo()
            while at != None:
                  print(at.getElemento().getValor())
                  at = at.getProximo()
      
      def insereNoFim(self, n):
            if not self.listaVazia():
                  atual = self.getCabeca()
                  while atual.getProximo() != None:
                        atual = atual.getProximo()
                  atual.setProximo(n)
            else:
                  self._cabeca.setProximo(n)

      def retiraNoFim(self):
            if not self.listaVazia():
                  anterior = self.getCabeca()
                  atual = self.getCabeca().getProximo()
                  while atual.getProximo() != None:
                        anterior = atual
                        atual = atual.getProximo()
                  anterior.setProximo(None)
                  return atual
            
      def insereOrdenado(self, v):
            anterior = self.getCabeca()
            atual = self.getCabeca().getProximo()
            while atual != None and atual.getElemento().getValor() < v.getElemento().getValor():
                  anterior = atual
                  atual = atual.getProximo()
            v.setProximo(atual)
            anterior.setProximo(v)
      
      def retiraElemento(self, x):
            if not self.listaVazia():
                  anterior = self.getCabeca()
                  atual = self.getCabeca().getProximo()
                  while atual != None and atual.getElemento().getValor() != x:
                        anterior = atual
                        atual = atual.getProximo()
                  if atual != None:
                        anterior.setProximo(atual.getProximo())
                        atual.setProximo(None)
                        return atual
            return None
      def contElem(self):
            if not self.listaVazia():
                  x = self.getCabeca()
                  cont = 0
                  while x.getProximo() != None:
                        cont += 1
                        x = x.getProximo()
                  print(cont)
            return None
      #exercicio corrigido:
      def ListaQuantidadeElemento(self):
            num = self.getCabeca().getProximo()
            x = 0
            while num != None:
                  x +=1
                  num = num.getProximo()
            return x
