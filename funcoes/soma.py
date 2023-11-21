"""def soma(num_1, num_2):
    return num_1 + num_2


resultado = soma(35, 36)
print(resultado)
"""


def soma_args(maximo, *numeros):
    resultado = 0
    numeros_somados = []

    for numero in numeros:
        if (resultado + numero) > maximo:
            break

        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados


soma_resultado, numeros_somados = soma_args(100, 1, 25, 489)
print(soma_resultado)
print(numeros_somados)
