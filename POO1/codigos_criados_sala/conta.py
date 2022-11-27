
class Conta():

    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Nao pode ser negativo')
        else:
            self._saldo = saldo

    @property
    def numero(self):
        return self._numero