
numero_inicial = int(input("Digite o inicio da contagem: "))
numero_final = int(input("Digite o final da contagem: "))


while numero_inicial <= numero_final:
    par = numero_inicial % 2 != 0
    if par:
        print(numero_inicial)
    numero_inicial += 1
