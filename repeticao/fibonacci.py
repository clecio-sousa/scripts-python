limite = int(input("Digite o limite da sequencia Fibonacci:"))  # 7

anterior = 0
atual = 1

while anterior <= limite:
    print(anterior)  # 0
    proximo = anterior + atual  # 0 + 1
    anterior = atual  # 1
    atual = proximo  # 1
