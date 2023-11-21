soma = 0

#codigo = int(input("Digite o código do produto:"))  NAO É AQUI!!

while True:
    codigo = int(input("Digite o código do produto:"))  # É AQUI!!

    if codigo == 1 or codigo == 2 or codigo == 3 or codigo == 5 or codigo == 9: # AQUI TROCA AND POR OR E COLOCA ==
        """print("Código inválido")
        codigo = int(input("Digite o código do produto"))"""
        quantidade = int(input("Digite a quantidade"))

        if codigo == 1:
            preco = quantidade * 0.50
            soma = soma + preco
        # print(preco)

        elif codigo == 2:

            preco = quantidade * 1.00
            soma = soma + preco
        # print(preco)

        elif codigo == 3:

            preco = quantidade * 4.00
            soma = soma + preco

        # print(preco)

        elif codigo == 5:

            preco = quantidade * 7.00
            soma = soma + preco

            # print(preco)

        elif codigo == 9:

            preco = quantidade * 8.00
            soma = soma + preco

            # print(preco)
    elif codigo == 0:
        break



print(soma)