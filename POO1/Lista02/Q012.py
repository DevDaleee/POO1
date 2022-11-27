corrida = {
    'Zuquinha': [],
    'Perigoso': [],
    'Relampago marquinhos': [],
    'Toretto': [],
    'Sabinelson': []
}
menor_tempo = 0
menor_volta = []
medias = []
soma_t = 0
# Aramazenando tempo de corrida
for chave, valor in corrida.items():
    print(f'corredor -> {chave}')
    for i in range(1, 4):
        tempo = float(input(f'Volta {i} - tempo em s: '))
        soma_t += tempo

        if i == 1:
            menor_tempo = tempo
        elif (tempo < menor_tempo):
            menor_tempo = tempo
            num_volta = i

        valor.append(tempo)

    medias.append(soma_t / 3)

    menor_volta.append(menor_tempo)
    menor_tempo = 0
    soma_t = 0
    print('-' * 25)

#Imprime saída
j = 0
for chave, valor in corrida.items():
    for i in valor:
        if (min(menor_volta) == i):
            print('Melhor volta: ')
            print(f'{chave}')
            print(f'N° da volta: {valor.index(i) + 1}')

    if (medias.index(max(medias)) == j):
        print('-' * 25)
        print('CAMPEÃO!!!')
        print(f'{chave}')
        print(f'Média de tempo em s -> {max(medias):.1f}')
        print('-' * 25)
    j += 1