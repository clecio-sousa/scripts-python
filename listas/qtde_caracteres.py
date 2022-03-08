caracter = []
qtde_consoante = 0

while True:

    i = input("Digite um caracter: ")
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':

        break

    qtde_consoante += 1
    caracter.append(i)

print(caracter)
