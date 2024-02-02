def conta_caracteres(texto):
    contagem = {}

    for i in texto:

        if i in contagem:
            contagem[i] += 1

        else:
            contagem[i] = 1

    return contagem


resultado = conta_caracteres('banana')
print(resultado)
