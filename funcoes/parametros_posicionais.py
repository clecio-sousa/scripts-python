def funcao_com_args(arg1, arg2, *args):
    print(f'Arg1: {arg1}')
    print(f'Arg2: {arg2}')
    print(f'*Args: {args}')


funcao_com_args(1, 2, 3, 4, 5)


def soma(*numeros):
    resultado = 0

    for numero in numeros:
        resultado += numero

    return resultado


resultado_soma = soma(1, 12, 32, 45, 48, 79, 489)

print(resultado_soma)
