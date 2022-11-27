from pessoa import Agenda

def menu():
    print('-' * 30)
    print('MENU DE OPÇÕES')
    print('-' * 30)

    print('[1] - Armazena pessoa')
    print('[2] - Remove pessoa')
    print('[3] - Busca pessoa')
    print('[4] - Imprime agenda')
    print('[0] - Sair')
    print('-' * 30)

agenda_dic = {}

pessoa = 0
while True:
    if pessoa == 10:
        print('Sua agendas está cheia, exclua um nome para adicionar mais')
        break
    
    menu()
    op = int(input('Digite sua opção: '))
    print('\n')

    if (op == 0):
        break
    elif (op == 1):
        pessoa += 1

        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        altura = float(input('Altura: '))
        print('\n')

        agenda = Agenda(nome, idade, altura)
        agenda_dic[pessoa] = agenda
        print('Salvo com sucesso!')

    elif (op == 2):
        agenda.listar_ag(agenda_dic)
        nome = str(input('Nome a ser excluído: '))
        print('\n')

        if (agenda.exclui(agenda_dic, nome)):
            print('Nome Excluido com sucesso')
            pessoa -= 1
        else:
            print('Pessoa não encontrada')
    
    elif (op == 3):
        nome = str(input('Nome da pessoa a ser procurada: '))
        print('\n')
        
        if (agenda.busca(agenda_dic, nome)):
            print('Operação concluida')
        else:
            print('Pessoa não encontrada!')
    
    elif (op == 4):
        agenda.listar_ag(agenda_dic)