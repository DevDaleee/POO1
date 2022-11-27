from datetime import datetime

__slots__ = ['__nome', '__nascimento', '__altura']
class Func:
    def __init__(self, nome, nascimento, altura):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__altura = altura
    @property
    def get_nome(self):
        return self.__nome
    
    @get_nome.setter
    def set_nome(self, nome):
        self.__nome = nome

    @property
    def get_nascimento(self):
        return self.__nascimento
    
    @get_nascimento.setter
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
    
    @property
    def get_altura(self):
        return self.__altura
    
    @get_altura.setter
    def set_altura(self, altura):
        self.__altura = altura
        
    def calc_idade(self, ano_n):
        ano_atual = datetime.now().year
        idade = ano_atual - int(ano_n)
        return print(f'Idade: {idade} anos')
        
    def Mdados(self):
        print(f'Nome: {self.get_nome}')
        print(f'Data de nascimento: {self.get_nascimento}')
        print(f'Altura: {self.get_altura:.2f}cm')