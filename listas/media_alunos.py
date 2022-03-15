notas = []
alunos = []
qtde_nota = 0
soma = 0

for i in range(2):
    alunos.append(input("Nome do aluno: " + str(i + 1)))
    for j in range(4):

        notas.append(float(input("Digite a %dª nota: " % (j + 1))))
        soma += j
        qtde_nota += 1
        media = soma/qtde_nota
