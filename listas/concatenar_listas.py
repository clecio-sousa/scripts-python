lista_a = []
lista_b = []
lista_inter = []

for i in range(10):
    lista_a.append(int(input("Digite o %dº numero: " % (i + 1) + '\n')))

for j in range(10):
    lista_b.append(int(input("Digite o %dº numero: " % (j + 1) + '\n')))

for k in range(10):
    lista_inter.append(lista_a[k])
    lista_inter.append(lista_b[k])
lista_inter.sort(reverse=False)
print(lista_a)
print(lista_b)
print(lista_inter)