def conta_vogais(string):
    contador = 0

    vogais = "aeiou"

    for letra in string:
        if letra.lower() in vogais:
            contador += 1

    return contador


resultado = conta_vogais('jabuticaba')
print(resultado)
