

'''
#questao 12
dicionario = {'flavio': [2, 3, 5], 'Henrique': [3, 10, 4], 'Jose': [4, 1, 6]}

nome_menor_tempo = list(dicionario.keys())[0]
melhor_volta = min(list(dicionario.values())[0])

nome_campeao = list(dicionario.keys())[0]
media_campeao = sum(list(dicionario.values())[0])/len(list(dicionario.values())[0])

for chave, valores in dicionario.items():
    if melhor_volta > min(valores):
        nome_menor_tempo = chave
        melhor_volta = min(valores)

    if media_campeao > sum(valores)/len(valores):
        nome_campeao = chave
        media_campeao = sum(valores)/len(valores)

print(nome_menor_tempo, melhor_volta)
print(nome_campeao, media_campeao)
'''


def menu():
    print('1 - Adicionar pessoa')
    print('2 - Incluir telefone')
    print('3 - Excluir telefone')
    print('4 - Excluir nome')
    print('5 - Consultar telefone')
    return int(input('Digite uma opção: '))

def incluirNovoNome(nome, telefone):
    agenda[nome] = [telefone]
    print('Nome adionado com sucesso!\n')

def incluirTelefone(nome, telefone):
    if nome in agenda.keys():
        agenda[nome].append(telefone)
        print('Telefone adicionado com sucesso!\n')

def imprimirAgenda():
    for nome, telefones in agenda.items():
        print(nome, ' Telefones: ', telefones)

def excluirTelefone(nome, telefone):
    if nome in agenda.keys():
        agenda[nome].remove(telefone)
        if len(agenda[nome]) == 0:
            p = agenda.pop(nome)
    else:
        print('Nome não está na agenda!\n')

agenda = {}
while True:
    op = menu()

    if op == 1:
        nome = input('Digite um nome: ')
        telefone = input('Digite um telefone: ')
        incluirNovoNome(nome, telefone)
    elif op == 2:
        nome = input('Digite um nome: ')
        telefone = input('Digite um telefone: ')
        incluirTelefone(nome, telefone)
    elif op == 3:
        nome = input('Digite um nome: ')
        telefone = input('Digite um telefone: ')
        excluirTelefone(nome, telefone)

    elif op == 5:
        imprimirAgenda()
