#programa que lê um número Real e mostra a porção inteira| Ex: 6,127 sua parte inteira é o 6
import math
n = float(input('digite um número: '))
inteiro = math.trunc(n)
print(f'o número que você digitou foi {n} e sua parte inteira é {inteiro}')#com import math

#outra forma
a = float(input('digite um número: '))
print(f'o número que você digitou foi {a} e sua parte inteira é {int(a)}') #sem import math