palavra_secreta = "deus"
digitadas = []
chances = 3


while True:
    if chances == 0:
        print("Você perdeu!!!")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:  # verifica se o usuario digitou mais de uma letra
        print("Isso não vale!!! Tente novamente")
        continue

    digitadas.append(letra)  # acrescenta a letra dentro da lista digitadas

    if letra in palavra_secreta:
        print("Vc acertou")

    else:
        print(f"A letra {letra} não existe na palavra secreta ")
        digitadas.pop()

    palavra_revelada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            palavra_revelada = palavra_revelada + letra_secreta
        else:
            palavra_revelada += '*'

    if palavra_revelada == palavra_secreta:
        print(f"Parabens! Vc acertou. A palavra secreta é {palavra_revelada}")
        break
    else:
        print(f"A palavra secreta está assim: {palavra_revelada}")

    if letra not in palavra_secreta:
        chances = chances - 1

    print(f"Vc ainda tem {chances} chances")
print("Palavras digitadas: {}".format(digitadas))





