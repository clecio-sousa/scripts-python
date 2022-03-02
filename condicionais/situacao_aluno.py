nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
serie = input("Digite a serie do aluno: ")

qtde_notas = 0
soma_notas = 0
questao = 1

while True:
    nota = float(input("Digite a %dº nota: " % questao))
    if nota == 0:
        break
    else:
        soma_notas += nota
        qtde_notas += 1
        questao += 1

media = float(soma_notas / qtde_notas)
aprovado = media >= 7
trabalho_extra = 5 <= media <= 7
recuperacao = 4 <= media <= 5
reprovado = media <= 4

if aprovado:
    print("APROVADO. PARABEnS. Media:{:.2f} ".format(media))
elif trabalho_extra:
    print("FAZER TRABALHO EXTRA. Media:{:.2f} ".format(media))

elif recuperacao:
    print("RECUPERAÇÃO. Media:{:.2f} ".format(media))

elif reprovado:
    print("REPROVADO. Media:{:.2f} ".format(media))

"""#  Condicoes de aprovacao
n1 = float(input("digite a nota: "))
n2 = float(input("digite a nota: "))
n3 = float(input("digite a nota: "))
n4 = float(input("digite a nota: "))

media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print("aprovado")
elif 5 <= media <= 7:
    print("trabalho extra")

elif 5 >= media <= 4:
    print("recuperacao")

elif media < 4:
    print("reprovado")
"""
