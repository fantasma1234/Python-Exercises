#programa que lê um número de 0 até 9999 e mostra cada um dos digitos separados
num = int(input('digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'o número tem {m} milhares')
print(f'o número tem {c} centenas')
print(f'o número tem {d} dezenas')
print(f'o número tem {u} unidades')