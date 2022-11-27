#Arrays em Python
#Lista é uma coleção ordenada e mutável. Permite membros duplicados.
#Nas Listas existem index
lista =  ["carro", True, 2, 3.5]
print(lista)
print(type(lista))
print(lista[1])

#Jeito legal de imprimir vários caracteres igual em Python
print("-"*30)

#Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
tupla = ("carro", True, 2, 3.5)
print(tupla)
print(type(tupla))
print(tupla[3])

print("-"*30)

#Dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado.
dicionario = {"nome":"carro", "logica": True, "numero": 2, "outroNumero":3.5}
print(dicionario)
print(type(dicionario))
print(dicionario["nome"])

print("-"*30)

#Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
conjunto = {"carro",True, 2, 3.5} 
print(conjunto)
print(type(conjunto))
print(conjunto[1])
