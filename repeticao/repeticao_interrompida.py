soma = 0
while True:
    numero = int(input("Digite um numero: "))

    if numero == 1:
        continue
    elif numero == 0:
        break
    soma += numero
print(soma)
