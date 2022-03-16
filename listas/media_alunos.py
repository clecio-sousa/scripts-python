notas = []
alunos = []
qtde_nota = 0
soma = 0
acima_media = 0

for i in range(2):
    alunos.append(input("Nome do aluno: "))

    for j in range(4):
        notas.append(float(input("Digite a %dª nota: " % (j + 1))))
        soma += notas[j]
        qtde_nota += 1
        media = soma / qtde_nota

        if media >= 7:
            acima_media += 1

print("TOTAL ACIMA DA MEDIA: {}".format(acima_media))
