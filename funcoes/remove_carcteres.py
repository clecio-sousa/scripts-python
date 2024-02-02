def remove_caracteres(texto, *lista):
    for i in lista:
        texto = texto.replace(i, '')

    return texto


resultado = remove_caracteres('clecio', 'c', 'e')
print(resultado)
