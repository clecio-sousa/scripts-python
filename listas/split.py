"""
SPLIT - separar palavras dentro de uma frase
"""

frase = " o Brasil é o pais do futebol futebol futebol"
lista = frase.split()

palavra = ''
contagem = 0

for valor in lista:
    qtde_vezes = lista.count(valor)  # variavel recebe a qtde de palavras q a frase possui

    if qtde_vezes > contagem:
        contagem = qtde_vezes
        palavra = valor
        print(palavra, " - ", contagem)



