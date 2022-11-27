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
if __name__ == '__main__':
    c = Conta(123, 'Dalessandro', saldo = 100)
    print(c.titular)

#Resposta:  Não posso instaciar classes abstratas.