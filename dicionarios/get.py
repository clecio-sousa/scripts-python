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


filho = cadastro.get('filho', None)
print(filho)