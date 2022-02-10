print("*************************")
print("*  JOGO DA ADIVINHAÇÃO  *")
print("*************************")

numero_secreto = 42

chute = int(input("Digite seu número:"))
print("Você digitou {}".format(chute))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Vc acertou. Numero secreto: {} ".format(numero_secreto))

elif(maior):
    print("Vc errou!!! O numero secreto é menor!!!")

elif(menor):
    print("Vc errou!!! O Numero secreto é maior!!!")
