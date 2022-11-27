def tamanhoS(var):
    contador = 0 
    for x in var:
        contador+=1
    return contador
var = input()
print(tamanhoS(var))