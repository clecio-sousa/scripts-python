numeros = []
numero = 1
soma = 0
multiplicacao = 1
while True:
    i = int(input("Digite o %dº numero: " % numero))

    if i == -1:
        break
    numeros.append(i)
    soma += i
    multiplicacao = multiplicacao * i

    numero += 1


print("SOMA: {}".format(soma))
print("PRODUTO: {}".format(multiplicacao))
print("NUMEROS: {}".format(numeros))

