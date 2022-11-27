def media(var):
    resultado = 0 
    tresultado = sum(resultado) / len(var)
    return tresultado

def mediana(var):
    var.sort()
    tamanho = len(var)
    if tamanho  % 2 == 0:
        posicomeio = tamanho  / 2
        posd = posicomeio+1
        resultado = (var[posicomeio]+var[posd])/2
        return resultado
    elif tamanho  % 2 != 0:
        meio = len(var) // 2
        return var[meio]

def variancia(var):
    aaa = media(var)
    resultado = 0
    for x in range(len(var)):
        resultado += ((var[x] - aaa) ** 2)
    resultadoo = resultado / len(var)
    return resultadoo-1

def d_padrao(var):
    raiz = variancia(var) ** 0.5
    return raiz

s = list(range(1,100))

print("Media é: ", media(s))
print("Mediana é: ", mediana(s))
print("Variancia é: ", variancia(s))
print("Desvio Padrão é: ", d_padrao(s))