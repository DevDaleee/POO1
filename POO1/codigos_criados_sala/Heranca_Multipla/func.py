class Funcionario():
    def __init__(self,nome):
        self.__nome = nome
        
class Gerente(Funcionario):
    def __init__ (self,nome,senha):
        super().__init__(nome)
        self._senha = senha
    def autentica(self,senha):
        if self._senha == senha:
            print('Logado')
            return True
        else:
            return False
