import numpy as np
alunos = {}
n = int(input("1 - Adicionar um aluno, 2 - Consultar a média"))
if n == 1:
    while n > 0:
        nome = str(input())
        n1 = int(input())
        n2 = int(input())
        alunos[nome].append(n1)
        alunos[nome].append(n2)
        n = int(input("Deseja adicionar outro aluno? "))
        if n < 0:
            break
elif n == 2:
    con = str(input("Qual aluno deseja ver a média? "))
    if con in alunos:
        