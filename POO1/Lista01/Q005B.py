#Combinção
def fatorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * fatorial(n-1)
         
n = int(input())
r = int(input())
combinacao = fatorial(n)/fatorial(r)*fatorial(n-r)
print(combinacao)