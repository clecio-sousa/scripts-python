salario = float(input("Digite o valor do salario:"))

salario_aumento_10 = (salario * 0.10) + salario
salario_aumento_15 = (salario * 0.15) + salario

if salario >= 1250:
    print("Novo salário:{}".format(salario_aumento_10))

if salario < 1250:
    print("Novo salário:{}".format(salario_aumento_15))



