#  CRIANDO SETS

carteira = {'PETR4', 'CASH3', 'MGLU3', 'BBAS3', 'WEGE3'}

carteira.add('PETR4')

carteira.update({'ABEV3'})  # Atualizando

carteira.discard('PETR4')  # Removendo

item = carteira.pop()  # REMOVE O ULTIMO ELEMENTOs

print(carteira)
