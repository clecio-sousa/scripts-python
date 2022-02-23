deposito_inicial = float(input("Digite o valor do deposito inicial: "))
tx_juros = float(input("Taxa de juros: "))
qtde_parcelas = int(input("Digite a quantidade de parcelas: "))
parcela = 1


while parcela <= qtde_parcelas:
    deposito_inicial = deposito_inicial + (deposito_inicial * (tx_juros / 100))
    print(f"{parcela}ª Parcela: R${deposito_inicial:8.2f}")
    parcela += 1

print(f"novo valor: R${deposito_inicial:8.2f}")
