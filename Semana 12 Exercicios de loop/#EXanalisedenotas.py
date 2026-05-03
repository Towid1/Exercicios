#EXanalisedenotas
soma = 0
aprovados = 0
reprovados = 0

for i in range(6):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    if nota < 6:
        reprovados += 1
    elif nota >= 6:
        aprovados += 1

print(f"A média da turma é de {soma/6}. Tiveram {aprovados} alunos aprovados e {reprovados} alunos reprovados.")