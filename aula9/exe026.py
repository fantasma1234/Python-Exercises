#programa que lê uma frase e diz quantas vezes aparece a letra A, sua primeira aparição e sua ultima aparição
frase = str(input('digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('Ela aparece pela ultima vez na posição {}'.format(frase.rfind('A') + 1))