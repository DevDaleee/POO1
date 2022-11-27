bd_Funcionarios = {}

class Funcionarios:
    def __init__(self, nome, cpf, nasc, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__nasc = nasc
        self.__salario = salario
    
    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def get_cpf(self):
        return self.__cpf
    
    @property
    def get_nasc(self):
        return self.__nasc
    
    @property
    def get_salario(self):
        return self.__salario
    
    @get_salario.setter
    def set_profissao(self, salario):
        self.__salario = salario

    def preenche_funcionario(self, funcionario):
        if (self.get_cpf not in bd_Funcionarios):
            bd_Funcionarios[self.get_cpf] = funcionario
            return True
        else:
            return False
    
    def verifica_cadastro(self, cpf):
        if (cpf in bd_Funcionarios):
            return True
        else:
            return False
