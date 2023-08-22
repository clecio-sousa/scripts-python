"""nome = "clecio sousa"
print(nome.split())
print(len(nome))
email = input("Digite seu email:")

for letra in nome:

    print(f'A letra {letra} apareceu {nome.count(letra)} X na frase')


email = input("Digite seu email:")
print('@' in email)

texto = input("Digite um texto:")

contador = texto.count('python')
print(contador)

print(texto.upper())
nome_invertido = texto[::-1]  # NOME INVERTIDO
print(nome_invertido)
print(texto.split())

contador_a = texto.count('a')
print(contador_a)

nome_completo = input("Digite seu nome completo:")

primeira_palavra = nome_completo.split()[0]
ultima_letra = nome_completo[-1]

print(primeira_palavra)
print(ultima_letra)"""

texto = input("Digite um texto: ")

substituto = texto.replace('a', 'z')
print(substituto)
