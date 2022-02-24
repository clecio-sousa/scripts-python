nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
serie = input("Digite a serie do aluno: ")


#  Condicoes de aprovacao
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

