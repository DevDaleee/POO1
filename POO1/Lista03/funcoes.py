from conta import Pessoa
from titular import Conta

def menu():
    print('-' * 30)
    print('Contas disponíveis: \n')
    c.listar_contas(contas)
    print('-' * 30)

contas = {}

while True:
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print('[1] - Criar conta')
    print('[2] - Listar contas')
    print('[3] - Sacar valor')
    print('[4] - Depositar valor')
    print('[5] - Realizar transferência')
    print('[6] - Consultar Histórico')
    print('[7] - Excluir conta')
    print('[0] - Sair')
    print('-' * 30)
    resp = int(input('Digite sua opção: '))

    if (resp == 0):
        break
    elif (resp == 1):
        nome = str(input('Digite o nome do titular da conta: ')).strip()
        cpf = str(input('Digite o CPF: ')).strip()
        tit = Conta(nome, cpf)
        c = Pessoa(tit, '', 0.0)

        numero = c.criar_conta('')
        if (numero not in contas):    
            contas[numero] = c
        else:
            while (numero in contas):
                numero = c.criar_conta('')
            contas[numero] = c

    elif (resp == 2):
        print('-' * 30)
        print()

        if (len(contas) == 0):
            print('Nenhuma conta existente!')
        else:
            c.listar_contas(contas)
        print('-' * 30)

    elif (resp == 3):
        menu()
        numsc = str(input('Número da conta para saque: ')).strip()
        
        if numsc in contas:
            valor = float(input('Digite o valor: R$'))
            print('-' * 30)

            if(contas[numsc].sacar(valor)):
                print('Saque efetuado com sucesso!')
            else:
                print('Saldo insuficiente.')
        else:
            print('Conta inválida!')
        print('-' * 30)

    elif (resp == 4):
        menu()
        numdp = str(input('Número da conta para depósito: ')).strip()

        if numdp in contas:
            valor = float(input('Digite o valor: R$'))
            print('-' * 30)

            if(contas[numdp].depositar(valor)):
                print('Depósito efetuado com sucesso!')
            else:
                print('Valor inválido!')
        else:
            print('Conta inválida!')
        print('-' * 30)

    elif (resp == 5):
       menu()

       c_origem = str(input('Número da conta de origem: ')).strip()
       c_destino = str(input('Número da conta de destino: ')).strip()

       if (c_origem in contas and c_destino in contas):
            val_transf = float(input('Valor a ser transferido: R$'))
            print('-' * 30)

            if(contas[c_origem].transfere_para(contas[c_destino], val_transf)):
                print('Transferência realizada com sucesso!')
            else:
                print('ERRO! Saldo insuficiente na conta de origem.')
       else:
            print('Conta inválida!')
       print('-' * 30)

    elif (resp == 6):
        menu()
        n_conta = str(input('Número da conta para consulta de histórico: ')).strip()
        print('-' * 30)

        if (n_conta in contas):
            contas[n_conta].historico.imprime_t()
        else:
            print('Conta inválida!')
        print('-' * 30)

    elif (resp == 7):
       menu()

       numex = str(input('Número da conta a ser excluída:'))
       print('-' * 30)

       if contas[numex].saldoc > 0:
            print('Saque o valor presente na conta para excluir!')
       else:
            contas.pop(numex)
            print('Conta excluída com sucesso!')
       print('-' * 30)