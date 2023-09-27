familia = {
    'pai': 'Clecio',
    'mae': 'Maria',
    'filha': 'Amora',
    'filho': 'Tobias'
}

print(f'Familia: {familia}')

# COPY
copia_familia = familia.copy()
print(f'Copia do dicionario familia: {copia_familia}')

# ITEMS
itens = familia.items()
print(f'Itens: {itens}')

for item in itens:
    print(f'Chave = {item[0]} e Valor = {item[1]}')

# KEYS

chaves = familia.keys()
print(f'Chaves: {chaves}')

# VALUES
valores = familia.values()
print(f'Valores: {valores}')

# SETDEFAULT
sobrinho = familia.setdefault('sobrinho', 'Dominic')
print(familia)

dicionario = {'a': 1, 'b': 2, 'c': 3}

resultado = 'd' in dicionario
excluido = dicionario.pop('a')
print(excluido)

linguagens = {}
print(linguagens)

linguagens = {
    'Python': 'Linguagem de programacao de alto nivel',
    'Java': 'Linguagem de programacao orientada a objeto',
    'JavaScript': 'Linguagem de programacao interpretada'
}

linguagens_populares = {
    'Python': 2,
    'Java': 1,
    'JavaScript': 3
}

linguagens_duplicadas = {
    'Python': 3,
    'Java': 3,
    'JavaScript': 3
}


descricao_java = linguagens['Java']

print(linguagens)
print(descricao_java)

if 'Python' in linguagens:
    python_existe = linguagens['Python']

    print(python_existe)

print(linguagens_populares)
linguagens_populares['Python'] = 4
del linguagens_populares['Java']

chaves = list(linguagens_populares.keys())  # Lista com as chaves do dicionario
valores = list(linguagens_populares.values())

itens = list(linguagens_populares.items())  # LISTA DE TUPLAS

print(linguagens_populares)
print(chaves)
print(valores)
print(itens)

for i in linguagens_duplicadas:
    if 5 in linguagens_duplicadas.values():
        print('5 existe')
        break

    else:
        print('5 nao existe')
        break

