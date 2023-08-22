palavra = input("Digite uma palavra:")

if palavra == palavra[::-1]:
    print("Palindromas")

else:
    print("Não são palindromas")