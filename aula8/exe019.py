#programa que escolhe aleatóriamente o nome de um aluno para apagar o quadroS
import random
aluno1 = str(input('entre com o nome do primeiro aluno: '))
aluno2 = str(input('entre com o nome do segundo aluno: '))
aluno3 = str(input('entre com o nome do terceiro aluno: '))
aluno4 = str(input('entre com o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorte = random.choice(lista)
print(f'o aluno escolhido foi {sorte}')