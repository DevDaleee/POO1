from random import randint

n = randint(0,100)
tentativas = 0
print("Acerte o Número q estou pensando")

while tentativas < 10:
    t = int(input())
    if t > n:
        print("Menor")
        tentativas+=1
    elif t < n:
        print("Maior")
        tentativas+=1
    elif t == n:    
        print("Acertou em {} tentativas".format(tentativas))
        break
    