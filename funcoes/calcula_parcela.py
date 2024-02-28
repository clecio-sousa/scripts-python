def calcula_parcela(valor_total, qtde_parcelas, taxa_juros):
    valor_parcela = (valor_total / qtde_parcelas) * (1 + taxa_juros)
    return valor_parcela


resultado = calcula_parcela(100, 10, 3)
print(resultado)
