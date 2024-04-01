print('\033[31mOlá, Mundo!')
print('\033[31;43mOlá, Mundo!\033[m')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')



a = 3
b = 5
print(f'os valores são \033[32m{a}\033[m e \033[31m{b}\033[m !!!')


nome = 'A'
print('olá, muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))


name = 'B'
cores = {'Limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo': '\033[33m', 
         'pretoebranco':'\033[7;30m'}
print('olá, muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], name, cores['Limpa']))