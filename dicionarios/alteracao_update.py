computador = {
    'cpu': 'Core i7',
    'ram': 'DDR 16',
    'ssd': '128 GB',

}

print(computador)

# ATUALIZANDO VALORES
computador['ram'] = 'DDR 16 128GB'

print(computador)

# ADICIONANDO CHAVES
computador['fonte'] = 'Fonte padrão'
print(computador)

computador.update({'fonte': 'Corsair 850W'})
print(computador)

# EXCLUSAO DE ELEMENTOS

fila = {
    '0': 'Joao',
    '1': 'Clecio',
    '2': 'Jesus',
    '3': 'Amora'
}
# DEL
del fila['0']

# POP
fila.pop('1')

print(f'Fila inicial:{fila}')

# POPITEM (RETIRA O ULTIMO VALOR)

fila.popitem()
print(fila)

# CLEAR (LIMPA TODO O DICIONARIO)
fila.clear()
print(fila)