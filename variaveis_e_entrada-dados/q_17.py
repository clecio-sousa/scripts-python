valor = int(input("Digite o valor a ser sacado:"))

nota_50 = valor//50
nota_10 = (valor % 50)//10
nota_5 = (valor % 10)//5
nota_1 = (valor % 5)

print(f"Nota de 50: {nota_50}\n")
print(f"Nota de 10: {nota_10}\n")
print(f"Nota de 5: {nota_5}\n")
print(f"Nota de 1: {nota_1}\n")
