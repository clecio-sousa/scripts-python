variavel = x, y, *resto = 1, 2, 3, 4, 5, 6

print(variavel)

"""
ARGS - empacotamento e desempacotamento
"""


def soma(*args):
    total = 0
    for i in args:
        total += i
        print(total)


soma(1, 2, 3, 4, 5, 6)
