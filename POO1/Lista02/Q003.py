def procura_c(letra, palavra):
    for i in range(0, len(palavra)):
        if letra == palavra[i]:
            return i

palavra = 'Teste'

c = str(input('Digite o caracter a ser procurado na palavra Teste: '))

print(f'Posição: {procura_c(c, palavra)}')