
'''
#Questao do slide com filter e reduce e lambda
import functools as ft

lista = [1, 2, 3, 4, 5, 6]

par = filter(lambda n: n%2==0 , lista)
soma = ft.reduce(lambda x, y: x+y , par)

print(soma)
'''

'''
#lista compreensiva
pares = [x+1 for x in range(0, 50) if x%2==0]

print(pares)
'''

''' 
n = 11
divisores = [x for x in range(1,n+1) if n%x == 0]
if len(divisores) <= 2:
    print(n, 'é primo')
else:
    print(n, 'não é primo')

print(divisores)
'''

''' 
#Exemplo tuplas
lista = ['elemento1', 'elemento2']
tupla = (1,2,3, 4, 5, True, 'flavio', lista)
lista2 = [1, 2, tupla]

lista.append('elemento3')
lista.pop(0)


print(tupla)
print(lista2)

print(lista2[2][-1][0])
'''

''' 
#Exemplos de conjutos
frutas = {'pera', 'uva', 'banana', 'banana', 'pera', 'maca', 'goiaba'}
numeros = {1,0, 44, 2, 3, 4, 5, 15, 10, 13}
letras = set('abacaxi')
letras2 = set('abacate')

print(letras & letras2)
'''

'''
#Gerar numeros aleatorios com lista compreensiva 
from random import randint

lista = [randint(0,9) for x in range(0,20)]

print(lista)
'''

'''
#Exemplo de dicionarios
dicionario = {'nome': [], 'idade': 31, 'sexo': 'm'}

dicionario['idade'] = 25

dicionario['nome'].append('Flavio')
dicionario['nome'].append('Jose')
print(dicionario['nome'])

dicionario['nome'][0] = 'Henrique'

for i in dicionario['nome']:
    print('lista = ', i)

print(dicionario)

for key, value in dicionario.items():
    print('A chave é = ', key)
    print('O valor é = ', value)
'''

''' 
#Passagem de varios parametros 
def teste(arg, *args):
    print(arg)
    for i in args:
        print(i)

def teste2(**kwargs):
    print(kwargs)
    print(kwargs['idade'])

teste2(nome='flavio', idade=31, sexo='m')
'''

dicionario = {}

#for i in range(0,2):
#    cpf = input('Digite o cpf: ')
#    nome = input('Digite o nome: ')
#    idade = int(input('Digite a idade: '))

#    dicionario[cpf] = [nome, idade]

dicionario = {'123': ['flavio', 31],
              '321': ['henrique', 16],
              '111': ['jose', 18],
              '222': ['maria', 15],
              '333': ['pedro', 20]}

#maiores = [lista[0] for lista in dicionario.values() if lista[1] >= 18]
maiores = [[cpf, lista[0]] for cpf, lista in dicionario.items() if lista[1] >= 18]

print(maiores)
