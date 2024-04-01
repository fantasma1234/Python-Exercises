#programa que lê seu nome e fala seu primeiro nome e seu ultimo nome
nome = str(input('digite seu nome completo: ')).strip().title()
d = nome.split()
print('prazer em te conhecer!')
print('seu primeiro nome é {}'.format(d[0]))
print('seu ultimo nome é {}'.format(d[-1]))
print('seu ultimo nome é {}'.format(d[len(d) - 1]))