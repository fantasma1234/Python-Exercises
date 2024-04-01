#programa que lê um nome e diz se nesse nome tem Silva
nome = str(input('digite seu nome: ')).strip().capitalize()
print('Seu nome tem Silva? {}'.format('Silva' in nome.capitalize()))

name = str(input('digite seu nome: ')).strip().capitalize()
print('Seu nome tem Silva? {}'.format(name[:].capitalize() == 'Silva'))
