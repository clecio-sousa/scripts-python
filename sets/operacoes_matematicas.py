homens = {'Joao', 'Clecio', 'Tobias', 'Dominic', 'Pedro', 'Antonio', 'Raimundo'}
alta_renda = {'Ana', 'Clecio', 'Joana', 'Antonio', 'Pedro', 'Carla', 'Adriana'}

print(f'Conjunto de homens: \t{homens}')
print(f'Conjunto de alta renda: {alta_renda}\n{"-" * 150}\n')

homens_alta_renda = homens.intersection(alta_renda)
uniao = homens.union(alta_renda)
homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)

print(f'Homens com alta renda: {homens_alta_renda}')
print(uniao)
print(homens_nao_alta_renda)
print(len(alta_renda_nao_homens))
