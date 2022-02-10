velocidade = float(input("Digite a velocidade do carro:"))

velocidade_permitida = 80

velocidade_maior = velocidade > 80

if(velocidade_maior):
    print("Carro multado. Sua velocidade {} .".format(velocidade))

else:
    print("O carro não foi multado")