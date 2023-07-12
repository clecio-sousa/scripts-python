valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
qtde_anos_pagar = int(input("Quantidade de anos a pagar:"))

prestacao = valor_casa / (qtde_anos_pagar * 12)
if prestacao > salario * 0.3:



    print("EMPRESTIMO NÃO APROVADO\n"
            f"SALARIO: {salario}\n"
            f"PRESTAÇÃO: {prestacao:.2f}")
else:

     print('-------------------------\n'
            f'VALOR DA PRESTAÇÃO: {prestacao:.2f}')