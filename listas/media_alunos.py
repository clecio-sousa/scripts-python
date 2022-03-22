notas = []
alunos = []
media = 0
soma = 0
qtde_notas = 0
acima_media = 0

#  leitura do nome dos alunos
for i in range(2):
    alunos.append(input("Nome do aluno: "))

    #  leitura das notas de cada aluno
    for j in range(4):
        notas.append(float(input("Digite a %dª nota: " % (j + 1))))

        media = media + notas[j]
        qtde_notas += 1

media = media / qtde_notas

if media > 7:
    acima_media = acima_media + 1


print("TOTAL ACIMA DA MEDIA: {}".format(acima_media))
