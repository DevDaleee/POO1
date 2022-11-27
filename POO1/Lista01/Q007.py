def decimal_para_binario(decimal):
    binario = ''    
    while decimal > 0:
        binario+= str(decimal%2)
        decimal//= 2
    return binario[::-1]    

num = int(input())
print(decimal_para_binario(num))