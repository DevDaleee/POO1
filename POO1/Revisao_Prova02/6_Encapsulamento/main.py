"""
Public, Protected, Private
_Protected (public _) |  "Recomenda-se que não altere esse valor"
__Private (_NOMECLASSE__nomeatributo) | "Recomenda-se fortemente que esse valor não seja alterado"
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    """
    @property
    def dados(self):
        self.__dados
    """
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Marcos')
bd.inserir_cliente(2, 'Dalessandro')
bd.__dados = "Uma outra mudança"
print(bd.__dados)
bd.lista_clientes()

#bd._dados = "Uma Mudança" Qunado for protected dá pra fazer isso.