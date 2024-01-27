def aplica_desconto(produtos: dict, desconto: float):
    resultado = {}

    for nome_produto, valor in produtos.items():
        resultado[nome_produto] = f'{valor * (1 - desconto): .2f}'

    return resultado


valores_produtos = {
    'microondas': 497.99,
    'computador': 3499.97,
    'forno': 399.97
}

print(aplica_desconto(valores_produtos, 0.15))

