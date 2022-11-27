import abc 

class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    @abc.abstractmethod
    def atualiza():
        pass
class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
         super().__init__(numero, titular, saldo, limite)
         
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, limite=1000):
         super().__init__(numero, titular, saldo, limite)
         
if	__name__	==	'__main__':
	ContaC = ContaCorrente('123-4',	'João',	1000.0)
    #contaP = ContaPoupanca('123-5', 'José', 1000.0)
    
	ContaC.atualiza(0.01)
	#contaP.atualiza(0.01)
 
	print(ContaC.saldo)
	#print(contaP.saldo)
