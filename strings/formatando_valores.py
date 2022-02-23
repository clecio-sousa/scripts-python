"""
FORMATANDO VALORES

:s - TEXTO(strings)
:d - Inteiros(int)
:f - Ponto flutuante (float)
:.(numero)f - QTDE de casas decimais




num_1 = 1
num_2 = 3

divisao = num_1 / num_2

print(f"{divisao:.2f}")
print("{:.2f}".format(divisao))
print(len(f"{num_1:0>1}.")) #  adiciona 9 casas a esquerda
print(f"{num_2:0<10}") #  adiciona 9 casas a direita

nome = "Clecio"
sobrenome = "Sousa"
nome_formatado = '{} {}'.format(nome, sobrenome)
print(nome_formatado.lower())
print(nome_formatado.upper())"""

texto = 'Clecio Sousa'
print(texto[5:])

