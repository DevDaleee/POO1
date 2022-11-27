#Dicionarios são muito bons para armazenad infomações que precisam de algum tipo de identificador. Vejamos no exemplo

emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plaza@gamil.com",
    "Barra": "barra@gmail.com"
}
print("-"*30)
#Assim fica mais fácil de achar coisas em meio a listras grandes

#Caso eu queira pegar algum email expecifico, vejamos como fazemos
email = emails_gerentes["Iguatemi"]
print(email)
#ou
print(emails_gerentes["Iguatemi"])

print("-"*30)
#Se eu quiser adicionar outra coisa ao meu dicionario
emails_gerentes["Leblon"] = "lebron@gmail.com"
print(emails_gerentes)

print("-"*30)
#Mas e seu eu quiser descobrir todos os shoppings que temos?
#Existem duas formas
#Forma 1: For
for shopping in emails_gerentes:
    print(shopping)
print("-"*30)
#forma 2: dicionario.keys()
print(emails_gerentes.keys())

print("-"*30)
#Mas se eu quiser todos os valores?
#Forma 1: For
for shopping in emails_gerentes:
    email = emails_gerentes[shopping]
    print(email)

print("-"*30)
#Forma 2: dicionario.values
print(emails_gerentes.values())
print("-"*30)

#Mas e seu eu quiser Retirar um valor do meu dicionario
emails_gerentes.pop("Leblon")
print(emails_gerentes)

print("-"*30)
#Verificando se um valor existe no meu dicionario
if "Leblon" in emails_gerentes:
    print("Existe")
else:
    print("Não Existe")