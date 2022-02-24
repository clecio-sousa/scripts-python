nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
serie = input("Digite a serie do aluno: ")
soma_notas = 1
qtde_notas = 1
media = soma_notas/qtde_notas

#  Condicoes de aprovacao
aprovado = media >= 7
trabalho_extra = 7 >= media >= 5
recuperacao = 5 >= media >= 4
reprovado = media < 4
################################

while True:
    if aprovado:
        print(f"Aluno aprovado. Media: {media}")

    elif trabalho_extra:
        print(f"Aluno aprovado. Media: {media}")

    elif recuperacao:
        print(f"Aluno aprovado. Media: {media}")

    elif reprovado:
        print(f"Aluno aprovado. Media: {media}")

    notas = float(input("Digite a %dª nota do aluno (0 para sair):" % qtde_notas))
    qtde_notas += 1
    soma_notas = soma_notas + qtde_notas



