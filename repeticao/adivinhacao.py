import random

numero_secreto = random.randint(1, 10)

tentativas = 3

while True and tentativas > 0:
    tentativa = int(input("Digite um numero:"))
    if numero_secreto == tentativa:
        print("Voce acertou o numero secreto:{}".format(numero_secreto))
        break

    elif tentativa < numero_secreto:
        print("O numero secreto é maior")
    else:
        print("O numero secreto é menor")

    tentativas -= 1
    print(f"Voce tem mais {tentativas} tentativas ")
