deposito_inicial = float(input("Digite o valor do deposito inicial: "))
tx_juros = float(input("Taxa de juros: "))
qtde_parcelas = int(input("Digite a quantidade de parcelas: "))
parcela = 1
novo_valor = deposito_inicial

while parcela <= qtde_parcelas:
    novo_valor = novo_valor + (novo_valor * (tx_juros / 100))
    print(f"{parcela}ª Parcela: R${novo_valor:8.2f}")
    parcela += 1

print(f"novo valor: R${novo_valor:8.2f}")
