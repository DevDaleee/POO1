dados = dict()
agenda = list()

for i in range(0, 10):
    print('-' * 25)
    print(f'Contato {i + 1}')
    dados['Nome'] = str(input('Nome: '))
    dados['Telefone'] = str(input('Telefone: '))
    agenda.append(dados.copy())

print('-' * 25)
print()
print(f'{"AGENDA":^60}')
print('-' * 60)

agenda.reverse()
for key, elem in enumerate(agenda):
    print(f'Contato {key + 1}')
    for chave, valor in elem.items():
        print(f'{chave} --> {valor}')
    print()
    print('-' * 25)