frase = 'clecio sousa da silva'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
letra_usuario = input("Digite a letra a ser alterada: ")
while contador < tamanho_frase:
    # # print(frase[contador], contador)
    # nova_string += frase[contador]
    # print(nova_string)
    # contador += 1

    letra = frase[contador]
    if letra == letra_usuario:
        nova_string += letra_usuario.upper()

    else:
        nova_string += letra
    contador += 1

print(nova_string)
