from xml.dom import VALIDATION_ERR
from clientes import *
from funcionarios import *
from criar_conta import *

class Tributacoes:
    def __init__(self):
        self.__tributacoes_hist = []

    @property
    def get_tributacoes_hist(self):
        return self.__tributacoes_hist

class Functions:

    def __init__(self, num_contas = 0):
        self.__tributacao = Tributacoes()
        self.__num_contas = num_contas
    
    @property
    def get_tributacao(self):
        return self.__tributacao
    
    @property
    def get_num_contas(self):
        return self.__num_contas
    
    @get_num_contas.setter
    def set_num_contas(self, num):
        self.__num_contas += num
    
    def mostrar_contas(self):
        if (len(bd_Contas) == 0):
            return False
        else:
            print(f'{"CPFs cadastrados":^40}')
            for chave, valor in bd_Contas.items():
                print(f'CPF -> {chave}')
                
                for i in valor:
                    print(f'{i.get_tipo}')
                print()
    
    def mostrar_clientes(self):
        if len(bd_Contas) > 0:
            for cpf_cont in bd_Contas.keys():
                for cpf_cli in bd_Clientes.keys():
                    if cpf_cont == cpf_cli:
                        print(f'Nome -> {bd_Clientes[cpf_cont].get_nome}')
                        print(f'Número de contas -> {bd_Clientes[cpf_cont].get_qnt_contas}')
                if (cpf_cont in bd_Seguros):
                    print(f'Seguros de vida -> {len(bd_Seguros[cpf_cont])}')
                else:
                    print('Seguros de vida -> 0')

                print()
            return True
        else:
            return False        


    def verifica_cadadastro(self, cpf_cad):
        bd_Clientes[cpf_cad].verifica_cadastro

    def criar_conta_corrente(self, cpf, tipo = 'Conta Corrente'):
        conta_corrente = ContaCorrente()
        try:
            conta_corrente.cria_conta(cpf, conta_corrente)
            if(bd_Clientes[cpf].num_contas(cpf, tipo)):
                self.set_num_contas = 1
                return True
        except:
            return False
    
    def criar_conta_poupanca(self, cpf, tipo = 'Conta Poupança'):
        conta_poupanca = ContaPoupanca()
        
        try:
            conta_poupanca.cria_conta(cpf, conta_poupanca)
            if(bd_Clientes[cpf].num_contas(cpf, tipo)):
                self.set_num_contas = 1
                return True
        except:
            return False
    
    def criar_seguro(self, cpf, valor_mes, valor_total):
        seguro = SeguroDeVida(cpf, valor_mes, valor_total)
        seguro.criar_seguro(cpf, seguro)
    
    def operacao(self, cpf, tipo, valor, tipo_conta):
        if (tipo == 7):
            
            for classe in bd_Contas[cpf]:
                if classe.get_tipo == tipo_conta:
                    classe.sacar(valor)
            return True

        elif (tipo == 8):

            for classe in bd_Contas[cpf]:
                if classe.get_tipo == tipo_conta:
                    classe.depositar(valor)
            return True

        else:
            return False
    
    def transfere(self, cpfO, cpfD, valor, tipo_origem, tipo_destino):
        try:
            for classe in bd_Contas[cpfO]:
                if classe.get_tipo == tipo_origem:
                    classe.transfere(cpfD, tipo_destino, valor)
                return True
        except:
            return False

    def historico(self, cpf, tipo_conta):
        try:            
            for classe in bd_Contas[cpf]:
                if classe.get_tipo == tipo_conta:
                    classe.get_historico.imprime_t()
            return True
        except:
            return False
    
    def tributacao(self):
        tributacao_clientes = {}
        soma_trib = 0

        for cpf, valor in bd_Contas.items():
            for conta in valor:
                if conta.get_tipo == 'Conta Corrente':

                    if cpf in bd_Seguros:
                        for classe in bd_Seguros[cpf]:
                            tributacao_clientes[cpf] = 10 + 0.01 * conta.get_saldo + 0.02 * classe.get_valor_mensal
                    else:
                        return False

        print(tributacao_clientes)
        for valor in tributacao_clientes.values():
            soma_trib += valor

        self.get_tributacao.get_tributacoes_hist.append(soma_trib)
        return self.get_tributacao.get_tributacoes_hist
    
    