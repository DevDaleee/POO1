from random import randint
from time import sleep

cartoes = dict()
aposta = list()
gabarito_lot = []

def gera_gabarito():
    gabarito = []
    for i in range(13):
        gabarito.append(randint(1, 3))
    return gabarito

def gera_aposta(resposta):
    resposta = []
    for i in range(13):
        resposta.append(randint(1, 3))
    return resposta

def gera_cartoes(cartoes):
    for i in range(1, 4):
        cartoes[i] = gera_aposta(aposta)

def confere_acertos(apostador, result):
    acerto = 0
    for i in range(len(apostador)):
        for j in range(len(result)):
            if ((i == j) and (apostador[i] == result[j])):
                acerto += 1
    return acerto

def confere_aposta(n_acertos):
    if (n_acertos == 13):
        print('Ganhou!')



gabarito_lot = gera_gabarito()
gera_cartoes(cartoes)

# MENU
print(f'GABARITO DA LOTERIA: {gabarito_lot}\n')
print('Verificando apostas...')
print('-' * 25)
sleep(3)

# Mostra resultados
for chave, valor in cartoes.items():
    print(f'Apostador {chave}')

    acertos = confere_acertos(valor, gabarito_lot)
    print(f'Número de acertos: {acertos}')
    confere_aposta(acertos)
    print(valor)
    print('-' * 25)