nome = str(input('qual o seu nome?: '))
if nome == 'João':
    print('muito comum')
else:
    print('nome um pouco menos comum')
print(f'bom dia, {nome}')


n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m}')
if m >= 6:
    print('passou')
else:
    print('rodou')

#outra forma 

nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi {media}')
print('passou' if media >=6 else 'rodou')