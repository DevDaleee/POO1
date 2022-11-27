from pessoa import Pessoa

p1 = Pessoa('Dalessandro', 20)

p1.comer('uva')
p1.parar_comer()

print('\n')

p1.falar('Jogos Eletronicos')
p1.parar_falar()

print('\n')

print(p1.get_ano_nascimento())