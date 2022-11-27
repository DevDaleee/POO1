from interface import Interface
import os.path

class Validar(Interface):
    def criar_arq_senhas(self,senha):
        arquivo = open("senhas.json","w")
        arquivo.write(senha)
        arquivo.close()  
            
    def validar_senha(self,senha_verificacao):
        nome_arquivo = "senhas.json"
        ok = False
        try:
            if(os.path.isfile(nome_arquivo)):
                arquivo = open(nome_arquivo, "r")
                senha = arquivo.read()
                if(senha_verificacao == senha):
                    ok = True
                arquivo.close()
        except:
            print("O arquivo não existe")
        return ok
