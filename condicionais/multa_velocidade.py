velocidade = float(input("Digite a velocidade do carro:"))

velocidade_permitida = 80

velocidade_maior = velocidade > 80
valor_multa = (velocidade - velocidade_permitida) * 5

if velocidade_maior:
    print(f'Você levou multa por exceder velocidade. \n'
          f'Velocidade registrada: {velocidade}\n'
          f'Velocidade permitida: {velocidade_permitida}\n'
          f'---------------------------\n'
          f'VALOR TOTAL DA MULTA:{valor_multa}')

else:
    print(" Você não foi multado.")