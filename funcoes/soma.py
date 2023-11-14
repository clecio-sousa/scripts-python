"""def soma(num_1, num_2):
    return num_1 + num_2


resultado = soma(35, 36)
print(resultado)
"""


def soma_args(maximo, *numeros):
    resultado = 0
    soma_numeros = []

    for numero in numeros:
        if (resultado + numero) > maximo:
            break

        resultado += numero
        soma_numeros.append(numero)

    return resultado, soma_numeros


soma_resultado, numeros_somados = soma_args(100, 20, 30, 40, 50)
print(soma_resultado)
print(numeros_somados)

