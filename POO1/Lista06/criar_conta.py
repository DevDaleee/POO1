from abc import ABC
from random import randint
from criar_conta import *
import datetime

bd_Contas = {}

class Historico:

    def __init__(self):
        self.__data_abertura = datetime.datetime.today()
        self.__transacoes = []
    
    @property
    def data_abertura(self):
        return self.__data_abertura
    
    @property
    def transacoes_c(self):
        return self.__transacoes

    def imprime_t(self):
        print(f'Data de abertura: {self.data_abertura}')
        print('Transações: ')
        for t in self.transacoes_c:
            print('-', t)

class Conta(ABC):
    def __init__(self, numero = 0, saldo = 0):
        self.__numero = numero
        self.__saldo = saldo
        self.__historico = Historico()
    
    @property
    def get_numero(self):
        return self.__numero

    @get_numero.setter
    def set_numero(self, numero):
        self.__numero = numero

    @property
    def get_saldo(self):
        return self.__saldo
    
    @get_saldo.setter
    def set_saldo(self, saldo):
        if saldo > 0:
            self.__saldo = saldo
            return True
        else:
            return False

    @property
    def get_historico(self):
        return self.__historico

    def gera_numero(self):
        numero = randint(100, 999)
        self.set_numero = numero
    

    def cria_conta(self, cpf, conta):
        if (cpf not in bd_Contas):
            bd_Contas[cpf] = []
            bd_Contas[cpf].append(conta)
        elif (len(bd_Contas[cpf]) == 1):
            bd_Contas[cpf].append(conta)
        else:
            return False

        return True
    
    def sacar(self, valor):
        if self.get_saldo > 0:
            self.set_saldo = self.get_saldo - valor
            self.get_historico.transacoes_c.append(f'Saque de R${valor} - Data: {datetime.datetime.today()}')
            return True
        else:
            return False
    
    def depositar(self, valor):
        if (valor > 0):
            self.set_saldo = self.get_saldo + valor
            self.get_historico.transacoes_c.append(f'Depósito de R${valor} - Data: {datetime.datetime.today()}')
            return True
        else:
            return False
    
    def transfere(self, cpf, tipo, valor):
        retirou = self.sacar(valor)

        if (retirou):
            for classe in bd_Contas[cpf]:
                if classe.get_tipo == tipo:
                    classe.depositar(valor)
            
            self.get_historico.transacoes_c.append(f'Transferência de R${valor} - Para conta de {bd_Contas[cpf].get_numero}')
            return True
        else:
            return False

class ContaCorrente(Conta):
    def __init__(self, numero = 0, saldo = 0, tipo = 'Conta Corrente'):
        super().__init__(numero, saldo)
        self.__tipo = tipo
    
    @property
    def get_tipo(self):
        return self.__tipo

class ContaPoupanca(Conta):
    def __init__(self, numero = 0, saldo = 0, tipo = 'Conta Poupança'):
        super().__init__(numero, saldo)
        self.__tipo = tipo
    
    @property
    def get_tipo(self):
        return self.__tipo
