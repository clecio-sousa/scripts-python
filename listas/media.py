notas = []
soma_nota = 0
qtde_notas = 0

while True:
    i = float(input("Digite a nota: "))
    if i == -1:
        break
    notas.append(i)
    soma_nota += i
    qtde_notas += 1
    print(notas)
media = soma_nota/qtde_notas

print(notas)
print(media)