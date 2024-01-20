def multiplica(*args):
    total = 1
    for i in args:
        total *= i
        # print(total)
    return total


resultado = multiplica(2, 4, 6, 10)
print(resultado)


def numero(x):

    condicao = x % 2 == 0

    if condicao:
        return 'par', x
    else:
        return 'impar', x


print(numero(10))
