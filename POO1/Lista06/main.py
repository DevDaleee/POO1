from funcionarios import *
from functions import *
from criar_conta import *
from clientes import *

def menu():
    print("Menu Principal")
    print("1 - Cadastrar Funcionario")
    print("2 - Cadastrar Cliente")
    print("3 - Criar Conta Corrente")
    print("4 - Criar Conta Poupança")
    print("5 - Criar Seguro de Vida")
    print("6 - Calcular Tributação")
    print("7 - Sacar")
    print("8 - Depositar")
    print("9 - Tranferir")
    print("10 - Imprimir Histórico")
    print("11 - Imprimir Contas")
    
def Operacao_1():
    nome = str(input('Nome: ')).strip()
    cpf = str(input('CPF: ')).strip()
    dia = str(input('Dia de nascimento: ')).strip()
    mes = str(input('Mês de nascimento: ')).strip()
    ano = str(input('Ano de nascimento: ')).strip()
    salario = float(input('Salário: '))

    nasc = dia + '/' + mes + '/' + ano

    return nome, cpf, nasc, salario

def Operacao_2():
    nome = str(input('Nome: ')).strip()
    cpf = str(input('CPF: ')).strip()
    dia = str(input('Dia de nascimento: ')).strip()
    mes = str(input('Mês de nascimento: ')).strip()
    ano = str(input('Ano de nascimento: ')).strip()
    profissao = str(input('Profissão: ')).strip()

    nasc = dia + '/' + mes + '/' + ano

    return nome, cpf, nasc, profissao

def Operacao_3():

    resp = str(input('Possui cadastro? [s / n]')).strip().lower()
    print("-"*20)

    if (resp in 's / n'):
        if (resp =='s'):
            cpf_cadastrado = str(input('Digite o CPF cadastrado: ')).strip()
            print("-"*20)
            
            try:
                Functions.verifica_cad(cpf_cadastrado)
                if(Functions.criar_conta_corrente(cpf_cadastrado)):
                    return True
            except:
                return False
                

        elif (resp == 'n'):
            print('Para criar uma conta, volte ao menu e realize seu cadastro!')
            return True

        print("-"*20)
    else:
        return False         

def Operacao_4():
    resp = str(input('Possui cadastro? [s / n]')).strip().lower()
    print("-"*20)

    if (resp in 's / n'):
        if (resp == 's'):
            cpf_cadastrado = str(input('Digite o CPF cadastrado: ')).strip()
            print("-"*20)
            
            try:
                Functions.verifica_cad(cpf_cadastrado)
                if(Functions.criar_conta_poupanca(cpf_cadastrado)):
                    return True
            except:
                return False
                

        elif (resp == 'n'):
            print('Para criar uma conta, volte ao menu e realize seu cadastro!')
            return True

        print("-"*20)
    else:
        return False

def Operacao_5():
    valor_mensal = float(input('Custo Mensal: '))
    valor_tot = float(input('Custo total: '))
    cpf_cadas = str(input('CPF cadastrado: ')).strip()
    
    print("-"*20)
    try:
        Functions.verifica_cad(cpf_cadas)
        Functions.criar_seguro(cpf_cadas, valor_mensal, valor_tot)
        return True
    except:
        return False

def Operacao_6():
    
    hist_trib = Functions.calc_tributacao()

    if (type(hist_trib) == list):
        for i in range(0, len(hist_trib)):
            print(f'{i + 1} tributação = {hist_trib[i]}')
            
def Operacao_7():
    print('CPFs com cadastro no banco e suas respectivas contas')
    print("-"*20)

    Functions.exibe_contas()
    cpf_op = str(input('CPF da conta: ')).strip()
    tipo_cont = int(input('Tipo de conta, [1] - Corrente | [2] - Poupança: '))
    valor = float(input('Valor a ser sacado: '))
    print("-"*20)

    if tipo_cont == 1:
        if(Functions.operacao(cpf_op, 7, valor, 'Conta Corrente')):
            return True
        else:
            print('Saldo insucifiente!')
            return False

    elif tipo_cont == 2:
        if(Functions.operacao(cpf_op, 7, valor, 'Conta Poupança')):
            return True

    else:
        return False

def Operacao_8():
    print('CPFs com cadastro no banco e suas respectivas contas')
    print("-"*20)

    Functions.exibe_contas()
    cpf_op = str(input('CPF da conta: ')).strip()
    tipo_cont = int(input('Tipo de conta, [1] - Corrente | [2] - Poupança: '))
    valor = float(input('Valor a ser depositado: '))
    print("-"*20)

    if tipo_cont == 1:
        if(Functions.operacao(cpf_op, 8, valor, 'Conta Corrente')):
            return True

    elif tipo_cont == 2:
        if(Functions.operacao(cpf_op, 8, valor, 'Conta Poupança')):
            return True

    else:
        return False
    
def Operacao_9():
    print('CPFs com cadastro no banco e suas respectivas contas')
    print("-"*20)

    Functions.exibe_contas()
    cpf_op_origem = str(input('CPF da conta de origem a ser realizada a operação: ')).strip()
    tipo_cont_origem = int(input('Tipo de conta, [1] - Corrente | [2] - Poupança: '))
    valor = float(input('Valor da transferência: '))
    cpf_op_destino = str(input('CPF da conta: ')).strip()
    tipo_cont_destino = int(input('Tipo de conta, [1] - Corrente | [2] - Poupança: '))
    print("-"*20)

    if tipo_cont_origem == 1 and tipo_cont_destino == 1:
        if(Functions.operacao_transfere(cpf_op_origem, cpf_op_destino, valor, 'Conta Corrente', 'Conta Corrente')):
            return True

    elif tipo_cont_origem == 1 and tipo_cont_destino == 2:
        if(Functions.operacao_transfere(cpf_op_origem, cpf_op_destino, valor, 'Conta Corrente', 'Conta Poupança')):
            return True
    
    elif tipo_cont_origem == 2 and tipo_cont_destino == 1:
        if(Functions.operacao_transfere(cpf_op_origem, cpf_op_destino, valor, 'Conta Poupança', 'Conta Corrente')):
            return True
    
    elif tipo_cont_origem == 2 and tipo_cont_destino == 2:
        if(Functions.operacao_transfere(cpf_op_origem, cpf_op_destino, valor, 'Conta Poupança', 'Conta Poupança')):
            return True
    else:
        return False

def Operacao_10():
    print('CPFs com cadastro no banco e suas respectivas contas')
    print("-"*20)

    Functions.exibe_contas()

    cpf_op = str(input('CPF para consulta: ')).strip()
    tipo_cont = int(input('Tipo de conta, [1] - Corrente | [2] - Poupança: '))
    print("-"*20)

    if tipo_cont == 1:
        if(Functions.historico_conta(cpf_op, 'Conta Corrente')):
            return True
    if tipo_cont == 2:
        if(Functions.historico_conta(cpf_op, 'Conta Poupança')):
            return True
    else:
        return False

def Operacao_11():
    print(f'Número de contas cadastradas: {Functions.get_num_contas}')
    print(f'Clientes cadastrados e suas contas: ')
    
    try:
        Functions.exibe_clientes()
        return True
    except:
        print('Nenhum cliente tem conta!')

while True:
    menu()
    operacao = int(input('Digite sua opção: '))
    print("-"*20)

    if (operacao == 0):
        break
    elif (operacao == 1):
        nome, cpf, nasc, salario = Operacao_1()

        funcionario = Funcionarios(nome, cpf, nasc, salario)
        
        print("-"*20)
        if funcionario.preenche_funcionario(funcionario):
            print("Operação Realizada Com Sucesso!")
        else:
            print("Erro na operação!")

    elif (operacao == 2):
        nome, cpf, nasc, profissao = Operacao_2()

        cliente = Clientes(nome, cpf, nasc, profissao)

        print("-"*20)
        if (cliente.preenche_clientes(cliente)):
            print("Operação Realizada Com Sucesso!")
        else:
            print("Erro na operação!")

    elif (operacao == 3):
        print("-"*20)
        
        if (Operacao_3()):
            print('Operação Realizada Com Sucesso!')
        else:
            print('ERRO AO ABRIR A CONTA!')

    elif (operacao == 4):
        print("-"*20)
        
        if (Operacao_4()):
            print('Operação Realizada Com Sucesso!')
        else:
            print('ERRO AO ABRIR A CONTA!')
    elif (operacao == 5):
        if (Operacao_5()):
            print("Operação Realizada Com Sucesso!")
        else:
            print("Erro na operação!")

    elif (operacao == 6):
        Operacao_6()
    elif (operacao == 7):
        if(Operacao_7()):
            print('Saque Realizado!')
        else:
            print('ERRO NO SAQUE!')
    
    elif (operacao == 8):
        if (Operacao_8()):
            print('Depósito Realizado!')
        else:
            print('Falha Ao Depositar')

    elif (operacao == 9):
        if (Operacao_9()):
            print('Transferencia Realizada!')
        else:
            print('Falha Na Transferencia!')

    elif (operacao == 10):
        try:
            Operacao_10()
        except:
            print('Falha Na Operação!')
    elif (operacao == 11):
        try:
            Operacao_11()
        except:
            print('Falha Na Operação') 