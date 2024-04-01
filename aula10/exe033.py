#programa que lê três valores e fala qual é o menor e o maior valor
n1 = float(input('digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
n3 = float(input('digite o terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'o menor valor digitado foi {menor} e o maior digitado foi {maior}')