class Conta:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def mostra_nome(self):
        return self.__nome
    
    @property
    def mostra_cpf(self):
        return self.__cpf