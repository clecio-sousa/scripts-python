frutas = set()
frutas.add('banana')
frutas.add('abacaxi')
frutas.add('manga')

frutas2 = ('laranja', 'uva', 'banana')

frutas3 = frutas.intersection(frutas2)

print(frutas.issubset(frutas2))
print(frutas.isdisjoint(frutas2))

frutas.remove('manga')

print(frutas)
print('goiaba' in frutas)

print(type(frutas))

print(frutas3)