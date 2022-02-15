qtde_kwh = float(input("Digite a quantidade de kilowatts:"))
tipo_instalacao = input("Digite o tipo de instalação:")



if(tipo_instalacao == 'r' and qtde_kwh <= 500):
    print("Preco a pagar: {}".format(qtde_kwh * 0.4))

elif(tipo_instalacao == 'r' and qtde_kwh > 500 ):
    print("Preco a pagar: {}".format(qtde_kwh * 0.65))

elif(tipo_instalacao == 'c' and qtde_kwh <= 1000):
    print("Preco a pagar: {}".format(qtde_kwh * 0.55))
elif(tipo_instalacao == 'c' and qtde_kwh > 1000):
    print("Preco a pagar: {}".format(qtde_kwh * 0.60))

elif(tipo_instalacao == 'i' and qtde_kwh <= 5000):
    print("Preco a pagar: {}".format(qtde_kwh * 0.55))

elif(tipo_instalacao == 'i' and qtde_kwh > 5000):
    print("Preco a pagar: {}".format(qtde_kwh * 0.60))

