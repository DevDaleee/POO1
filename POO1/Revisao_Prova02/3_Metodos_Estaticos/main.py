from pessoa import Pessoa

p1 = Pessoa.por_ano_nascimento('Dalessandro', 2001)
p1 = Pessoa('Marcos', 45)

print(p1)
print(p1.nome, p1.idade)

p1.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())