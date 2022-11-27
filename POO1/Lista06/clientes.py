bd_Clientes = {}

class Clientes():
    def __init__(self, nome, cpf, nasc, profissao, num_cc = 0, num_cp = 0, qnt_contas = 0):
        self.__nome = nome
        self.__cpf = cpf
        self.__nasc = nasc
        self.__profissao = profissao
        self.__num_cc = num_cc
        self.__num_cp = num_cp
        self.__qnt_contas = qnt_contas
    
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
    def get_profissao(self):
        return self.__profissao
    
    @get_profissao.setter
    def set_profissao(self, profissao):
        self.__profissao = profissao
    
    @property
    def get_num_cc(self):
        return self.__num_cc

    @get_num_cc.setter
    def set_num_cc(self, num):
        self.__num_cc += num
    
    @property
    def get_num_cp(self):
        return self.__num_cp
    
    @get_num_cp.setter
    def set_num_cp(self, qnt):
        self.__num_cp += qnt
    
    @property
    def get_qnt_contas(self):
        return self.__qnt_contas
    
    @get_qnt_contas.setter
    def set_qnt_contas(self, valor):
        self.__qnt_contas += valor

    def preenche_clientes(self, cliente):
        if (self.get_cpf not in bd_Clientes):
            bd_Clientes[self.get_cpf] = cliente
            return True
        else:
            return False
    
    def verifica_cadastro(self, cpf):
        if (cpf in bd_Clientes):
            return True
        else:
            return False
    
    def num_contas(self, cpf, tipo):
        if (tipo == 'Conta Corrente' and bd_Clientes[cpf].get_num_cc == 0):
            bd_Clientes[cpf].set_num_cc = 1
            bd_Clientes[cpf].set_qnt_contas = 1
            return True
        elif (tipo == 'Conta Poupança' and bd_Clientes[cpf].get_num_cp == 0):
            bd_Clientes[cpf].set_num_cp = 1
            bd_Clientes[cpf].set_qnt_contas = 1
            return True
        else:
            return False


bd_Seguros = {}
class SeguroDeVida(Clientes):
    def __init__(self, cpf, valor_mensal, valor_tot):
        self.__cpf = cpf
        self.__valor_mensal = valor_mensal
        self.__valor_tot = valor_tot

    @property
    def get_cpf(self):
        return self.__cpf
    
    @get_cpf.setter
    def set_cpf(self, cpf):
        self.__cpf = cpf

    @property
    def get_valor_mensal(self):
        return self.__valor_mensal
    
    @get_valor_mensal.setter
    def set_valor_mensal(self, novo_val):
        self.__valor_mensal = novo_val
    
    @property
    def get_valor_tot(self):
        return self.__valor_tot
    
    @get_valor_tot.setter
    def set_valor_tot(self, novo_val):
        self.__valor_tot = novo_val

    def criar_seguro(self, cpf, seguro):
        if (cpf not in bd_Seguros):
            bd_Seguros[cpf] = []
            bd_Seguros[cpf].append(seguro)
        else:
            bd_Seguros[cpf].append(seguro)
