from time import sleep

agenda = {}
telefones = []

def menu():
    print(f'-' * 30)
    print(f'{"MENU DE OPÇÕES":^30}')
    print(f'-' * 30)
    print('[ 1 ] - Incluir novo nome')
    print('[ 2 ] - Incluir novo telefone')
    print('[ 3 ] - Excluir telefone')
    print('[ 4 ] - Excluir nome')
    print('[ 5 ] - Consultar telefone')
    print('[-1 ] - Sair')
    print(f'-' * 30)

def incluir_nome(nome, telefones):
    for chave, valor in agenda.items():
        if (chave == nome):
            for i in telefones:
                valor.append(i)
    print('ADICIONADO COM SUCESSO!!!')

def incluir_telefone(nome, telefones):
    for chave, valor in agenda.items():
        if (chave == nome):
            for i in telefones:
                if (i not in valor):
                    valor.append(i)
    print('ADICIONADO COM SUCESSO!!!')  

def excluir_telefone(nome, telefone):
    for chave, valor in agenda.items():
        if (chave == nome):
            if (len(valor) > 1):
                valor.remove(telefone)
            elif(len(valor) == 1):
                del agenda[nome]
                break
    print('EXCLUÍDO COM SUCESSO!!!')

def excluir_pessoa(nome):
    del agenda[nome]
    print('EXCLUÍDO COM SUCESSO!!!')

def consultar_telefone(nome):
    if (nome not in agenda):
        print('PESSOA NÃO CONSTA NA AGENDA!!!')
        print('...')
        sleep(1.5)
    else:
        print('NÚMEROS:')
        for chave, valor in agenda.items():
            if (chave == nome):
                for i in valor:
                    print(i)
        print(f'-' * 30)
        print('CONCLUÍDO!!!')

while True:
    telefones.clear()
    menu()
    op = int((input('Digite sua opção: ')))

    if (op == 1):
        nome = str(input('Digite o nome: ')).strip()
        agenda[nome] = []
        n_telef = int(input('Digite quantos n° de telefone quer adiconar: '))

        for i in range(n_telef):
            telefone = str(input('Digite o n° de telefone: ')).strip()
            if (telefone not in telefones):
                telefones.append(telefone)
        
        print(f'-' * 30)
        print('Adicionando...')
        sleep(1.5)
        print(f'-' * 30)
        incluir_nome(nome, telefones)

    elif (op == 2):
        telefone = str(input('Digite o n° de telefone: ')).strip()
        telefones.append(telefone)
        nome = str(input('Digite o nome que deseja adicionar o novo número: ')).strip()

        if (nome not in agenda.keys()):
            print('Nome não existe na agenda, adicionando...')
            print(f'-' * 30)
            sleep(1.5)
            agenda[nome] = []
            incluir_nome(nome, telefones)
        else:
            print(f'-' * 30)
            print('Adicionando...')
            sleep(1.5)
            print(f'-' * 30)
            incluir_telefone(nome, telefones)

    elif (op == 3):
        telefone = str(input('Digite o n° de telefone a ser excluído: ')).strip()
        nome = str(input('Nome responsável pelo telefone: ')).strip()
        
        print(f'-' * 30)
        print('Excluindo...')
        sleep(1.5)
        print(f'-' * 30)
        excluir_telefone(nome, telefone)

    elif (op == 4):
        nome = str(input('Nome a ser excluído da agenda: ')).strip()

        print(f'-' * 30)
        print('Excluindo...')
        sleep(1.5)
        print(f'-' * 30)
        excluir_pessoa(nome)

    elif (op == 5):
        nome = str(input('Nome de quem deseja fazer a consulta na agenda: ')).strip()

        print(f'-' * 30)
        print('Pesquisando...')
        sleep(1.5)
        print(f'-' * 30)
        consultar_telefone(nome)

    elif (op == -1):
        break