number = int(input('Numero: '))
ePrimo = 0

for i in range(1, (number + 1)):        
  if number % i == 0:
    ePrimo += 1
    
if ePrimo == 2 :
  print(True)
else:
  print(False)

com = int(input())
fim = int(input())

for com in range(fim):        
  if com % i == 0:
    print(com)
  # else:
  #   print("não primo")