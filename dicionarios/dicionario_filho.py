clientes = {
    'cliente_01': {
        'nome': 'Clecio',
        'sobrenome': 'Sousa',
    },
    'cliente_02': {
        'nome': 'Maria',
        'sobrenome': 'Jesus'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')

    for dados_k , dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


