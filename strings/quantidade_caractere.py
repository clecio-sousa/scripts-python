nome = input("Digite um nome: ")

for i, letra in nome:
    if nome[i] == letra:
        print(nome.count(letra), letra)
