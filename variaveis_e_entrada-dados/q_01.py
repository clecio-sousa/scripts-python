a = 4
b = 10
c = 5.0
d = 1
f = 5

print(a==c)
print(a < b)
print(d > b)
print(c != f)
print(a==b)
print(c < d)
print(b > a)
print("\n")

print("OPERADORES LOGICOS")
print(not True)
print(not False)
print(True and True)
print(True and False)
print(True or True)
print(False or True)

salario = float(input("Digite o salario: \n"))

if(salario > 1200):
    print(f"PAGUE IMPOSTO {salario}")
    print("PAGUE IMPOSTO{}".format(salario))

else:
    print(f"Nao precisa pagar imposto {salario}")
    print("Nao precisa pagar imposto. Salario: {}".format(salario))

          