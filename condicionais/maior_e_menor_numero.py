num_1 = int(input("Digite o 1º numero:"))
num_2 = int(input("Digite o 2º numero:"))
num_3 = int(input("Digite o 3º numero:"))

maior = num_1

if(num_2 > maior and num_2 > num_3 ):
    print("Maior numero: {} ".format(num_2))

elif(num_3 > maior and num_3 > num_2):
    print("Maior numero: {} ".format(num_3))

else:
    print("Maior numero: {} ".format(num_1))



