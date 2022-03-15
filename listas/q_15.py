lista = []
numero = 1

while True:
    i = int(input(" Digite o %dº número: " % numero))
    if i == -1:
        break
    lista.append(i)
    numero += 1

print("Quantidade de valores lidos: {}" .format(len(lista)))
for j in lista:
    print(j, end='-', '\n')

for z in lista:
    print(z)
