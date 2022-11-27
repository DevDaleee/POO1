class Agenda:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_idade(self):
        return self.__idade
    
    @property
    def get_altura(self):
        return self.__altura

    def mostrar_ag(self, numero_pess):
        print(f'Número: {numero_pess}')
        print(f'Nome: {self.get_nome}')
        print(f'Idade: {self.get_idade}')
        print(f'Altura: {self.get_altura:.2f}')
        print('-' * 30)
    
    def listar_ag(self, agenda_dic):
        for chave, valor in agenda_dic.items():
            valor.mostrar_ag(chave)

    def exclui(self, agenda_dic, nome):
        for chave, valor in agenda_dic.items():
            if (valor.nome == nome):
                agenda_dic.pop(chave)
                return True
        return False
    
    def busca(self, agenda_dic, nome):
        for chave, valor in agenda_dic.items():
            if (valor. nome == nome):
                valor.mostrar_ag(chave)
                return True
        return False