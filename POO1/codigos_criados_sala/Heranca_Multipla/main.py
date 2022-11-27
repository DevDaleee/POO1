from func import Funcionario, Gerente
from autenticavel import Autenticavel
from sistemaInterno import SistemaInterno

if __name__ == '__main__':
    g = Gerente('flavio', '123')
    Autenticavel.register(Gerente)
    SistemaInterno().login(g)