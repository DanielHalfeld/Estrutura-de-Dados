from ListaEncadeada import ListaEncadeada

class PilhaEncadeada(ListaEncadeada):
      def __init__(self):
            self = super().__init__()

      def pilhaVazia(self):
            return super().listaVazia()
      
      def push(self, v):
            super().insereNoFim(v)

      def pop(self):
            super().retiraNoFim()