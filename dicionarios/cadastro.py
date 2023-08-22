cadastro = {
    'id': 1,
    'nome': 'Clecio Sousa',
    'filhos': ['joana', 'sara'],
    'compras': [
        {'id': 4758,
         'produto': 'notebook',
         'preco': 2597.99

         }
    ]
}

print(cadastro['nome'])
print(cadastro['filhos'])
print(cadastro['compras'][0])

print(f'O usuário {cadastro["nome"]} realizou a seguinte compra {cadastro["compras"][0]["produto"]}')