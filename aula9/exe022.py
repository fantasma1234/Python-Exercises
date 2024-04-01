#programa que lê o nome de uma pessoa e mostra ele um maiusculo, minusculo, mostra quantas letras tem e quantas letras tem seu primeiro nome.
nome = str(input('digite seu nome completo: ')).strip()
d = nome.split()
print(f'seu nome em maiusculo fica assim {nome.upper()}')
print(f'seu nome em minusculo fica assim {nome.lower()}')
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print(f'seu primeiro nome tem {len(d[0])}')