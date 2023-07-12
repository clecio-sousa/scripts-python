distancia = float(input("Distancia percorrida pelo usuário: "))

if distancia <= 200:
    valor = distancia * 0.5

else:
    valor = distancia * 0.45

print(f'Valor da corrida: {valor}')