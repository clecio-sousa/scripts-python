from random import randint

capacidade_maxima_balde = 1000
balde = 0

while balde <= capacidade_maxima_balde:
    volume_copo = randint(95, 100)
    print(f'O copo foi enchido com {volume_copo}ml')
    balde += volume_copo

print(f'O volume do balde é de {balde} e  ultrapassou a capacidade maxima em {balde - capacidade_maxima_balde}ml')