#lê duas notas de um aluno e calcula sua média
nome = str(input('digite o nome do aluno/aluna: '))
n1 = float(input('digite a primeira nota do aluno/aluna: '))
n2 = float(input('digite a segunda nota do aluno/aluna: '))
media = (n1 + n2) / 2
print(f'aluno/aluna {nome} tirou as notas {n1:.2f} e {n2:.2f}, sua média foi de {media:.2f}')