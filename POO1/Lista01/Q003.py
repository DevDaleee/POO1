print("Digite T para Triangulo, Q para Quadrado e C para Circulo")
a = input()
if a == "T":
    c1 = int(input())
    c2 = int(input())
    h = (c1**2 + c2**2) ** (1/2)
    print(h)
    
elif a == "Q":
    b  = int(input())
    a = int(input())
    result = a * b
    print(result)
    
elif a == "C":
    r = int(input())
    result = 3.14 * (r**2)
    print(result)