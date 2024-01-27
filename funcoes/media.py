"""def media(*numeros):
    return sum(numeros) / len(numeros)


resultado = media(10, 20, 30, 40)
print(resultado)
"""


def media(*lista):
    soma = 0
    qtde_numeros = 0

    for i in lista:
        soma += i
        qtde_numeros += 1

    return soma / qtde_numeros


resultado = media(10, 20, 30, 40)

print(resultado)
