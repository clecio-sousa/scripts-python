contador = 0
acumulador = 0
soma = 0

print("contador"+'|'+ "acumulador")

while contador <= 5:
    contador += 1
    acumulador += contador # ACUMULA OS NUMEROS DO IMPRESSOS NO CONTADOR
    soma = soma + acumulador
    print('\t', contador, '\t\t', acumulador)


print(f'TOTAL ACUMULADOR:{acumulador}')
print(f'TOTAL ACUMULADOR:{soma}')


