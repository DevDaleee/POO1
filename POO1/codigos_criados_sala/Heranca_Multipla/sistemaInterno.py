from autenticavel import Autenticavel

class SistemaInterno():
    def login(self,obj):
        if isinstance(obj, Autenticavel):
            return obj.autentica('123')
        else:
            print('Método autentica não implementado')
            return False