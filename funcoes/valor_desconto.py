def porcentagem(valor):
    valor_sem_desconto = valor * 0.7

    return valor_sem_desconto


resultado = porcentagem(121)
print(f'Valor com desconto:{resultado:.2f}')
