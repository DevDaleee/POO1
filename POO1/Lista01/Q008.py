preco = 5
quantidade = 120
lucro = 400

while preco > 1:
  print("preço ingresso = {:.2f}, quantidade = {},  lucro = {:.2f}".format(preco, quantidade, lucro))
  preco-=0.5
  quantidade+=26
  ganho = preco * quantidade
  lucro = ganho - 200
  lucroa = lucro
  for i in range(6):
    if lucro > lucroa:
      lucromax = lucro
      precomax = preco
      quantidademax = quantidade
print("\nLucro Máximo = ", lucromax)
print("Preço do Ingresso = ", precomax)
print("Quantidade Vendida = ", quantidademax)
  