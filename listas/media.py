notas = []
soma_nota = 0
qtde_notas = 0

while True:

    nota = float(input("Digite a nota: "))
    if nota == -1:
        break

    notas.append(nota)
    soma_nota += nota
    qtde_notas += 1
    print(notas)
media = soma_nota/qtde_notas


print(f"Quantidade de notas obtidas: {qtde_notas}")

print(f"Media do aluno: {media}")

