import time

contagem = int(input("Digite um inicio da contagem regressiva:"))

while contagem > 0:
    print(contagem)
    time.sleep(1) # BIBLIOTECA TIME USADA PARA SIMULAR A CONTAGEM DE SEGUNDO EM SEGUNDO
    contagem -= 1

print("FOGO!!!")
