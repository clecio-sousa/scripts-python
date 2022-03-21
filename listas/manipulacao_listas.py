lista = ['clecio', 'jesus', 'maria', 'pedro']

# INDEX
posicao = lista.index('maria')
print(posicao)
print('clecio' in lista)
print('carlos' not in lista)

# COUNT
posicao = lista.count('jesus')
print(posicao)


# APPEND
lista.append('dominic')
print(lista)

# INSERT
lista.insert(0, 'joao')
print(lista)

# EXTEND

lista2 = ['carlos', 'rita', 'bel']
lista.extend(lista2)
print(lista)


# REVERSE

lista5 = [1, 2, 3, 4, 5]
lista5.reverse()
print(lista5)

# SORT
lista6 = [3, 5, 6, 7, 2, 1]
lista6.sort(reverse=True)  # ORDEM DECRESCENTE
lista6.sort(reverse=False) # ORDEM CRESCENTE
print(lista6)

# MIN E MAX

lista6 = [3, 5, 6, 7, 2, 1]
print(min(lista6))
print(max(lista6))

