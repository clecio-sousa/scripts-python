soma_numeros = 0
qtde_numeros = 0


while True:
    numero = int(input("Digite um numero: "))

    if numero == 0:
        break
    qtde_numeros = qtde_numeros + 1
    soma_numeros = soma_numeros + numero


media = float(soma_numeros/qtde_numeros)

print("QUANTIDADE DE NUMEROS DIGITADOS: {}".format(qtde_numeros))
print(f"SOMA DOS NUMEROS DIGITADOS: {soma_numeros}")
print("MEDIA:{}".format(media))

