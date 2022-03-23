frase = input("Digite uma frase: ")
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

alterar_letra = input("Qual letra deseja colocar maiuscula?")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == alterar_letra:
        nova_frase += alterar_letra.upper()

    else:
        nova_frase += letra
    contador += 1

print(nova_frase)