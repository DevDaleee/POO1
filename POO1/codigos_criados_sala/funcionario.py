
class Funcionario():

    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def get_bonificacao(self):
        return 0.1*self._salario

    def imprimir(self):
        print(self._nome, self._salario)

class Gerente(Funcionario):

    def __init__(self, nome, salario, senha):
        super().__init__(nome, salario)
        self._senha = senha

    def get_bonificacao(self):
        return 0.2*self._salario

    def imprimir(self):
        super().imprimir()
        print(self._senha)

class ControleBonificacao():

    def __init__(self):
        self._total_bonificacoes = 0

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()



if __name__ == '__main__':
    f = Funcionario('Henrique', 100)
    g = Gerente('Flavio', 100, 'senha')
    g1 = Gerente('Jose', 100, 'senha')
    cb = ControleBonificacao()

    cb.registra(f)
    cb.registra(g)
    cb.registra(g1)

    print(cb.total_bonificacoes)


    f.imprimir()
    g.imprimir()
