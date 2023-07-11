print("*************************")
print("*  JOGO DA ADIVINHAÇÃO  *")
print("*************************")

numero_secreto = 42
numero = 75

segundo_numero = 32
triplo = 4
terceiro = 89
nome = 'clecio'
sobre_nome = 'clecio'




chute = int(input("Digite seu número:"))
print("Você digitou {}".format(chute))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print("Vc acertou. Numero secreto: {} ".format(numero_secreto))

elif maior:
    print("Vc errou!!! O numero secreto é menor!!!")

elif menor:
    print("Vc errou!!! O Numero secreto é maior!!!")
