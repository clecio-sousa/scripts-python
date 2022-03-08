par =[]
impar = []
total = []

while True:
    numero = int(input("Digite um numero :"))
    if numero == -1:
        break

    elif numero % 2 == 0:
        par.append(numero)
        par.append(total)

    elif numero % 2 != 0:
        impar.append(numero)
        impar.append(total)

print("Pares : {}".format(par))
print("Impares : {}".format(impar))
print("Total : {}".format(total))

