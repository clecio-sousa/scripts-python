notas = []
alunos = []
qtde_nota = 0
soma = 0
media = 0
aprovados = []

for i in range(1):
    alunos.append(input("Nome do aluno: "))

    for j in range(4):
        notas.append(float(input("Digite a %dª nota: " % (j + 1))))
        soma = soma + notas[j]
        qtde_nota += 1
        media = media + notas[j]

media = float(soma/qtde_nota)
if media >= 7.0:
    print("Aluno: {}".format(alunos))
    print(media)
else:
    print(media)







