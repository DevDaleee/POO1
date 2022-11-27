

'''
#Fatorial recursivo
def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n*fatorial(n-1)

fat = fatorial(5)
print(fat)
'''


'''
#Questão 6
def is_primo(n):
    cont=0
    for i in range(1,n+1):
        if n%i == 0:
            cont+=1

    if cont <= 2:
        return True
    else:
        return False

a = 10
b = 16

flag = False
for i in range(a, b+1):
    if is_primo(i):
        flag = True
        print(i)

if flag == False:
    print('Não tem primos no intervalo')
'''

'''
#Setima
d = 4

resto = 0
aux = 1
aux2 = 0
while d>=1:
    resto = d%2
    d = d//2
    aux2 = aux2 + aux*resto
    aux = aux*10

print(aux2)
'''

''' 
#Exemplo format
import math

f = float(input('digite real: '))

str = 'flávio henrique'
completo = '{a}, {b}, hdhddhdvdhv {c}'
expressao = 'pi = {:.2f}'

print(completo.format(a= 'primeiro', b= 'ultimo', c='hdhdhd'))
print(expressao.format(f))

'''

'''
#split
nome = 'flavio henrique ffssn jisji duarte'
res = nome.split(' ')
print(res)
'''

''' 
nome = ' Flavio '

if nome.upper().strip() == 'flavio'.upper():
    print('Nomes iguais ')


sobrenome = 'Duarte'

print(sobrenome.center(100))
'''

''' 
#Exemplo de funções de listas
lista = [1, 2, 3, 4, 5, 6.234, 'flavio', True]
lista.append(1)
lista.append('henrique')

print(lista[8:2:-2])

lista2 = [3, 4, -2, 1, 0]
lista2.sort()
print(lista2)

lista.extend(lista2)

print(lista)

'''

'''
#Questão ordenação
pares = []
impares = []
zeros = []

n = 0
while n >= 0:
    n = int(input('Digite um numero: '))

    if n < 0:
        break
    elif n == 0:
        zeros.append(n)
    elif n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()
print(pares + zeros + impares)
'''

''' 
#Questão de lista sorteio
import random

n1 = int(input('Intervalo1: '))
n2 = int(input('Intervalo2: '))
quant = int(input('Quantidade de sorteados: '))

sorteados = []
while len(sorteados) < quant:
    x = random.randint(n1, n2)
    if x not in sorteados:
        sorteados.append(x)

print(sorteados)
'''

'''
#uso do map
def metade(n):
    return n/2

lista = [1, 2, 3, 4]
resultado = map(metade, lista)
print(list(resultado))
'''

'''
#Uso do filter
def isZero(n):
    return n == 0

lista = [0, 1, 2, 0, 3, 4, 0]
resultado = filter(isZero, lista)
print(list(resultado))
'''

''' 
#questao com filter
def isZero(n):
    return n == 0

def isPar(n):
    return n%2==0 and n != 0

def isImpar(n):
    return n%2!=0

n = 0
lista = []
while n >= 0:
    n = int(input('Digite um numero: '))

    if n < 0:
        break
    lista.append(n)

pares = list(filter(isPar, lista))
impares = list(filter(isImpar, lista))
zeros = list(filter(isZero, lista))

pares.sort()
impares.sort()

print(pares + zeros + impares)
'''

''' 
import functools as ft

def soma(x,y):
    return x+y

lista = [1, 2, 3, 4, 5]
resultado = ft.reduce(soma, lista)

print(resultado)
'''

def isZero(x):
    return x == 0

lista = [1, 2, 3, 0, 0]
resultado = filter(lambda x: x==0, lista)
print(list(resultado))