from random import randint

alunos = ['tobias', 'Amora', 'Dominic', 'Clecio', 'Jesus']

for aluno in alunos:
    print(aluno)

for aluno in alunos:
    nota = randint(3, 10) # RANDINT = Numeros aleatorios
    print(f'A nota do aluno {aluno} foi {nota}')

for aluno in alunos:

    # 3 notas multiplicados pelo peso
    nota_1 = randint(0, 10) * 0.2
    nota_2 = randint(0, 10) * 0.3
    nota_3 = randint(0, 10) * 0.5

    nota_final = nota_1 + nota_2 + nota_3
    print(f'A nota final do aluno {aluno} foi {nota_final:.2f}')  # Saida limitada com 2 casas decimais