num_1 = int(input("Digite um numero:"))
num_2 = int(input("Digite um numero:"))
num_3 = int(input("Digite um numero:"))

maior = num_1

if num_2 > maior:
    maior = num_2
if num_3 > maior:
    maior = num_3

print("Maior: {}".format(maior))

menor = num_1

if num_2 < menor:
    menor = num_2
if num_3 < menor:
    menor = num_3


print("Menor: {}".format(menor))