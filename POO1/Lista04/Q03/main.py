from funcoes import Func

def menu():
    print('-'*30)
    print(f'{"ELEVADOR":^30}')
    print('-'*30)
    print('[1] - Entra pessoa')
    print('[2] - Sai pessoa')
    print('[3] - Subir andar')
    print('[4] - Desce andar')
    print('[0] - Finaliza programa')
    print('-'*30)

capac_elev = int(input('Capacidade do elevador: '))
tot_and = int(input('Total de andares: '))

elevador = Func(tot_and, capac_elev)


while True:
    menu()
    op = int(input('Digite sua opção: '))
    if (op == 0):
        break

    elif (op == 1):
        if (elevador.verifica_espaco_entrada() == True):   
            elevador.entra_pessoa(1)

            print('Operação realizada com sucesso!!!')
        else:
            print('Elevador cheio!!!')
    
    elif (op == 2):
        if (elevador.verifica_espaco_saida() == True):
            elevador.sai_pessoa(-1)

            print('Operação realizada com sucesso!!!')
        else:
            print('ERRO! Não tem ninguem no elevador!')
    
    elif (op == 3):
        if (elevador.verifica_andar_subida() == True):
            elevador.sobe_andar(1)

            print('Operação realizada com sucesso!!!')
        else:
            print('ERRO! Já está no último andar')
    
    elif (op == 4):
        if (elevador.verifica_andar_descida() == True):
            elevador.desce_andar(-1)

            print('Operação realizada com sucesso!!!')
        else:
            print('ERRO! Você está no andar térreo!')