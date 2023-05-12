class Elemento:
  def __init__(self, v = 0):
    self.__valor = v
  def getValor(self):
    return self.__chave 
  def setValor(self, v):
    self.__valor = v 
  def getElemento(self):
    return self.getChave(), self.getNome()