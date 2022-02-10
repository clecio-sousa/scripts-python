usuario = input("Nome de usuário:")
senha = input("Digite a senha:")

usuario_bd = 'clecio'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print("Você está logado!!!")

else:
    print("Usuário ou senha inválido")