from funcoes import Func

nome = str(input('Digite seu nome: ')).strip()
ano = str(input('ANO -  ')).strip()
mes = str(input('MÊS -  ')).strip()
dia = str(input('DIA - ')).strip()
nascimento = dia + '/' + mes + '/' + ano
altura = float(input('Altura: '))

pessoa = Func(nome, nascimento, altura)

pessoa.calc_idade(ano)
pessoa.Mdados()