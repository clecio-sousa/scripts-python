meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']


while True:
    mes = int(input(" Digite um mes (1-12): "))
    if 1 > mes > 12:
        print(f"Mes invalido:{mes}")
        continue

    elif 1 <= mes < 13:
        print("O mês é: {} ".format(meses[mes - 1]))





