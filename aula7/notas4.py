#print(5 + 3 * 2)
#print(5 ** 2)
#print(pow(5,2)) #com pow perde a ordem de precedência
#print(5 ** 3)
#print(19 // 2)
#print(19 / 2)
#print(18 % 2)
#print(122 % 3)
#print(81 ** (1/2))
#print(25 ** 0.5)
#print(8 ** (1/3))
#print('oi' * 5)
#print('=' * 100)
nome = str(input('digite seu nome: '))
print(f'prazer em te conhecer {nome:20}!')
print(f'prazer em te conhecer {nome:>20}!')
print(f'prazer em te conhecer {nome:<20}!')
print(f'prazer em te conhecer {nome:^20}!')
print(f'prazer em te conhecer {nome:=^20}!')
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print(f'a soma vale {s}, \n a multiplicação vale {m} e a divisão vale {d:.2f}', end = ' ') #end serve para não quebrar a linha e \n serve para quebrar linha
print(f'a divisão inteira vale {di} e potência vale {p}')