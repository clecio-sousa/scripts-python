"""
for i in range(100):
    print(i+1)


for i in range(100, 0, -1):
    print(i)


for i in range(200):
    if i % 2 == 0:
        print(i)
        """

soma_pares = 0
contador_par = 0
contador_impar = 0
i = 25
while i <= 200:
    if i % 2 == 0:
        soma_pares = soma_pares + i
    i += 1
    print(soma_pares)