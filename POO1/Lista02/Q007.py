lista1 = list(range(0,10))
lista2 = list(range(10,20))
lista3 = []
for x in range(10):
    resultado = lista1[x] + lista2[x]
    lista3.append(resultado)
print(lista3)