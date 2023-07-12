minutos = int(input("Quantos minutos voce utilizou por mês:"))

valor_15 = minutos * 0.15
valor_18 = minutos * 0.18
valor_20 = minutos * 0.20

if minutos < 200:
    print(f'Valor total: {valor_20}')

elif 200 <= minutos <= 400:
    print(f'Valor total: {valor_18}')

elif minutos > 400:
    print(f'Valor total: {valor_15}')


