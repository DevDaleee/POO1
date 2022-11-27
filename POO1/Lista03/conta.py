from random import randint
import datetime

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

class Pessoa:
    
    def __init__(self, titular, numero, valor):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = valor
        self.__historico = Historico()

    @property
    def saldoc(self):
        return self.__saldo
    
    @saldoc.setter
    def saldoc(self, valor):
        self.__saldo = valor

    @property
    def numeroc(self):
        return self.__numero
    
    @numeroc.setter
    def numeroc(self, numc):
        self.__numero = str(numc)

    @property
    def tit(self):
        return self.__titular
    
    @property
    def historico(self):
        return self.__historico

    def sacar(self, valor):
        atual = 0
        if (valor <= self.saldoc and valor > 0):
            atual = self.saldoc
            atual -= valor
            self.saldoc = atual
            return True
        else:
            return False

    def depositar(self, valor):
        atual = 0
        if (valor > 0):
            atual = self.saldoc
            atual += valor
            self.saldoc = atual
            return True
        else:
            return False

    def transfere_para(self, destino, valor):
        retirou = self.sacar(valor)

        if (retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes_c.append(f'Transferência de R${valor} - Para conta {destino.numeroc}')

            return True

    def extrato(self):
        print(f'Titular da conta: {self.tit.mostra_nome}')
        print(f'CPF do titular: {self.tit.mostra_cpf}')
        print(f'Número da conta: {self.numeroc}')
        print(f'Saldo da conta: R${self.saldoc:.2f}')
        print('\n')

    def criar_conta(self, numero):
        numero = randint(100, 1000)
        self.numeroc = numero

        print('-' * 30)
        print('Conta criada com sucesso!')
        print(f'{self.numeroc} é o número da conta!')
        print('-' * 30)
        return str(numero)

    def listar_contas(self, contas):
        for chave, valor in contas.items():
            valor.extrato()
    