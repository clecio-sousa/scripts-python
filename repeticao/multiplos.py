total_multiplos = int(input("Digite um numero: "))

x = 1
soma_multiplos = 0
while total_multiplos >= 1:
    if x % 3 == 0:
        print(x)
        x += 3
    total_multiplos -= 1
    soma_multiplos += x

print(soma_multiplos)
