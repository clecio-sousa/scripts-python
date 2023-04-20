numero_1 = int(input("Digite o 1º numero:"))
numero_2 = int(input("Digite o 2º numero:"))


print("\t\tCALCULADORA\n"
      "DIGITE A OPERAÇÃO DESEJADA\n"
      " + - SOMA\n"
      " -   SUBTRAÇÃO\n"
      " * - MULTIPLICAÇÃO\n"
      " / - DIVISÃO\n"
      )

operacao = input("Digite a operação")
equacao = f'{numero_1} {operacao} {numero_2}'
resultado = eval(equacao)

print(f'Resultado: {resultado}')