print("----------TABUADA----------")
opcao = int(input("ESCOLHA A OPERAÇÃO DESEJADA:\n"))

"1 - ADIÇÃO\n"
"2 - SUBTRAÇÃO\n"
"3 - MULTIPLICAÇÃO\n"
"4 - DIVISÃO\n" \
"5 - SAIR"

tabuada = int(input("TABUADA DE: "))
numero = 1

while True:
    if opcao == 5:
        break
    while numero <= 10:

        if opcao == 1:
            print(f"{tabuada} + {numero} = {tabuada + numero}")
        elif opcao == 2:
            print(f"{tabuada} - {numero} = {tabuada - numero}")
        elif opcao == 3:
            print(f"{tabuada} * {numero} = {tabuada * numero}")
        elif opcao == 4:
            print(f"{tabuada} / {numero} = {tabuada/numero}")

        numero += 1







