lista = []


def maior(*numeros):
    for i in numeros:
        lista.append(i)

    return max(lista)


resultado = maior(1, 5, 8, 78, 789, 58, 47)
print(resultado)
