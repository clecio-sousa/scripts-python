def dados():
    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereco: ")
    telefone = input("Digite seu telefone: ")

    return nome, endereco, telefone


resultado = dados()
print(resultado)
