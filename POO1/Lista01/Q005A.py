#Arranjo
def fatorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * fatorial(n-1)
         
n = int(input())
p = int(input())
arranjo = fatorial(n)/ fatorial(n-p)
print(arranjo)