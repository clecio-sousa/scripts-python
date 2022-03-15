lista = []
lista_acima_media = []
numero = 1
soma = 0

while True:
    i = float(input(" Digite o %dº número: " % numero))
    if i == -1:
        break
    soma = soma + i
    numero += 1
    lista.append(i)


print("Quantidade de valores lidos: {}" .format(len(lista)))
for j in lista:
    print(j, end='-')

print("\n")
for z in lista:
    lista.sort(reverse=True)
media = soma/numero

for m in lista:
    if m > media:
        lista_acima_media.append(m)

print(lista)
print("Soma dos valores : {}".format(soma))
print("Media dos valores : {}".format(media))
print("Notas acima da média: {}".format(lista_acima_media))
